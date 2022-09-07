#webscraping iphone12 details from flipkart
import requests as r
from bs4 import BeautifulSoup as bs

def iphone12(gb):
    if gb==64:
        URLreliance64="https://www.reliancedigital.in/apple-iphone-12-64-gb-black/p/491901528"
        pagereliance64 = r.get(URLreliance64)
        soupreliance64 = bs(pagereliance64.content, "html.parser")
        pricereliance64=soupreliance64.find("span",{"class":"pdp__offerPrice"}).get_text()
        s_reliance64=""
        for i in pricereliance64:
            if i.isdigit() or i==".":
                s_reliance64+=i
        Pricereliance64=float(s_reliance64)
        
item=input("enter the item")
if item=="iphone":
    product=input("enter the prodcut u want(if phone specify gb as well):-")
    if product in["iphone 64","IPHONE 64","Iphone 64","iphone64","IPHONE64","Iphone64","iphone 128","IPHONE 128","Iphone 128","iphone128","IPHONE128","Iphone128"]:
        s=""
        gb=0
        for i in product:
            if i.isdigit():
                s+=i
                gb=float(s)
        iphone12(gb)
     
