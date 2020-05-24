import csv
import os

# Меню где надо выбрать файл 
def menu():
	count = len(os.listdir())
	menu = ""
	for i in os.listdir() and range(count):
		menu += os.listdir()[i]
		menu += "\n"
	menu = menu.split()
	for i in range(count):
		print("[",i,"]",menu[i])
	try:
		num_csv = int(input("num file:"))
	except:
		print("Вы должны ввести число")

	file = os.listdir()[num_csv]
	return file

# Парсинг 

def main(file):
	csvfile = open(file,encoding='utf-8')
	readCSV = csv.reader(csvfile, delimiter=',')


	row_count = sum(1 for row in readCSV)

	csvfile = open(file,encoding='utf-8')
	readCSV = csv.reader(csvfile, delimiter=',')

	for i in range(row_count):
		for row in readCSV:
			print(row[0])
			break
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:1][0])
			break
		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[1])
			break
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:2][1])
			break
		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[2])
			break
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:3][2])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[3])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:4][3])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[4])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:5][4])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[5])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:6][5])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[6])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:7][6])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[7])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:8][7])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[8])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:9][8])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print(row[9])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:10][9])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[10])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:11][10])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[11])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:12][11])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[12])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:13][12])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[13])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:14][13])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[14])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:15][14])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[15])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:16][15])
			break

		csvfile = open(file,encoding='utf-8')
		readCSV = csv.reader(csvfile, delimiter=',')
		
		for row in readCSV:
			print(row[16])
			break

		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			print("\t",row[:17][16])
			break

		print("#"*50)

if __name__ == '__main__':
		main(menu())