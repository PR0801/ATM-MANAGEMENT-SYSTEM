import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='root',database='atm')
c1=conn.cursor()
print("================================================================================")
print("WELCOME TO OUR ATM")
print("================================================================================")
print("1. CREATE ACCOUNT")
print("2. LOGIN")
print("3. EXIT")
print("================================================================================")
op=int(input("Enter your choice :"))
print("================================================================================")
if op==1:
      c="y"
      while c=="y":
            print("================================================================================")
            print("SERVER CONNECTED")
            print("================================================================================")
            print("WE HOPE YOU WOULD LIKE OUR SERVICES")
            m=int(input("Enter a 4 digit number to set as your account number : "))
            cb="select * from records where ACCOUNT_NO={}".format(m)
            c1.execute(cb)
            d=c1.fetchall()
            data=c1.rowcount
            if data==1:
                  print("================================================================================")
                  print("This account number already exists in our system")
                  print("================================================================================")
                  c=input("Do you want to continue y/n -")
                  print("================================================================================")
                  if c=="y" or c=="Y":
                        continue
                  else:
                        print("THANK YOU")
                        print("================================================================================")
                        print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                        print("VISIT AGAIN")
                        print("================================================================================")
            else:
                  name=input("Enter your name:")
                  passw=int(input("Enter your password:"))
                  ab="insert into records(ACCOUNT_NO,PASSWORD,NAME) values({},{},'{}')".format(m,passw,name)
                  print("================================================================================")
                  c1.execute(ab)
                  conn.commit()
                  print("ACCOUNT CREATED SUCCESSFULLY")
                  print("================================================================================")
                  print("The minimum balance for a account in our bank is Rs 1000 ")
                  print("================================================================================") 
                  s=int(input("Enter the amount to be deposited : "))
                  print("================================================================================")
                  sr="update records set  CR_AMT={} where ACCOUNT_NO={}".format(s,m)
                  c1.execute(sr)
                  conn.commit()
                  ef="update records set balance=cr_amt-withdrawl where ACCOUNT_NO={}".format(m)
                  c1.execute(ef)
                  conn.commit()
                  print("SUCCESSFULLY DEPOSITED")
                  print("================================================================================")
                  print("THANK YOU")
                  print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                  print("VISIT AGAIN")
                  print("================================================================================")
                  print("SERVER DISCONNECTED")
                  print("================================================================================")
                  break
if op==2:
      y="y"
      while y=="y":            
            acct=int(input("Enter your account number:"))
            cb="select * from records where ACCOUNT_NO={}".format(acct)
            c1.execute(cb)
            c1.fetchall()
            data=c1.rowcount
            if data==1:
                  pas=int(input("Enter your password  : "))
                  print("================================================================================")
                  e="select password from records where ACCOUNT_NO={}".format(acct)
                  c1.execute(e)
                  a=c1.fetchone()
                  d=list(a)
                  if pas==d[0]:
                        print("================================================================================")
                        print("SERVER CONNECTED SUCCESSFULLY")
                        print("================================================================================")
                        print("Your account has been found in our system")
                        print("The Password entered by you is corrrect")
                        print("================================================================================")
                        print("1. DEPOSIT")
                        print("2. WITHDRAW")
                        print("3. TRANSFER")
                        print("4. CHECK BALANCE")
                        print("5. CHANGE ACCOUNT NUMBER")
                        print("6. CHANGE PASSWORD")
                        print("7. CLOSE ACCOUNT")
                        print("================================================================================")
                        r=int(input("Enter your choice:"))
                        print("================================================================================")
                        if r==1:
                              amt=int(input("Enter the amount of money to be deposited : "))
                              print("================================================================================")
                              sr="update records set CR_AMT=CR_AMT + {} where ACCOUNT_NO={}".format(amt,acct)
                              c1.execute(sr)
                              conn.commit()
                              ef="update records set balance=cr_amt-withdrawl where ACCOUNT_NO={}".format(acct)
                              c1.execute(ef)
                              conn.commit()
                              print("SUCCESSFULLY DEPOSITED")
                              print("================================================================================")
                              t=input("Do you want to continue y/n -")
                              print("================================================================================")
                              if t=="y" or t=="Y":
                                    continue
                              else:
                                    print("THANK YOU")
                                    print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                        if r==2:
                              amt=int(input("Enter the money to withdraw : "))
                              print("================================================================================")
                              ah="select  BALANCE from records where account_no={}".format(acct)
                              c1.execute(ah)
                              m=c1.fetchone()
                              if amt >m[0]:
                                    print("Your account balance is less than",amt)
                                    print("Please first Deposit money in your account.")
                                    print("PLEASE TRY AGAIN LATER")
                                    print("================================================================================")
                              else:
                                    sr="update records set balance=balance - {}  where ACCOUNT_NO={}".format(amt,acct)
                                    ed="update records set  WITHDRAWL ={}  where ACCOUNT_NO={}".format(amt,acct)
                                    c1.execute(ed)
                                    c1.execute(sr)
                                    conn.commit()
                                    print("SUCCESSFULLY UPDATED")
                                    print("================================================================================")
                              y=input("Do you want to continue y/n -")
                              if y=="y" or y=="Y":
                                    continue
                              else:
                                    print("THANK YOU")
                                    print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                                    print("================================================================================")
                        if r==3:
                              act=int(input("Enter the account number to transfer funds : "))
                              print("================================================================================")
                              cb="select * from records where ACCOUNT_NO={}".format(act)
                              c1.execute(cb)
                              c1.fetchall()
                              data=c1.rowcount
                              if data==1:
                                    print(act ,"ACCOUNT NUMBER FOUND")
                                    print("================================================================================")
                                    m=int(input("Enter the amount to be transferred : "))
                                    print("================================================================================")
                                    ah="select  BALANCE from records where account_no={}".format(acct)
                                    c1.execute(ah)
                                    c=c1.fetchone()
                                    if m > c[0]:
                                          print("INSUFFICIENT FUNDS")
                                          print("================================================================================")
                                          print("Your account balance is less than",m)
                                          print("Please Deposit sufficient amount in your account first")
                                          print("PLEASE TRY AGAIN LATER")
                                          print("================================================================================")
                                    else:
                                          av="update records set balance=balance-{} where ACCOUNT_NO={}".format(m,acct)  
                                          cv="update records set balance=balance+{} where ACCOUNT_NO={}".format(m,act)
                                          w="update records set withdrawl=withdrawl+{} where account_no={}".format(m,acct)
                                          t="update records set  CR_AMT=CR_AMT+{} where account_no={}".format(m,act)
                                          c1.execute(av)
                                          c1.execute(cv)
                                          c1.execute(w)
                                          c1.execute(t)
                                          conn.commit()
                                          print("SUCCESSFULLY TRANSFERED")
                                          print("================================================================================")
                                    y=input("Do you want to continue y/n -")
                                    if y=="y" or y=="Y":
                                          continue
                                    else:
                                          print("THANK YOU")
                                          print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                                          print("================================================================================")
                        if r==4:
                              ma="select balance from records where account_no={}".format(acct)
                              c1.execute(ma)
                              k=c1.fetchone()
                              print("Balance in your account=",k[0])
                              print("================================================================================")
                              y=input("Do you want to continue y/n -")
                              if y=="y":
                                    continue
                              else:
                                    print("THANK YOU")
                                    print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                                    print("================================================================================")
                        if r==5:
                              i=int(input("Enter your new account number : "))
                              cb="select * from records where ACCOUNT_NO={}".format(i)
                              c1.execute(cb)
                              c1.fetchall()
                              data=c1.rowcount
                              if data==1:
                                    print("This account number already exists")
                                    print("TRY AGAIN")
                                    print("================================================================================")
                                    y=input("Do you want to continue y/n -")
                                    if y=="y":
                                          continue
                                    else:
                                          print("Thank you")
                                          print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                                          print("================================================================================")
                              else:
                                    name=input("Enter your name : ")
                                    print("================================================================================")
                                    ar="Update records set account_no={} where name='{}' and password={}".format(i,name,pas)
                                    c1.execute(ar)
                                    conn.commit()
                                    print("================================================================================")
                                    print("ACCOUNT NUMBER UPDATED SUCCESSFULLY")
                                    print("Your new account number is ",i)
                                    print("================================================================================")
                        if r==6:
                             i=int(input("Enter your Account Number :"))
                             cb="select * from records where ACCOUNT_NO={}".format(i)
                             c1.execute(cb)
                             c1.fetchall()
                             data=c1.rowcount
                             if data==1:
                                  p=int(input("Enter your Password : "))
                                  n=input("Enter your name : ")
                                  print("================================================================================")
                                  ar="Update records set PASSWORD={} where NAME='{}' and ACCOUNT_NO={};".format(p,n,i)
                                  c1.execute(ar)
                                  conn.commit()
                                  print("PASSWORD UPDATED SUCCESSFULLY")
                                  print("================================================================================")
                                  print("================================================================================")
                                  y=input("Do you want to continue y/n -")
                                  if y=="y":
                                          continue
                                  else:
                                        print("================================================================================")
                                        print("SERVER DISCONNECTED")
                                        print("================================================================================")
                                        print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
                                        print("THANK YOU")
                                        print("================================================================================")
                                        break
                             else:
                                  print("ACCOUNT NUMBER NOT FOUND")
                                  print("PLEASE ENTER A VALID ACCOUNT NUMBER")
                                  print("================================================================================")
                             
                        if r==7:
                            a=int(input("Enter your Account Number : "))
                            print("================================================================================")
                            d="select * from records where ACCOUNT_NO={}".format(a)
                            c1.execute(d)
                            c1.fetchall()
                            data=c1.rowcount
                            if data==1:
                                print("Your Account exists in our System")
                                print("================================================================================")
                                de="delete from records where ACCOUNT_NO={};".format(a)
                                c1.execute(de)
                                conn.commit()
                                print("ACCOUNT CLOSED SUCCESSFULLY")
                                print("================================================================================")
                                break
                            else:
                                print("Please enter a valid Account Number")
                                print("================================================================================")
                  else:
                        print("WRONG PASSWORD")
                        print("================================================================================")
                        y=input("Do you want to continue y/n -")      
            else:
                  print("Your Account does not exists")
                  print("================================================================================")
                  print("OR")
                  print("================================================================================")
                  print("Try re-entering your ACCOUNT NUMBER and PASSWORD")
                  print("================================================================================")
if op==3:
      print("SERVER DISCONNECTED")
      print("================================================================================")
      print("PLEASE CLOSE THIS FILE BEFORE CLOSING THIS WINDOW")
      print("THANK YOU")
      print("================================================================================")
      c1.close()
