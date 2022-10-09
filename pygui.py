import pyautogui
import random
import string
import time
import secrets

from time import sleep
from random import randint




#subtl
url1 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTczNjE4Nw&rm=en_in']
#adder
url2 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcyOTM5Mw&rm=en_in']
#subtl
url3 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcxMTIyMw&rm=en_in']
url4 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcyOTc3NQ&rm=en_in']
url5 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcxMTM4OQ&rm=en_in']
url6 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTczNjcyNg&rm=en_in']
url7 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcyODk4Mg&rm=en_in']
url8 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcyOTEwNg&rm=en_in']
url9 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTczNjAxNg&rm=en_in']
url10 = ['https://www2.hm.com/en_in/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzE1NTcyOTE1MA&rm=en_in']


urls = ['https://www2.hm.com/en_in/women/shop-by-product/accessories.html','https://www2.hm.com/en_in/home/shop-by-product/decorations.html']


#randomized character functions
N5 = 8
N7 = 1
N6 = 3
N = 16
res = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.ascii_letters)
              for i in range(N))

res1 = ''.join(secrets.choice(string.digits)
               for i in range(N5))


res2 = ''.join(secrets.choice(string.digits)
               for i in range(N6))

res5 = ''.join(secrets.choice(string.digits)
               for i in range(N7))

#samples
diss = ['01', '02', '03', '04', '05','06','07','08', '09', '10', '11', '12', '13', '14', '15', '16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
doyz = (random.sample(diss, k=1))

noss = ['01', '02', '03', '04', '05','06','07','08', '09', '10', '11', '12']
monts = (random.sample(noss, k=1))

yees =  ['1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003']

yoiz = (random.sample(yees, k=1))



firstnames = ['Rudra', 'Ishaan', 'Shivay', 'Rudra','Ishaan', 'Shivay', 'Rudransh', 'Shivansh','Krish', 'Kanha', 'Mohammed', 'Ali', 'Ramunghor', 'Aliya', 'Ishika', 'Mahek', 'Jhilmil', 'Tumei', 'Tomol', 'Gaurav', 'Kunal','Preetum','Piyush', 'Arnav', 'Sujal']

lastnames  = ['Singh', 'Bordoloi', 'agrawal', 'Jain', 'Kalita', 'Kumar', 'Bharta', 'Sethi', 'Gupta', 'Bhagat','Swami', 'Yuvraj', 'Sri', 'Rishi', 'Rao','Das']

postals = ['208002', '202001', '230501', '231225', '231302', '233221', '250001', '273155', '231225', '211002']

homelocation = ['opp. Guarav panshop', 'saroji road, ken apartment', 'Opp. KK Hotel', 'Jc resort']



#1
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url1)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#2
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url2)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("2@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#3
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url3)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("3@gmail.com"))
print(str(res)+("3@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)




#loop over
pyautogui.leftClick(136, 50)
time.sleep(2)
pyautogui.leftClick(116, 120)
time.sleep(1)
pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#4
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url4)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("4@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#5
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url5)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("5@gmail.com"))
print(str(res)+("5@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)



#loop over
pyautogui.leftClick(136, 50)
time.sleep(2)
pyautogui.leftClick(116, 120)
time.sleep(1)
pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#6
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url6)))
pyautogui.hotkey('ENTER')

pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("6@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#7
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url7)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("7@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)


#8
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url8)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(4,5))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("8@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)



#loop over
pyautogui.leftClick(136, 50)
time.sleep(2)
pyautogui.leftClick(116, 120)
time.sleep(1)
pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#9
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url9)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(3,4))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("9@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)

#10
sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(1)
pyautogui.leftClick(460,180)

time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url10)))
pyautogui.hotkey('ENTER')
pyautogui.leftClick(460,180)
sleep(randint(3,4))
pyautogui.click(500,470)
time.sleep(1)
pyautogui.typewrite (str(res)+("10@gmail.com"))
print(str(res)+("@gmail.com"))
time.sleep(1)
pyautogui.leftClick(500,550)
time.sleep(0.5)
pyautogui.typewrite(str(res)+(res2))
time.sleep(1)
pyautogui.leftClick(500,680)

pyautogui.write(random.choice(diss))

pyautogui.leftClick(700,680)

pyautogui.write(random.choice(noss))

pyautogui.leftClick(900,680)


pyautogui.typewrite(random.choice(yees))
time.sleep(1)
pyautogui.leftClick(1360,500)
sleep(randint(1,2))
pyautogui.leftClick(660,440)
sleep(randint(4,5))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite(random.choice(urls))
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(4)
#cloth selection
pyautogui.leftClick(400,700)
pyautogui.leftClick(400,730)
pyautogui.leftClick(400,760)
pyautogui.leftClick(400,770)


time.sleep(3)
pyautogui.leftClick(1360,240)
sleep(randint(1,2))

pyautogui.leftClick(1200,655)
pyautogui.leftClick(1200,625)
pyautogui.leftClick(1200,605)
pyautogui.leftClick(1200,585)
pyautogui.leftClick(1200,565)
pyautogui.leftClick(1200,545)
pyautogui.leftClick(1200,525)
pyautogui.leftClick(1200,505)
pyautogui.leftClick(1200,485)
pyautogui.leftClick(1200,465)
pyautogui.leftClick(1200,445)
time.sleep(1)
pyautogui.leftClick(1360,90)

sleep(randint(1,2))

#add cart
#go cart
pyautogui.leftClick(1270,120)
sleep(randint(5,6))
pyautogui.leftClick(1360,720)
time.sleep(2)
pyautogui.leftClick(1060,280)
pyautogui.leftClick(1060,260)
pyautogui.leftClick(1060,240)
pyautogui.leftClick(1060,300)
pyautogui.leftClick(1060,340)

sleep(randint(9,12))

#fill up billing info
#firstname
pyautogui.leftClick(350,480)
time.sleep(1)
pyautogui.write(random.choice(firstnames))

#lastname
pyautogui.leftClick(520,480)
pyautogui.write(random.choice(lastnames))
time.sleep(1)
pyautogui.leftClick(300,610)
pyautogui.typewrite(random.choice(homelocation))

time.sleep(1)
pyautogui.leftClick(300,720)
pyautogui.write(random.choice(postals))
time.sleep(1)
pyautogui.leftClick(1360,650)
time.sleep(1)
pyautogui.leftClick(130,388)
time.sleep(1)
pyautogui.leftClick(660,545)
time.sleep(1)
pyautogui.write ("90"+(str(res1)))
time.sleep(1)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(1)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(1)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(3)
pyautogui.leftClick(136,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(4)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(2)
pyautogui.leftClick(878,215)
time.sleep(1)



#loop over
pyautogui.leftClick(136, 50)
time.sleep(2)
pyautogui.leftClick(116, 120)
time.sleep(1)

pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)
time.sleep(1)
pyautogui.leftClick(296, 18)
