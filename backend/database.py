import psycopg2
def get_connection():
    conn=psycopg2.connect(
        host="localhost",
        database="carromdb",
        user="postgres",
        password="1234"
)
    return conn