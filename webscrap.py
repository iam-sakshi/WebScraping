import requests
from bs4 import BeautifulSoup as b
info=input("Enter the name of the user you want to extract information")
user="https://www.github.com/"+info
r= requests.get(user)
soup= b(r.content,'html.parser')
profile_img = soup.find('img', {'alt' : 'Avatar'} )['src']
name=soup.find('span',{'class':"p-name vcard-fullname d-block overflow-hidden"}) 
repo= soup.find('span',{'class': 'Counter'})
about= soup.find('div',{"class":"p-note user-profile-bio mb-3 js-user-profile-bio f4"})
print("\n\n***********************************************************************")
print("Name of this Github user:",name.text)
print("Profile picture link:", profile_img)
print("About :" , about.text)
print("Number of Repositoy :", repo.text)
print("\n\n***********************************************************************")
