from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import urllib.request as urllib2
import wget
import sys

analysis_period = input("Enter number of days to scrape:")
race_code = input('Race Code to scarpe Dogs or Horses:')
win_type = input('Enter Win or Place data to scrape:')

if race_code == 'Horses':
    country = input('Enter Country Code (Aus, Ire, Uk, USA, RSA): ')

if win_type not in ("Win","Place"):
    print("Win Type Unavailable")
    sys.exit()

search_win = win_type.lower()

if race_code == "Horses" and country not in ("Aus","Ire","Uk","USA","RSA"):
    print("Data for Country Code entered unavailable")
    sys.exit()
    
if race_code == "Dogs":
    search = "greyhound"+search_win
elif (race_code == "Horses"):
    search = country.lower()+search_win
else:
    print("Incorrect Race Code entered")
    sys.exit()



lastrun = datetime.now() - timedelta(int(analysis_period))
f_lastrun = datetime.strftime(lastrun,'%d%m%Y')
#print(f_lastrun)
link_p1 = "https://promo.betfair.com"

html_page = urllib2.urlopen("https://promo.betfair.com/betfairsp/prices")
soup = BeautifulSoup(html_page,"html.parser")


for link in soup.findAll('a'):
    if search in link.get("href") and f_lastrun in link.get("href"):
        wget.download(link_p1+link.get('href'),r'C:\Users\srira\OneDrive\Documents\Betfair\Greyhounds\Place_Data_2022')
    





