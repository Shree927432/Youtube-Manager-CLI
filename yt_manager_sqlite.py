import sqlite3

con = sqlite3.connect("/Users/shrikantpawade/Documents/python_revisit/SQLite/youtube_manager/Youtube_manager.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS videos 
               (video_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
""")

def show_all():
    cursor.execute("SELECT * FROM videos ")
    print("Id| Name       |   Time")
    print("-----------------------")
    for row in cursor.fetchall():
        print(f"{row[0]} |{row[1]} | {row[2]}")


def add_record(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    con.commit()


def update_record(new_name,new_time,id):
    cursor.execute("""UPDATE videos
                  SET name = ?, time = ? WHERE video_id = ? """,(new_name,new_time,id))
    con.commit()

def delete_record(id):
    cursor.execute("""DELETE FROM videos WHERE video_id = ?""",(id,))

    con.commit()


def main():
    try:
        while True:
            print("\nYOUTUBE MANAGER")
            print("---------------")
            print("1.List all Youtube videos")
            print("2.Add a youtube video.")
            print("3.Update a youtube video.")
            print("4.Delete a youtube video.")
            print("5.Exit the app.\n")

            choice = input("Enter your choice :")
            
            match choice:
                case '1':
                    show_all()

                case '2':
                    name = input("Enter name of video :")
                    time = input("Enter time :")
                    add_record(name,time)
                
                case '3':
                    show_all()
                    id = input("Select id to update :")
                    new_name = input("Enter new name :")
                    new_time = input("Enter new time :")
                    update_record(new_name,new_time,id)

                case '4':
                    show_all()
                    id = input("Enter id to delete :")
                    delete_record(id)
                    print(id , " has been deleted.")
                
                case '5':
                    break

                case _ :
                    print("Invalid Choice!")  
    finally:
        con.close()     


if __name__ == "__main__":
    main()
