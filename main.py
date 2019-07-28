import datetime
import psycopg2
import time

# kali ini kita akan mengkonekan python ke postgresql
now = datetime.datetime.now()
now = str(now)
username = input("masukan username anda : \n")
password = input("masukan password anda : \n")


# berikut ini adalah syntaq SQL nya
sql = f"INSERT INTO username (username, password) VALUES ('{username}','{password}') RETURNING (nomer);"

try:
    # menjadikan variabel conn sebagai koneksinya
    conn = psycopg2.connect(user = "postgres", password = "fadliselaz13", 
                            host = "35.224.102.180", port = "5432",
                            database = "fadli")

    # menjadikan variable cursor
    cursor = conn.cursor()
    print(conn.get_dsn_parameters(), "\n")
    cursor.execute(sql)
    conn.commit()
    record = cursor.fetchall()
    print("you are connect to ", record, "\n")
    print(record)
        
except Exception as err:
    print("eerroro ngak bisa..", err)

finally:
    if conn:
        print("berhasil tambah data")
        cursor.close()
        conn.close()

