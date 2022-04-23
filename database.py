import psycopg2



def insert(name,Class,roll):
    print(name,roll,Class) 
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom.cbzzzaywzhby.us-east-1.rds.amazonaws.com", port = "5432")

    cur=con.cursor()
    cur.execute(f"INSERT INTO students (name,class,roll) values ('{name}',{Class},{roll});")
    con.commit()
    con.close()

def show():
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom.cbzzzaywzhby.us-east-1.rds.amazonaws.com", port = "5432")
    cur=con.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows
def delete(id):
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom.cbzzzaywzhby.us-east-1.rds.amazonaws.com", port = "5432")
    cur=con.cursor()
    cur.execute(f"DELETE from students where id={id}")
    con.commit()
    con.close()

def findone(id):
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom.cbzzzaywzhby.us-east-1.rds.amazonaws.com", port = "5432")
    cur=con.cursor()
    cur.execute(f"Select * from students where id={id}")
    rows=cur.fetchone()
    con.commit()
    con.close()
    return rows

def update(id,name,roll,Class):
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom.cbzzzaywzhby.us-east-1.rds.amazonaws.com", port = "5432")
    cur=con.cursor()
    cur.execute(f"Update students set name='{name}' , roll={roll},class={Class} WHERE id={id}")
    con.commit()
    con.close()



