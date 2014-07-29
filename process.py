import xlrd
import csv

def txtencode(string):
    #if type(string) in (unicode, str):
    string = str(string).replace(u'\xa0', ' ')
    return string.encode('utf-8')
    #else:
        #return string

wb = xlrd.open_workbook('CombinedNamed.xlsx', encoding_override="latin-1")
sh = wb.sheet_by_name('Sheet1')
your_csv_file = open('Sheet1.csv', 'wb')
wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

for rownum in xrange(sh.nrows):
    print rownum
    row = sh.row_values(rownum)
    new_row = []
    for val in row:
        new_row.append(txtencode(val))
    wr.writerow(new_row)

your_csv_file.close()


