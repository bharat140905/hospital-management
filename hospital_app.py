import sqlite3

with sqlite3.connect('hospital.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patient(
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            issue   TEXT NOT NULL,
            amount  REAL
        )
    ''')
    conn.commit()

while True:
    print("\n1. Add patient")
    print("2. Update amount")
    print("3. Delete patient")
    print("4. View all")
    print("5. Exit")

    choice = input("CHOOSE OPTION: ")

    if choice == "1":
        name = input("Patient name: ")
        issue = input("Issue: ")
        amount = int(input("Amount: "))
        with sqlite3.connect('hospital.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO patient(name,issue,amount) VALUES(?,?,?)', (name, issue, amount))
            conn.commit()
        print("Patient added !")

    elif choice == "2":
        update_name = input("ENTER THE PATIENT WHOSE AMOUNT TO BE UPDATE : ")
        new_amount = int(input("ENTER NEW AMOUNT: "))
        with sqlite3.connect('hospital.db') as conn:
            cursor =conn.cursor()

            cursor.execute('UPDATE patient SET amount =? WHERE name =?', (new_amount,update_name))
            conn.commit()
        print("patient updated !")
        

    elif choice == "3":
         del_name = input(" WHICH PATIENT TO DELETE ? :")
         with sqlite3.connect('hospital.db') as conn:
          cursor =conn.cursor()
          cursor.execute('DELETE FROM patient WHERE name =?', (del_name,))
          conn.commit()
         print(f"patient :{del_name} is deleted !")

        


    elif choice == "4":
        with sqlite3.connect('hospital.db') as conn:
            cursor =conn.cursor()
            cursor.execute('SELECT * FROM patient')
            rows =cursor.fetchall()
            for row in rows:
                print(row)

    elif choice == "5":
        print("HAVE A GOOF DAY !")
        break