import requests
from bs4 import BeautifulSoup
import smtplib

response=requests.get("https://codeforces.com/contests")
soup=BeautifulSoup(response.text,'lxml')
table=soup.find("table",{"class":""})
tds=table.find_all("td")
tdlist=[]
for td in tds:
	tdlist.append(td.text.lstrip())
name1=[]
date1=[]
length1=[]
dl1=[]
dlr1=[]
i=0
j=1
k=2
l=3
m=4
while(i<len(tdlist)):
	name1.append(tdlist[i])
	date1.append(tdlist[j])
	length1.append(tdlist[k])
	dl1.append(tdlist[l])
	dlr1.append(tdlist[m])
	i=i+6
	j=j+6
	k=k+6
	l=l+6
	m=m+6
response=requests.get("https://www.codechef.com/contests")
soup=BeautifulSoup(response.text,'lxml')
mytable=soup.find("table",{"class":"dataTable"})
tds=mytable.find_all("td")
tdlist2=[]
for td in tds:
	tdlist2.append(td.text)
i=0
j=1
k=2
l=3
code=[]
name2=[]
date2=[]
end=[]
while(i<len(tdlist2)):
	code.append(tdlist2[i])
	name2.append(tdlist2[j])
	date2.append(tdlist2[k])
	end.append(tdlist2[l])
	i=i+4
	j=j+4
	k=k+4
	l=l+4
message='ATTENTION \n'+'CODEFORCES :\n'
for i in range(len(name1)):
	message=message+name1[i]+' '+date1[i]+' '+length1[i]+' '+dl1[i]+' '+dlr1[i]+'\n'
message=message+'\n'+'CODECHEF :\n'
for i in range(len(code)):
	message=message+code[i]+' '+name2[i]+' '+date2[i]+' '+end[i]+'\n'
message=message+"END OF THE MESSAGE\n"
message=message+'THIS MESSAGE WILL SELF DESTRUCT IN 5 MINUTES\n'
try:
	conn=smtplib.SMTP('smtp.gmail.com',587)
	conn.ehlo()
	conn.starttls()
	conn.login(mailid of notification bot,its password)
	conn.sendmail(mailid of notification bot,mailid of user,Message to be sent)
	conn.quit()
	print('Mail sent')
except:
	print('Some error')