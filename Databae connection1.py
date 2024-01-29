import cx_Oracle


oracle_connection = {
    'user': 'system',
    'password': 'xxxxxxxxx',
    'dsn': 'localhost:1521/xe'  
}


connection = cx_Oracle.connect(**oracle_connection)


cursor = connection.cursor()

try:

    admin_table_query = '''
    CREATE TABLE Admin_tbl (
        ID VARCHAR(25),
        username VARCHAR(255),
        password VARCHAR(255),
        name VARCHAR(255),
        surname VARCHAR(255),
        cell VARCHAR(20),
        email VARCHAR(255),
        employee_id NUMBER(8,2),
        PRIMARY KEY (ID)
    )
    '''

   
    cursor.execute(admin_table_query)

   
    connection.commit()

except cx_Oracle.DatabaseError as e:
   
    print(f"Database Error: {e}")

finally:
    
    cursor.close()
    connection.close()
