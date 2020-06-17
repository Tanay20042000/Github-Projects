import sqlite3

class Contact:
    
    def add(db,name,call):
        cur1 = db.cursor()
        cur1.execute('insert into phone values(?,?)', (name, call))
        pass
    
    def delete(db,name):
        cur2 = db.cursor()
        cur2.execute('delete from phone where name = (?)', (name,))
        pass
    
    def view(db):
        cur3 = db.cursor()
        cur3.execute('select * from phone')
        cts = cur3.fetchall()
        return cts
    
    def edit1(db,name,call):
        cur4 = db.cursor()
        db.execute('update phone set name = (?) where ph_no = (?)', (name, call))
        pass
    
    def edit2(db,name,call):
        cur5 = db.cursor()
        cur5.execute('update phone set ph_no = (?) where name = (?)', (call, name))
        pass
    
    def search1(db,names):
        cur6 = db.cursor()
        cur6.execute("SELECT * FROM phone WHERE name = ?",(names,))
        row1 = cur6.fetchall()
        for i in row1:
            print(i)
        pass
    
    def search2(db,calls):
        cur7 = db.cursor()
        cur7.execute("SELECT * FROM phone WHERE ph_no = ?",(calls,))
        row1 = cur7.fetchall()
        for i in row1:
            print(i)
        pass