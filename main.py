import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="psvmsout"
)
cursorObject = database.cursor()
# cursorObject.execute("DROP DATABASE MyNewDatabase")

cursorObject.execute("CREATE DATABASE MyNewDatabase")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database = 'MyNewDatabase',
    passwd="psvmsout"
)

if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL server", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database() ")
    record = cursor.fetchone()
    print("Connected to database", record)

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='MyNewDatabase',
        user='root',
        password='psvmsout'
    )
    mySql_Create_Table_Query = """
     CREATE TABLE Marvel(
     ID int(10) NOT NULL,
     MOVIE varchar(50) NOT NULL,
     DATE varchar(10) NOT NULL,
     MCUPHASE varchar(10))"""

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Students Table created.")

    cursor.execute("SHOW TABLES")

    for table_name in cursor:
        print(table_name)
except mysql.connector.Error as error:
    print("FAILED: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL is closed")

file_bject = open("Marvel.txt")

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='MyNewDatabase',
        user='root',
        password='psvmsout'
    )
    CursorObject = connection.cursor()

    while file_bject:
        text = file_bject.readline()
        if text == "":
            break
        splitLines = text.split()
        Insert = """INSERT INTO marvel (ID, MOVIE, DATE, MCU_PHASE)
                 VALUES (%s, %s, %s, %s)"""
        record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
        CursorObject.execute(Insert, record)
        connection.commit()
    print("Records are inserted into Marvel table.")
    CursorObject.close()

    sql_select = "SELECT MOVIE FROM marvel"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_select)
    records = cursorObject.fetchall()

    for row in records:
        print(row)

    sql_remove = "DELETE FROM marvel WHERE MOVIE= 'TheIncredibleHulk'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_remove)
    connection.commit()

    sql_list = "SELECT * FROM marvel WHERE MCU_PHASE='Phase2'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_list)
    records1 = cursorObject.fetchall()

    for row1 in records1:
        print(row1)

    sql_update = "UPDATE marvel SET DATE= 'November 3, 2017' WHERE MOVIE='Thor:Ragnarok'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_update)
    connection.commit()

except mysql.connector.Error as error:
    print("Failed while inserting record into marvel table {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed. ")