import sys
import pickle
user=open(r'C:\Users\asus\.idlerc\userrec.bin','ab')

import random
import string
def passgenerator():
password=[]
passlength=random.randrange(2,4)
for i in range(passlength):
upper=random.choice(string.ascii_uppercase)
password.append(upper)
digit=random.choice(string.digits)
password.append(digit)
random.shuffle(password)
finalpass=''.join(password)
#.join() converts list to string
passgenerator.passw=finalpass
#function attribute
return finalpass
#CONFIRMATION MODULE

def amt_display():
print('''
Your details are confirmed.Amount to be paid is displayed
below.

''')

tprice=price_tick*no_tick
print("Price of ticket:",price_tick,'*',no_tick,'=',tprice)
print("Price of refreshments:",price_refn)
total=int(tprice)+int(price_refn)
print("Total amount to be paid:",total)
print('ENJOY YOUR MOVIE!!')
print('.'*80)
print("Press 'u' to go back to the homepage")
print('Press "m" to go back to choose a movie')
c=input()
if c in ['u','U']:
welcomepage()
if c in ['m','M']:

movie_module()

def display():
print("The details of your booking are provided below")
print('.'*167)
print(' '*75,'Movie name :',movie_name,' '*75)
print(' '*75,'Number of tickets:',no_tick,' '*75)
print(' '*75,"Theatre chosen:'",theatre,' '*75)
print(' '*75,'Time:',time,' '*75)
print(' '*75,'Refreshments(with price):',s_list,' '*75)
price_ref=0
for i in s_list:
for value in i:
price_ref=price_ref+i[value]
global price_refn
price_refn=price_ref

#DISPLAY DETAILS
def conf_module():
display()

#ASKING THE USER TO CONFIRM DETAILS
while True:
conf=input('Shall the details be confirmed?(y/n):')

#DISPLAYING THE PAYMENT DETAILS IF DEAILS ARE
CONFIRMED
if conf in 'Yy':
amt_display()
break

#IF THE USER WISHES TO CHANGE THE DETAILS
if conf in 'Nn':
while True:
print('''
1.TIME
2.NO OF TICKETS
3.NONE''')
c=int(input("Enter the number corresponding to the detail you wish to change:"))
if c==1:
def time():
print('''CHOOSE YOUR TIMINGS FOR THE MOVIE

1.9.00-12.00 AM
2.1.00-4.00 PM
3.5.30-8.30 PM
4.9.00-12.00 PM
''')
t=int(input("ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE:"))
global time
if t==1:
time='9.00-12.00 AM'
if t==2:
time='1.00-4.00 PM'
if t==3:
time='5.30-8.30 PM'
if t==4:
time='9.00-12.00 PM'

time()
print('TIME CHANGED')
display()
amt_display
break

elif c==2:
def no_tick():
global no_tick
no_tick=int(input("ENTER THE NUMBER OF TICKETS YOU WANT:"))
no_tick()
print('NO OF TICKETS CHANGED')
display()
amt_display()
break

elif c==3:
amt_display()
break

#BOOKING MODULE

#DISPLAYING THE DETAILS OF ALL THEATRES
#DISPLAYING THE DETAILS OF ALL THEATRES
def read_theatre():

import pickle
fin=open(r'C:\Users\asus\.idlerc\THEATRE.dat','rb')
data=[]
print('*'*167)
print('Data stored in file....................')
while True:
try:
data=pickle.load(fin)
print('THEATRE NAME:', data[0])
print('LOCATION:',data[1])
print('SEATING CAPACITY:',data[2])
print('PRICE OF A TICKET:', data[3])
print('REFRESHMENTS AVAILABLE(price in bracket):', data[4])
print('.'*167)

except EOFError:
fin.close()
break

#BOOKING MODULE

def booking_module():
print('*'*90)
print('''PLEASE SELECT THE NUMBER CORRESPONDING TO
YOUR CHOICE

1.DISPLAY ALL THEATRES
2.SEARCH THEATRE
3.GO BACK TO MOVIE MODULE''')
i=int(input())
if i==1:
print("...........THEATRES AVAILABLE FOR WATCHING THE MOVIE ALONG WITH ITS DETAILS...........")
read_theatre()
elif i==2:
while True:
search_theatre()
print()
print()
j=input('DO YOU WISH TO SEARCH FOR ANY OTHER THEATRE?(Y/N):')
if j in "nN":
break
elif i==3:
movie_module()
else:

print("INVALID CHOICE")
global theatre
theatre=input("ENTER THE NAME OF THE THEATRE YOU WISH TO WaTCH THE MOVIE:").upper()

def time():
print('.'*167)
print('''CHOOSE YOUR TIMINGS FOR THE MOVIE
1.9.00-12.00 AM
2.1.00-04.00 PM
3.5.30-08.30 PM
4.9.00-12.00 PM
''')

t=int(input("ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE:"))
global time
if t==1:
time='9.00-12.00 AM'
if t==2:
time='1.00-4.00 PM'
if t==3:
time='5.30-8.30 PM'
if t==4:
time='9.00-12.00 PM'

def no_tick():
global no_tick
print()
no_tick=int(input("ENTER THE NUMBER OF TICKETS YOU WANT:"))

time()
no_tick()

import pickle
fin=open(r'C:\Users\asus\.idlerc\THEATRE.dat','rb')
data=[]
try:
while True:
data=pickle.load(fin)
if theatre==data[0]:
global price_tick
price_tick=int(data[3])
global ref_t
ref_t=data[4]
except Exception:

fin.close()
print()
print()
print('.'*167)
print('THE SNACKS AVAILABLE IN THE THEATRE ARE DISPLAYED BELOW ALONG WITH THEIR PRICE:')
global s_list
s_list=[]
while True:
j=1
for i in ref_t:
print(j,i)
j=j+1
ref_n=int(input('''ENTER THE NUMBER CORRESPONDING TO THE SNACKS YOU WANT:(PRESS '0' IF YOU WANT NONE)'''))

if ref_n==0:
s_list=[]
print('............REDIRECTING TO CONFIRMATION MODULE............')
conf_module()
break
ref=ref_t[ref_n-1]

no_s=int(input('HOW MANY OF THE ABOVE SNACK DO YOU WANT?'))
for key in ref:
s=key
for key in ref:
p=ref[key]
ref_price=p*no_s
ref_n={s:ref_price}
s_list.append(ref_n)
a=input('DO YOU WISH TO HAVE ANY MORE SNACKS(Y/N):')
if a in 'nN':
print()
print()
print()
print('............REDIRECTING TO CONFIRMATION MODULE............')
conf_module()
break
else:
continue

#ADDING A NEW THEATRE
def add_theatre():
import pickle
outfile=open(r'C:\Users\asus\.idlerc\THEATRE.dat','ab+')
while True:
thr_name=input("Enter the name of the theatre:").upper()
thr_loc=input("Enter the location of theatre:")
thr_seat=input("Enter the seating capacity of the theatre:")
price_tick=input("Enter the price of each ticket:")
snack=[]
s_no=int(input("Enter the no of snacks and drinks available:"))
for i in range(s_no):
s=input("Enter the name of the snack/drink:")
p=int(input("Enter the price of the above snack/drink:"))
temp={s:p}
snack.append(temp)
theatre_details=[thr_name,thr_loc,thr_seat,price_tick,snack]
pickle.dump(theatre_details,outfile)
choice=input('Do you want to enter details of more theatres(y/n):')
if choice in 'nN':
break
outfile.close()

#SEARCHING FOR A THEATRE
def search_theatre():
import pickle
print('SEARCH FOR A THEATRE BY NAME')
global theatre
theatre=input('Enter the name of the theatre to be searched:').upper()
fin=open(r'C:\Users\asus\.idlerc\THEATRE.dat','rb')
flag=0
try:
while True:
s_theatre=pickle.load(fin)
if theatre==s_theatre[0]:
flag=1
print()
print()
print('.'*79,'THEATRE PRESENT','.'*79)
print('.'*79,'DISPLAYING THEATRE DETAILS','.'*79)

print()
print()
print('THEATRE NAME: ',s_theatre[0])
print('LOCATION: ',s_theatre[1])
print('SEATING CAPACITY: ',s_theatre[2])
print('PRICE OF A TICKET: ',s_theatre[3])
print('REFRESHMENTS AVAILABLE(price in bracket):',s_theatre[4])

except Exception:
if flag==0:
print('...............SORRY, THEATRE NOT PRESENT!!!...............')
fin.close()

#DELETING A THEATRE
def del_theatre():
import pickle
f=open(r'C:\Users\asus\.idlerc\THEATRE.dat','rb')
data=pickle.load(f)
f.close()
pc=input('Enter the name of the theatre to delete its details: ').upper()
f=open('THEATRE.dat','wb')

lst=[]
for record in data:
if record[0]==pc:
continue
lst.append(record)
pickle.dump(lst,f)
f.close()
print("Theatre Deleted")

#SEARCH MOVIES
def search_movies():
import pickle
print('SEARCH FOR A MOVIE NAME')
print()
print()
global movie_name
movie_name=input('Enter the name of the movie to be searched: ')
fin=open('MOVIE.dat','rb')
flag=0

try:
while True:
s_movie=pickle.load(fin)
if movie_name==s_movie[0]:
flag=1
print('...............MOVIE AVAILABLE...............')
print('...............DISPLAYING MOVIE DETAILS...............')
print('MOVIE NAME: ',s_movie[0])
print('MOVIE GENRE: ',s_movie[1])
print('MOVIE LANGUAGE: ',s_movie[2])
print('MOVIE DIRECTOR: ',s_movie[3])
print('MOVIE CAST: ',s_movie[4])
print('MOVIE SYNOPSIS: ',s_movie[5])
print('MOVIE RATING: ',s_movie[6])
print(' '*75,'REDIRECTING TO BOOKING PAGE',' '*75)
booking_module()
except Exception:
if flag==0:
print('...............SORRY, MOVIE NOT AVAILABLE!!!...............')
movie_module()

#DELETE MOVIES
def del_movies():
import pickle
f=open('MOVIE.dat','rb')
data=pickle.load(f)
f.close()
pc=input('Enter the name of the movie to delete its details: ')
f=open('MOVIE.dat','wb')
lst=[]
for record in data:
if record[0]==pc:
continue
lst.append(record)
pickle.dump(lst,f)
f.close()

#ROMCOM GENRE
def romcom_genre():
import pickle

m=[]
m_name='ROMCOM'
f=open('MOVIE.dat','rb')
try:
while True:
m=pickle.load(f)
for i in m:
if m[1]==m_name:
print('....................DISPLAYING ACCORDING TO YOUR CHOICE....................')

print(' MOVIE NAME: ',m[0])
print('MOVIE GENRE: ',m[1])
print('MOVIE LANGUAGE: ',m[2])
print('MOVIE DIRECTOR: ',m[3])
print('MOVIE CAST: ',m[4])
print('MOVIE SYNOPSIS: ',m[5])
print('MOVIE RATING: ',m[6])
print('.'*167)
break
except Exception:
f.close()
global movie_name
movie_name=input('Enter the movie name: ')

print('*'*167)
print()
print()
print('Your choices have been saved!')
print()
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()
booking_module()

#THRILLER GENRE
def thriller_genre():
import pickle
m=[]
m_name='THRILLER'
f=open('MOVIE.dat','rb')
try:
while True:
m=pickle.load(f)
for i in m:
if m_name==m[1]:

print('....................DISPLAYING ACCORDING TO YOUR CHOICE....................')

print(' MOVIE NAME: ',m[0])
print('MOVIE GENRE: ',m[1])
print('MOVIE LANGUAGE: ',m[2])
print('MOVIE DIRECTOR: ',m[3])
print('MOVIE CAST: ',m[4])
print('MOVIE SYNOPSIS: ',m[5])
print('MOVIE RATING: ',m[6])
print('.'*167)
break
except Exception:
f.close()
global movie_name
movie_name=input('Enter the movie name: ')
print('*'*167)
print()
print()
print('Your choices have been saved!')
print()
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()

booking_module()

#SCIFI GENRE
def scifi_genre():
import pickle
m=[]
m_name='SCI-FI'
f=open('MOVIE.dat','rb')
try:
while True:
m=pickle.load(f)
for i in m:
if m_name==m[1]:
print('....................DISPLAYING ACCORDING TO YOUR CHOICE....................')

print(' MOVIE NAME: ',m[0])
print('MOVIE GENRE: ',m[1])
print('MOVIE LANGUAGE: ',m[2])
print('MOVIE DIRECTOR: ',m[3])
print('MOVIE CAST: ',m[4])
print('MOVIE SYNOPSIS: ',m[5])

print('MOVIE RATING: ',m[6])
print('.'*167)
break
except Exception:
f.close()
global movie_name
movie_name=input('Enter the movie name: ')
print('*'*167)
print()
print()
print('Your choices have been saved!')
print()
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()
booking_module()

# MOVIES IN HINDI LANGUAGE
def hindi_lan():
import pickle

print()
print()
m=[]
pref_lan='HINDI'
print('MOVIES AVAILABLE IN HINDI LANGUAGE')
f=open('MOVIE.dat','rb')
try:
while True:
m=pickle.load(f)
for i in m:
if m[2]==pref_lan:
print(' MOVIE NAME: ',m[0])
print('MOVIE GENRE: ',m[1])
print('MOVIE LANGUAGE: ',m[2])
print('MOVIE DIRECTOR: ',m[3])
print('MOVIE CAST: ',m[4])
print('MOVIE SYNOPSIS: ',m[5])
print('MOVIE RATING: ',m[6])
print('.'*167)
break
except Exception:
f.close()
global movie_name

movie_name=input('Enter the movie name ')
print('*'*167)
print()
print()
print('Your choices have been saved!')
print()
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()
booking_module()

# MOVIES IN MALAYALAM LANGUAGE
def mal_lan():
import pickle
print()
print()
m=[]
pref_lan='MALAYALAM'
print('MOVIES AVAILABLE IN MALAYALAM LANGUAGE')

f=open('MOVIE.dat','rb')
try:
while True:
m=pickle.load(f)
for i in m:
if m[2]==pref_lan:
print(' MOVIE NAME: ',m[0])
print('MOVIE GENRE: ',m[1])
print('MOVIE LANGUAGE: ',m[2])
print('MOVIE DIRECTOR: ',m[3])
print('MOVIE CAST: ',m[4])
print('MOVIE SYNOPSIS: ',m[5])
print('MOVIE RATING: ',m[6])
print('.'*167)
break
except Exception:
f.close()
global movie_name
movie_name=input('Enter the movie name: ')
print('*'*167)
print()
print()
print('Your choices have been saved!')

print()
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()
booking_module()

# MOVIES IN ENGLISH LANGUAGE
def eng_lan():
import pickle
print()
print()
m=[]
pref_lan='ENGLISH'
print('MOVIES AVAILABLE IN ENGLISH LANGUAGE')
f=open('MOVIE.dat','rb')
try:
while True:
m=pickle.load(f)
for i in m:
if m[2]==pref_lan:

print(' MOVIE NAME: ',m[0])
print('MOVIE GENRE: ',m[1])
print('MOVIE LANGUAGE: ',m[2])
print('MOVIE DIRECTOR: ',m[3])
print('MOVIE CAST: ',m[4])
print('MOVIE SYNOPSIS: ',m[5])
print('MOVIE RATING: ',m[6])
print('.'*167)
break
except Exception:
f.close()
global movie_name
movie_name=input('Enter the movie name: ')
print('*'*167)
print()
print()
print('Your choices have been saved!')
print()
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()
booking_module()

#MOVIE MODULE
def movie_module():
print('*'*167)
print('''HOW WOULD LIKE TO VIEW THIS PAGE:
1. BY YOUR PREFERRED GENRE
2. BY YOUR PREFERRED LANGUAGE
3. SHOW ALL MOVIES
4. SEARCH MOVIE
(ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE)''')
ch=int(input('ENTER YOUR CHOICE: '))
if ch==1:
y=int(input('''ENTER YOUR PREFERRED GENRE:
1. ROMCOM
2. THRILLER
3. SCIFI
(ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE)'''))
if y==1:
m_name='ROMCOM'
print(m_name)
romcom_genre()

elif y==2:
m_name='THRILLER'
thriller_genre()
elif y==3:
m_name='SCI-FI'
scifi_genre()
else:
print('INVALID CHOICE!!!')
elif ch==2:
x=int(input('''ENTER YOUR PREFERRED LANGUAGE:
1. ENGLISH
2. MALAYALAM
3. HINDI
(ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE)'''))
if x==1:
pref_lan='ENGLISH'
eng_lan()
elif x==2:
pref_lan='MALAYALAM'
mal_lan()
elif x==3:
pref_lan='HINDI'

hindi_lan()
else:
print('INVALID CHOICE!!!')
elif ch==3:
read_movies()
elif ch==4:
search_movies()
else:
print('INVALID CHOICE!!!')

#USER MODULE
def users():
print()
print('_'*79+'LOGIN'+'_'*79)
name=input('Enter a Username: ')
print('The system generated password for your account is: {}'.format(passgenerator()))
emailid=input('Provide a valid Email id: ')
phoneno=input('Enter Phone Number: ')
print()
print('YOU HAVE SUCCESSFULLY CREATED A USER PROFILE!!!')

print('.'*80)
preflan=input('''Please enter your preferred language from the given choices:

(enter the number that corresponds to each choice)

1.MALAYALAM
2.ENGLISH
3.HINDI
''')
print()
print('YOUR CHOICE HAS BEEN SAVED.')
print()
prefgen=input('''Please enter your preferred genre from the given choices:

(enter the number that corresponds to each choice)

1.ACTION
2.SCI-FI
3.ROM-COM

''')
print()
print('YOUR PREFERENCES HAVE BEEN SAVED.')

titles={'NAME':name,'PASSWORD':passgenerator.passw,'EMAILID':em
ailid,'PHONENO':phoneno,'PREFERRED_LAN':preflan,'PREFERRED_
GENRE':prefgen}
pickle.dump(titles,user)
print('THANK YOU FOR HELPING US TO PROVIDE YOU WITH A BETTER EXPERIENCE.')
print('(redirecting...)')
movie_module()

#ADD MOVIES
def add_movies():
import pickle
outfile=open('MOVIE.dat','ab')
while True:
movie_name= input('Enter the name of the movie: ')
genre= input('Enter the genre of movie: ')
language=input('Enter the language of the movie: ')
director= input('Enter the name of the movie director: ')
cast= input('Enter the cast of the movie: ')

synopsis= input('Enter the synopsis of the movie: ')
rating= input('Enter the rating of the movie: ')

movie_details=[movie_name,genre,language,director,cast,synopsis,rat
ing]
pickle.dump(movie_details,outfile)
choice=input('Do you want to enter more record of movies(y/n): ')
if choice in 'nN':
break
outfile.close()

#READ MOVIES
def read_movies():
import pickle
f=open('MOVIE.dat','rb')
data=[]
print('*'*167)
print('Please select a movie of your choice from the following...................')
print()
print()

while True:
try:
data=pickle.load(f)
for i in data:
print (i)
print()
if data.index(i) in range(6,54,6):
print('*'*50)
else:
pass
except:
f.close()
break
global movie_name
movie_name=input("Enter the name of the movie you wish to book a ticket for:")
print('.............REDIRECTING YOU TO BOOKING MODULE...........')
print()
print()
booking_module()

#ADMIN MODULE

def admin():

while True:
print('Which module do you want to work on:')
print('''

1.MOVIES
2.THEATRES
3.EXIT''')

w=int(input('Enter the number of your choice(1/2/3): '))
if w==1:
print('1.Add movie and its details')
print('2.Read movie and its details')
print('3.Search movies')
print('4.Delete movie and its details')
print('5.EXIT')
ch=int(input('Enter the number of your choice(1/2/3/4): '))
if ch==1:
add_movies()
elif ch==2:
read_movies()
elif ch==3:
search_movies()
elif ch==4:
del_movies()
elif ch==5:
break
else:
print('INVALID CHOICE!!!')

elif w==2:
print('1.Add theatres ')
print('2.Display theatres')
print('3.Search theatre')
print('4.Delete theatre and its details')
print('5.EXIT')
ch=int(input('Enter the number of your choice(1/2/3/4): '))
if ch==1:
add_theatre()
elif ch==2:
read_theatre()
elif ch==3:
search_theatre()
elif ch==4:

del_theatre()
elif ch==5:
break
else:
print('INVALID CHOICE!!!')

elif w==3:
break
else:
print('INVALID CHOICE!!!')

#WELCOME PAGE
def welcomepage():
while True:
print("WELCOME TO STARK'S ONLINE MOVIE TICKET
BOOKING")
print('*'*80)
choice=int(input('''Please select a choice(1/2/3):
1.SIGN IN(NEW USER)
2.LOGIN(EXISTING USER)
3.ADMIN

'''))

if choice==1:
users()
elif choice==2:
print()
name1=input('ENTER YOUR USERNAME : ')
filein=open('userrec.bin','rb')
logincred=pickle.load(filein)
for each in logincred:
if logincred['NAME']==name1:
print('USERNAME IS VALID.')
password1=input('ENTER YOUR PASSWORD : ')
if logincred['PASSWORD']==password1:
print('PASSWORD IS CORRECT.')
print('SIGN IN SUCCESSFUL...')
print('(redirecting...)')
movie_module()
sys.exit()
else:
print('WRONG PASSWORD ENTERED!!!')
sys.exit()
else:
print("THE USERNAME DOESN'T EXIST!!!")

elif choice==3:
adminname='tonystark'
adminpass='robertjr'
print('ENTER LOGIN CREDENTIALS FOR ADMIN...')
print()
adminnameinput=input('NAME : ')
adminpassword=input('PASSWORD : ')
if adminnameinput==adminname and
adminpassword==adminpass:

#checks the admin credentials
admin()
else:
print(''' ACCESS REVOKED!!!
WRONG NAME/PASSWORD ENTERED''')

else:
print('WRONG CHOICE ENTERED!!!')

welcomepage()
user.close()
