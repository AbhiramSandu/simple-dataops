import mysql.connector
import sys

arguements = sys.argv

mydb = mysql.connector.connect(
  host=arguements[1],
  user=arguements[2],
  passwd=arguements[3]
)

cursor = mydb.cursor()

statement = ""

isSuccess = true
if isSuccess:
  else:
    mydb.rollback()l_file = arguements[4]

for line in open(sql_file, 'r'):
    if re.match(r'--', line):  # ignore sql comment lines
        continue
    if not re.search(r'[^-;]+;', line):  # keep appending lines that don't end in ';'
        statement = statement + line
    else:  # when you get a line ending in ';' then exec statement and reset for next statement
        statement = statement + line
        #print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
        try:
            cursor.execute(statement)
        except (OperationalError, ProgrammingError) as e:
            isSuccess = false
            break
        statement = ""
        
if isSuccess:
  mydb.commit()
  print("Success")
else:
  mydb.rollback()
  print("Failed")