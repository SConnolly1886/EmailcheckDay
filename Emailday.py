"""
Program that categorizes each mail message
by which day of the week the commit was done.
Look for lines that start with "From", then look for the third word
and keep a running count of each of the days of the week.
Prints out the contents of your dictionary
(order does not matter).

"""
fname = input('Enter file name: ')
if len(fname) < 1 :
    fhandle = open('mbox-short.txt')
else:
    try:
        fhandle = open(fname)
    except:
        print('Invalid file')
        quit()

daycount = dict()

for lines in fhandle :
    lines = lines.rstrip()
    words = lines.split()
    if len(words) < 3 : continue
    if words[0] != 'From' : continue
    day = words[2]
    print(day)
    if day not in daycount :
        daycount[day] = 1
    else:
        daycount[day] += 1
print(daycount)
