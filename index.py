import sqlite3

class Connection:

    db = sqlite3.Connection("Movies.db")
    db.execute("Create table if not exists movies(id int primary key, name varchar(60), actor varchar(30), actress varchar(30), director varchar(30), release_year int)")
    print("Table Successfully created")

    def insert(self):
        id = int(input("Enter Id: "))
        name = input("Enter Movie Name: ")
        actor_name = input("Enter Actor Name: ")
        actress_name = input("Enter Actress Name: ")
        director_name = input("Enter Director Name: ")
        release_year = int(input("Enter Release Year: "))

        self.db.execute("insert into movies(id, name, actor, actress, director, release_year) values(?, ?, ?, ?, ?, ?)", (id, name, actor_name, actress_name, director_name, release_year))
        self.db.commit()
        print("Data Inserted Succesfully")

    def display(self):
        data = self.db.execute("select * from movies")
        for row in data:
            print("Id: {}, Name: {}, Actor: {}, Actress: {}, Director: {}, Release Year: {}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def update(self):
        print("Update Table Data: ")

        id = int(input("Enter Id: "))
        name = input("Enter Movie Name: ")
        actor_name = input("Enter Actor Name: ")
        actress_name = input("Enter Actress Name: ")
        director_name = input("Enter Director Name: ")
        release_year = int(input("Enter Release Year: "))

        self.db.execute("update movies set name = ?, actor = ?, actress = ?, director = ?, release_year = ? where id = ?", (id, name, actor_name, actress_name, director_name, release_year))
        self.db.commit()
        print("Data Updated Succesfully")

    def delete(self):
        print("Delete Table")

        id = int(input("Enter Id: "))
        self.db.execute("delete from movies where id = ?", (id))
        self.db.commit()
        print("Data Deleted Succesfully")

# con = Connection()
# con.insert()
# con.display()
# con.update()

while(True):
    print("1. Add Movie")
    print("2. View Movie")
    print("3. Update Movie")
    print("4. Delete Movie")

    var = int(input("Choose from 1-4: "))
    
    if var == 1:
        con = Connection()
        con.insert()
    elif var == 2:
        con = Connection()
        con.display()
    elif var == 3:
        con = Connection()
        con.update()
    elif var == 4:
        con = Connection()
        con.delete()
    else:
        print("Enter Valid Choise")