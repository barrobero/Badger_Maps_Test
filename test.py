import csv 
from datetime import *

class Customer: 
	FirstName = ""
	LastName = ""
	Street = ""
	Zip = ""
	City = ""
	Type = ""
	LastCheckInDate = ""
	Job = ""
	Phone = ""
	Company = ""

	def __init__(self, fn, ln, s, z, c, t, lci, j, p, co): # encapsulation
		self.FirstName = fn
		self.LastName = ln 
		self.Street = s # required
		self.Zip = z 	#required
		self.City = c 	#required
		self.Type = t 	
		self.LastCheckInDate = lci # required 
		self.Job = j 
		self.Phone = p 
		self.Company = co # required

def load_list(list): # creates a list of Customer objects
	with open('sample_test.csv', 'r') as csv_reader:
		reader = csv.reader(csv_reader)
		headings = next(reader) # store the headers in a separate variable
		print("Loading csv file...")
		for row in reader:
			if not ''.join(row).strip(): # if a row is empty, continue with the loop
				print("Empty row...")
				continue

			if len(row[2])==0 or len(row[3])==0 or len(row[4])==0 or len(row[6])==0 or len(row[9])==0: # check if a required field is empty
				print('A required field is empty in the row: ')
				print(row)
				pass 
			customer_list.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])) # add to the list

customer_list = []
load_list(customer_list) # now we can manipulate the fields of the csv as objects of the class