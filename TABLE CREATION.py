import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='root',database='ATM')
if conn.is_connected():
      print("sucessfully connected")
c1=conn.cursor()
mn="CREATE TABLE RECORDS( ACCOUNT_NO  INT(4) primary key,PASSWORD INT(3),NAME VARCHAR(20),CREDIT_AMT INT default(0),WITHDRAWL INT default(0),BALANCE INT default(0))"
c1.execute(mn)
print("Sucessfulluy created")
