import sys
import os
import sqlite3
import re


       
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
    cur.execute("SELECT * FROM Cases")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    pass


def add_a_case():
    db_name = "/Users/jarvisbigger/Downloads/database.db"
    conn = create_connection(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cases")
    rows = cur.fetchall()
    for row in rows:
        print(row)
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

def show_id():
        """ local function for showing all values from table Case"""
        show_statement = "SELECT * FROM id;"
        cur.execute(show_statement)
        rows = cur.fetchall()

        print(rows)

def show_description():
        """ Local function for showing all values form table Case """
        show_statement = "SELECT * FROM description ORDER BY id DESC"
        cur.execute(show_statement)
        rows = cur.fetchall()

        print(rows)

def show_tags():
        """ local function for showing all values from table Case"""
        show_statement = "SELECT * FROM tags"
        cur.execute(show_statement)
        rows = cur.fetchall()

        print(rows)

def show_date():
        """ local function for showing all values from table Case"""
        show_statement = "SELECT * FROM date"
        cur.execute(show_statement)
        rows = cur.fetchall()

        print(rows)



main()
