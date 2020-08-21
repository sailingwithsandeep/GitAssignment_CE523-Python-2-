import sqlite3
class myconnect:
      
      def __init__(self):
            conn = sqlite3.connect('employee.sqlite')
            conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE_DETAILS(emp_id INTEGER PRIMARY KEY  autoincrement,NAME TEXT,
         EMAIL            TEXT,
         MOBILE        INT,
         EMP_TYPE             TEXT,
         EXPERIANCE   INT,
         SALARY         INT);''')
                  
      def savetodb(self,name,email,mobile,emp_type,experience,salary):
            conn = sqlite3.connect('employee.sqlite')
            cursor = conn.cursor()

            query = '''
            INSERT INTO EMPLOYEE_DETAILS values(NULL,?,?,?,?,?,?)
            '''

            cursor.execute(query,(name,email,mobile,emp_type,experience,salary))

            conn.commit()
            conn.close()


      def display(self,id):
            conn = sqlite3.connect('employee.sqlite')

            cursor = conn.cursor()

            query = ''' SELECT *
            FROM EMPLOYEE_DETAILS
            WHERE emp_id = {}'''.format(id)

            cursor.execute(query)
            all_rows = cursor.fetchall()
           
            conn.commit()            
            conn.close()
            return all_rows
      
      def display_data(self):
            id = int(input('Enter the employee id: '))
            data = self.display(id)
            if not data:
                  print("No data found at employee ID: ",id)
            else:
                  for rows in data:
                        print('==============================================')
                        print('Name: ',rows[1])
                        print('Email: ',rows[2])
                        print('Mobile No: ',rows[3])
                        print('Employee Type: ',rows[4])
                        print('Experience: ',rows[5])
                        print('Salary: ',rows[6])
                        print('==============================================')
      
