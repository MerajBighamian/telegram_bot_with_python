#---- impoer module mysql.connector -----#
import mysql.connector
#----------- end -----------#


#---- impoer module random -----#
import random
#----------- end -----------#


# --- define connection with db ----#
connection = mysql.connector.connect(user='root',
                                        password='',host='127.0.0.1',
                                        database='bot')
#----------- end -----------#

#----- define a cursor of connection ------#
cursor = connection.cursor()
#----------- end -----------#

#----- define a cursor of connection ------#
def open_cursor():
    cursor = connection.cursor()
    onnection = mysql.connector.connect(user='root',
                                        password='',host='127.0.0.1',
                                        database='bot')
#----------- end -----------#

#----- define class db for work with database ------#
class db:
    def __init__(self, name, chat_id):
        self.name = name
        self.chat_id = chat_id
    random.seed()
    
    
    
    def insert_in_db(self):
        cursor.execute("INSERT INTO users VALUES(\'{}\',{},{},2);".format(self.name,self.chat_id,random.randint(1,10000000)))
        connection.commit()
        
    def read_from_db(self):
        cursor.execute('SELECT * FROM users WHRE {};'.format(self.chat_id))
        for (name_user,chat_id,id_,shop) in cursor:
            return('user name is {} and chat id is {} and id is {} and shop item is {}'.format(name_user,chat_id,id_,shop))
#----------- end -----------#


def curso_close():
    cursor.close()   
    connection.close()