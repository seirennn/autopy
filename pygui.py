import pyautogui
import random
import string
import time
import secrets

from time import sleep
from random import randint




url = ['https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2MDQ2Mg&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2ODQyMQ&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2MDQyNQ&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU1OTQzMg&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU1OTQwOQ&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2MDM3NA&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2MDU2NA&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU1OTU5OQ&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2MDQ1OQ&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2ODQwNg&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2Njc2Ng&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2NjYwMQ&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2NjM5Ng&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2NjMyMA&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2NjI1NA&rm=en_in','https://www.hm.com/register?utm_source=invite_a_friend&utm_medium=desktop&rcr=MzEyMTU2NjExMg&rm=en_in']








#randomized character functions
N5 = 8
N7 = 1
N6 = 3
N = 14
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


urls = ['https://www2.hm.com/en_in/women/new-arrivals/view-all.html']

firstnames = ['Rudra', 'Ishaan', 'Shivay', 'Rudra','Ishaan', 'Shivay', 'Rudransh', 'Shivansh','Krish', 'Kanha', 'Mohammed', 'Ali', 'Ramunghor', 'Aliya', 'Ishika', 'Mahek', 'Jhilmil', 'Tumei', 'Tomol', 'Gaurav', 'Kunal','Preetum','Piyush', 'Arnav', 'Sujal']

lastnames  = ['Singh', 'Bordoloi', 'agrawal', 'Jain', 'Kalita', 'Kumar', 'Bharta', 'Sethi', 'Gupta', 'Bhagat','Swami', 'Yuvraj', 'Sri', 'Rishi', 'Rao','Das']

postals = ['208002', '202001', '230501', '231225', '231302', '233221', '250001', '273155', '231225', '211002']

homelocation = ['opp. Guarav panshop', 'saroji road, ken apartment', 'Opp. KK Hotel', 'Jc resort']




sleep(randint(2,3))
pyautogui.leftClick(95, 10)
time.sleep(2)
pyautogui.leftClick(300,50)
time.sleep(1)

#url
pyautogui.write(str(random.choice(url)))
time.sleep(1)
pyautogui.hotkey('ENTER')
sleep(randint(5,6))
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
sleep(randint(6,7))
pyautogui.leftClick(300,50)
sleep(randint(4,5))
pyautogui.typewrite('https://www2.hm.com/en_in/women/new-arrivals/view-all.html')
time.sleep(2)
pyautogui.hotkey('ENTER')
time.sleep(5)
#cloth selection
pyautogui.leftClick(400,700)



time.sleep(5)
pyautogui.leftClick(1200,600)
sleep(randint(2,3))

pyautogui.leftClick(1200,655)
sleep(randint(2,4))
#add cart
pyautogui.leftClick(1200,669)
time.sleep(3)
#go cart




pyautogui.moveTo(1270,120)
time.sleep(4)
pyautogui.leftClick(1240,490)
pyautogui.leftClick(1240,492)
pyautogui.leftClick(1240,488)
pyautogui.leftClick(1240,494)
pyautogui.leftClick(1240,496)


sleep(randint(10,15))

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
time.sleep(2)

pyautogui.leftClick(270,660)
pyautogui.leftClick(270,800)
time.sleep(3)
pyautogui.leftClick(509,426)
time.sleep(1)
pyautogui.leftClick(805,594)
pyautogui.leftClick(805,585)
pyautogui.leftClick(805,612)
time.sleep(3)
pyautogui.leftClick(509,426)


pyautogui.hotkey('ENTER')
time.sleep(2)
pyautogui.leftClick(242,540)
time.sleep(6)
pyautogui.leftClick(153,347)
time.sleep(2)
pyautogui.leftClick(270,690)
time.sleep(6)
pyautogui.leftClick(1360,90)
time.sleep(1)

pyautogui.leftClick(1360,90)

time.sleep(1)
pyautogui.moveTo(1030,120)
time.sleep(4)
pyautogui.leftClick(878,225)
time.sleep(1)
pyautogui.leftClick(300,50)
time.sleep(1)
pyautogui.write ('https://www2.hm.com/en_in/women/new-arrivals/view-all.html')
pyautogui.hotkey('ENTER')
time.sleep(4)
pyautogui.moveTo(1030,120)
time.sleep(4)
pyautogui.leftClick(878,225)