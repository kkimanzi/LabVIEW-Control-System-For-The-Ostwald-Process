import random
import time

def random_number(max, min):
	return round((random.random() * (max - min) + min), 4);

while (True):
	line1 = "<!doctype html>"
	line2 = "<html>"
	line3 = "<head>"
	line4 = "<title>Raw Materials Global Prices</title>"
	line5 = "</head>"
	line6 = "<body>"
	line7 = "<h1>Prices of Raw Materials </h1>"
	line8 = "<ul>"

	linei = "Liquid Nitrogen - " + str(random_number(1.8,2.4)) + " $\n"
	lineii = "Liquid Oxygen - " + str(random_number(4.2,5.7)) + " $\n"
	lineiii = "Liquid Ammonia - " + str(random_number(12.11, 14.01)) + " $\n"
	lineiv = "Liquid Hydrogen - " + str(random_number(6.2,7.4)) + " $\n"

	line9 = "<li>"+linei+"/L</li>"
	line10 = "<li>"+lineii+"/L</li>"
	line11 = "<li>"+lineiii+"/L</li>"
	line12 = "<li>"+lineiv+ "/L<li>"

	line13 = "</ul>"
	line14 = "</body>"
	line15 = "</html>"

	with open('price_list.html', 'w') as out:
		out.writelines([line1, line2, line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15])

	time.sleep(10)