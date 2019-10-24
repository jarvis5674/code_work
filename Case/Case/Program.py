import sys
import os
import sqlite3


       
def main():


    def menu():
        print("MAIN MENU")
    
    print()

    case_selection = input("""
                      A: Show All Cases in Registry
                      B: Search for All Cases
                      C: Add a Case
                      D: Modify a Case
                      Q: Quit
            

                      Please enter your choice: """)

    if case_selection == "A" or case_selection =="a":
        show_all_cases()
    elif case_selection == "B" or case_selection =="b":
        search_all_cases()
    elif case_selection == "C" or case_selection =="c":
        add_a_case()
    elif case_selection=="D" or case_selection=="d":
        modify_a_case()
    elif case_selection=="Q" or case_selection=="q":
        sys.exit
    else:
        print("Unknown Error")
        print("Please try again")
        menu()
    


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def show_all_cases():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cases")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    pass
  


def search_all_cases():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    search = input("Please search for your desired case:")
    cur.execute(f"SELECT * FROM Cases WHERE description LIKE '%{search}%'")
    cur.execute("SELECT * FROM Cases WHERE tags LIKE '%open%'")
    cur.execute("SELECT * FROM Cases WHERE tags LIKE '%closed%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    conn.close()
    pass
    

def add_a_case():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    case_id = input("What is the Case ID? ")
    case_description = input("What is the case description? ")
    case_tag =  input("What is the tag?")
    case_date = input("Please format YYYY:MM:DD"  )
    cur.execute('''INSERT INTO Cases(id,description,tags, date)
              VALUES(?,?,?,?)''', [case_description])
    
    conn.commit()
    conn.close()
    pass
    
  
  

def modify_a_case():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cases")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    pass




main()
