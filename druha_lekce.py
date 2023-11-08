file = open("leapyears.txt", "r") # stary file
new_file = open("roky.csv", "w") # novy file
header = "Year;Leap_year\n"

for i in file:
    year = i.replace('\n', '')
    if year == 'Year':
        new_file.write(header)
    else:
        year = int(year)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            result = "Yes"
        else:
            result = "No"
        new_file.write(f'{year};{result}\n')

file.close()
new_file.close()
    