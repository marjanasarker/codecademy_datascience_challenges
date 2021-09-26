import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cacao_site = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
#print(type(cacao_site))
soup = BeautifulSoup(cacao_site.content, "html.parser")
#print(type(soup))
ratings_tag = soup.select(".Rating")
ratings_strings = []
for rating in ratings_tag:
  #if rating!=rating.isalpha():
  ratings_strings.append(rating.get_text())
for rating in ratings_strings:
  if rating.isalpha():
    ratings_strings.remove(rating)
ratings = [float(rating) for rating in ratings_strings ] 
#print(ratings)

plt.hist(ratings)
plt.show()

#cacao_panda=pd.read_html(cacao_site)
company_tags = soup.select(".Company")
#company_list_strings=[]
company_list=[]
for company in company_tags:
  company_list.append(company.get_text())
# for company in company_list:
#   if company=="Company":
#     company_list.remove(company)
company_list.pop(0)
#print(company_list)
# making a dataframe from 2 lists using a dictionary
company_rating = {"Company": company_list, "Ratings": ratings}
company_ratingDF=pd.DataFrame.from_dict(company_rating)

mean_ratings = company_ratingDF.groupby("Company").Ratings.mean()
ten_best = mean_ratings.nlargest(10)
#print(ten_best)

# selecting tag which holds cocoa percent
cocoa_percent_tag = soup.select(".CocoaPercent")
#print(cocoa_percent_tag)
cocoa_percent = []
for cocoa_percent_alone in cocoa_percent_tag:
  
    only_text_cocoa = cocoa_percent_alone.get_text()
    # check if first item is a number, this is to avoid evaluating the header of this column
    if only_text_cocoa[0].isdigit():
      cocoa_wo_percent = only_text_cocoa[:-1]
      cocoa_percent.append(float(cocoa_wo_percent))
    
#print(cocoa_percent)
#use DF to add cocoa percentage, not the dictionary
company_ratingDF["CocoaPercentage"] = cocoa_percent
#company_ratingDF.head()

plt.clf()
plt.scatter(company_ratingDF.CocoaPercentage, company_ratingDF.Ratings)
#to look at correlation
z = np.polyfit(company_ratingDF.CocoaPercentage, company_ratingDF.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(company_ratingDF.CocoaPercentage, line_function(company_ratingDF.CocoaPercentage), "r--")

plt.show()
