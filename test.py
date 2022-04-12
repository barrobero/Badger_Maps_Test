import csv 
from datetime import *

customer_list = []

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

def print_date():
	date1 = customer_list[0].LastCheckInDate # store the first date
	d, m, y = date1.split("/")
	min_date = date(int(y), int(m), int(d)) # date in format "datetime"
	max_date = min_date
	pos1 = pos2 = 0 # index for saving the customer's position

	for i in range(1, len(customer_list)):
		if(customer_list[i].LastCheckInDate == ""):
			continue
		date2 = customer_list[i].LastCheckInDate
		d2, m2, y2 = date2.split("/")
		date3 = date(int(y2), int(m2), int(d2)) # casting for int
		if date3 < min_date:
			min_date = date3
			pos1 = i
		if date3 > max_date:
			max_date = date3
			pos2 = i

	print("The customer with the oldest Last Check-in Date is: ", customer_list[pos1].FirstName, customer_list[pos1].LastName)
	print("The customer with the newest Last Check-in Date is: ", customer_list[pos2].FirstName, customer_list[pos2].LastName)



load_list(customer_list) # now we can manipulate the fields of the csv as objects of the class
print("\n..................................................................\n")
print_date()
