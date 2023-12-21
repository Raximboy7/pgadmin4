import psycopg2


db = psycopg2.connect(
    database = 'Payshanba',
    password='0000',
    user='postgres',
    host='localhost'
)

cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
   user_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
   name VARCHAR(40),
   lastname VARCHAR(40),
   contact VARCHAR(15) UNIQUE
)''')

cursor.execute('''INSERT INTO users(name, lastname, contact)
VALUES (%s, %s, %s)
ON CONFLICT DO NOTHING''',('Odilbek', 'Murodaov', '12112133132'))



db.commit()
db.close()
