
import sys
import os
import sqlite3


       
def main():


    def menu():
        print("MAIN MENU")
    
    print()

    case_selection = input("""
                      A: Show All Cases in Registry
                      B: Search for Cases
                      C: Add a Case
                      D: Modify a Case
                      Q: Quit
            

                      Please enter your choice: """)

    if case_selection == "A" or case_selection =="a":
        print(show_all_cases())
    elif case_selection == "B" or case_selection =="b":
        search_all_cases()
    elif case_selection == "C" or case_selection =="c":
        add_a_case()
    elif case_selection=="D" or case_selection=="d":
        modify_a_case()
    elif case_selection=="Q" or case_selection=="q":
        write_to_file()
        sys.exit()

    else:
        print("Unknown Error")
        print("Please try again")
        menu()
    
CASE_TABLE_NAME = "Case" 
CASE_TABLE_FIELDS = [
    ("id",          "VARCHAR"),
    ("description", "VARCHAR"),
    ("tags",        "VARCHAR"),
    ("date",        "VARCHAR"),
]



def write_to_file():
    fout = open('/Users/jarvisbigger/code_work/code_work-master/Case/Case/registry.txt','w')
    fout.write(str(show_all_cases()))
    fout.close()


def create_connection(db_file):
    
    
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
   

    conn.commit()
    conn.close()
    return rows
  


def search_all_cases():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    search = input("Please search for your desired case:")
    cur.execute("SELECT * FROM Cases WHERE tags LIKE '%open%'")
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
    sql = "INSERT INTO Cases (id,description, tags, date) VALUES (?,?,?,?)"
    conn.execute(sql, (case_id,case_description,case_tag,case_date))
    conn.commit()
    conn.close()
    
    
  
  

def modify_a_case():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    update = input('Would you like to change the tag or description[y/N]: ')
    if update.lower() == 'y':
        old_tag= input('Old tag: ')
        new_tag = input('Update your tag: ')
        cur.execute('UPDATE Cases SET tags=? WHERE tags=?', (new_tag, old_tag))
    else:
        updated = input("Please change your description. Please enter") 
        old_description = input('Old description: ')
        new_description = input('Update your description: ')
        cur.execute('UPDATE Cases SET description=? WHERE description=?', (new_description, old_description))


    conn.commit()
    conn.close()
   
    pass



while True:
    main()
main()
