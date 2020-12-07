from bs4 import BeautifulSoup as sp
import requests as req
from datetime import datetime as time
import pandas as pd
import matplotlib.pyplot as plt


class stock:
	
	def __init__(self, ticker):
		self.ticker = ticker
		self.url ="https://finance.yahoo.com/quote/"+ticker+"/history?p="+ticker
		self.r = req.get(self.url)
		self.s = sp(self.r.text, "html.parser")
		self.tables = self.s.find_all("tr",{"class" : "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"})
		self.df = pd.DataFrame(columns = ["Date", "Price"] )
	
	
	#Obtain stockprice from Yahoo Finance:
	def stockPrice(self):
		url = "https://finance.yahoo.com/quote/"+self.ticker+"/"
		r = req.get(url) 
		s = sp(r.text, "html.parser")
		price = s.find_all("div", {"class" : "D(ib) Va(m) Maw(65%) Ov(h)"})[0].find("span").text
		print(self.ticker.upper() + " " +  price)

	#Use for continues price monitoring:
	def continuePrice(self):
		url = "https://finance.yahoo.com/quote/"+self.ticker+"/" 
		r = req.get(url)
		s = sp(r.text, "html.parser") 
		price = float(s.find_all("div", {"class" : "D(ib) Va(m) Maw(65%) Ov(h)"})[0].find("span").text.replace(',','')) 
		return price
	
	#Obatin RSI value of stock 14days: 
	def getRSIValue(self):
		posAvg = 0
		negAvg = 0

		for x in range(10):
			if (len(self.tables[x].find_all("td")) == 2 or len(self.tables[x+1].find_all("td")) == 2):
				continue

			else:
				closedPrice = float(self.tables[x].find_all("td")[4].find("span").text.replace(',', ''))
				prevClosedPrice = float(self.tables[x+1].find_all("td")[4].find("span").text.replace(',', ''))
				date= self.tables[x].find_all("td")[0].find("span").text
        
				if(closedPrice > prevClosedPrice):
					posAvg +=  closedPrice - prevClosedPrice
				elif( closedPrice < prevClosedPrice):
					negAvg += prevClosedPrice - closedPrice

		print(self.df)
		self.rsiCalculator(posAvg,negAvg)
      
    
	#Graph the stock price    
	def getGraph(self,y):
		for x in range(y):
			if(len(self.tables[x].find_all("td")) == 2 or len(self.tables[x+1].find_all("td")) == 2):
				continue
			else:
				date = self.tables[x].find("td").find("span").text
				closedPrice = float(self.tables[x].find_all("td")[4].find("span").text.replace(',', ''))
				self.df.loc[x,"Date"] = date 
				self.df.loc[x,"Price"] =closedPrice

		self.sort()
		plt.xticks([0,20,40,60,75,89])
		plt.plot(self.df.Date, self.df.Price)
		plt.show()

	#Calculate RSI
	def rsiCalculator(self, posAvg, negAvg):
		gain= posAvg/14                                                                                                 
		loss = negAvg/14                                                                                                 
		rs = gain/loss                                                                                                 
		rsiValue = 100 - (100/(1+(rs)))  
		round(rsiValue, 2)
		print("RSI Value: " + str(round(rsiValue, 2)) + "\n" )



	def sort(self):
		self.df = self.df.reindex(index=self.df.index[::-1])


