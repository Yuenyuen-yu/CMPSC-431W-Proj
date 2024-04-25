#import psycopg2 for connection to postgre database
import psycopg2

#We are going to implement three functions first
#define function for interacting with the local database, this function executes SQL provided by user onto the database. 
def connection():       
      try:
            conn = psycopg2.connect(host= "localhost", dbname= "postgres", user= "postgres"
                        , password= "123456", port=5432)

            cur = conn.cursor()

            cur.execute(option_modified_sql_input)

            conn.commit()

            cur.close()
            conn.close()
      except psycopg2.Error as e:
            print(f"Database error: {e}")

#To begin the CLI user interface, populate the CLI page using basic print statements
#Also make this a function so the interface can be shown multiple times making possible to support multiple action user takes.
def interface():
      print("""
CMPSC 431W Project CLI interface
Student name: Yuenyuen Yu 

Please select one of the following options:
      1. Insert Data
      2. Delete Data
      3. Update Data
      4. Search Data
      5. Aggregate Functions
      6. Sorting
      7. Joins
      8. Grouping
      9. Subqueries
      10. Transactions
      11. Error Handling
      12. Exit
      """)

#This is a helper function used to display the database schema to user to help users with creating their queries.
def schema_display():
      print("""
This is the schema of the database:
Format: [TableName: column1, column2, ...]
            
Laptop: laptop_id, name, product_ean, product_sku, price_id, 
date_id, cpu_id, ram_id, gpu_id, storage_id, battery_id, 
bluetooth_id, size_id, weight_id, display_id, audio_id, keyboard_id
Price: price_id, price_eur
Date: date_id, release_year
CPU: cpu_id, cpu_processor
RAM: ram_id, ram_memory
GPU: gpu_id, gpu_integrated, gpu_extra
Storage: storage_id, internal_storage_gb, storage_type
Battery: battery_id, battery_life_h, battery_capacity_wh, psu_watts
Bluetooth: bluetooth_id, has_bluetooth, bluetooth_version
Size: size_id, height_mm, weight_mm, depth_mm
Weight: weight_id, weight_kg
Display: display_id, display_inch, display_cm, display_resolution, 
display_ratio
Audio: audio_id, audio_system, speakers_count
Keyboard: keyboard_id, keyboard_backlit, keyboard_numpad, 
has_touchscreen
      """)

#Body of the program starts here
#Call the interface
interface()

#Take choice input from user
user_choice = input("Enter your choice here (1-12):")

#Use if statemements to jump to different scenarios
#Insert data
if (user_choice == "1"):
      
      #print schema page to help users with input
      print("<You are now inserting into the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table = input("Input the table name you want to insert: ")
      user_input_columns = input("Input the columns you want to insert[eg. \"column1, column2, column3, ...\"]: ")
      user_input_values = input("Input the values you want in previous columns sequentially[eg. \"value1,value2,value3, ...\"]: ")
      option_modified_sql_input = ("INSERT INTO {} ({}) VALUES ({});").format(user_input_table, user_input_columns, user_input_values)
      print(option_modified_sql_input)

#Connect to database
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")

#Second case: delete data
elif (user_choice == "2"):
      
      #print schema page to help users with input
      print("<You are now deleting data from the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table = input("Input the table name you want to delete from: ")
      user_input_condition = input("Input the condition for deleting row[eg. column1 > 50, column1 = 10 AND column2 = 20, ...]: ")
      option_modified_sql_input = ("DELETE FROM {} WHERE {};").format(user_input_table, user_input_condition)
      print(option_modified_sql_input)

#Connect to database
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")

#Third case: update data
elif (user_choice == "3"):
      
      #print schema page to help users with input
      print("<You are now updating data in the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table = input("Input the table name you want to update data in: ")
      user_input_update = input("Input the updates you want to make[eg. column1 = 50, column2 = \"dog\"]: ")
      user_input_condition = input("Input the condition for updating rows[eg. column1 > 50, column1 = 10 AND column2 = 20, ...]: ")
      option_modified_sql_input = ("UPDATE {} SET {} WHERE {};").format(user_input_table, user_input_update, user_input_condition)
      print(option_modified_sql_input)

#Connect to database
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")

#Case four: search data
elif (user_choice == "4"):
      
      #print schema page to help users with input
      print("<You are now searching data in the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table = input("Choose the table to search from: ")
      user_input_condition = input("Input the condition of wanted rows[eg. column1 > 50, column1 = 10 AND column2 = 20, ...]: ")
      option_modified_sql_input = ("SELECT * FROM {} WHERE {};").format(user_input_table, user_input_condition)
      print(option_modified_sql_input)

#Connect to database
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")

#Case five: aggregating data
elif (user_choice == "5"):
      
      #print schema page to help users with input
      print("<You are now aggregating data in the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table = input("Choose the table to perform aggregation: ")
      user_input_aggregation = input("Choose one of the aggregation function to perform[SUM, AVG, COUNT, MAX, MIN]: ")
      user_input_column = input("Input the column you want to perform the aggregation function on: ")
      option_modified_sql_input = ("SELECT {}({}) WHERE {};").format(user_input_aggregation, user_input_column, user_input_table)
      print(option_modified_sql_input)

#Connect to database1
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")
      
#Case six:sorting data
elif (user_choice == "6"):
      
      #print schema page to help users with input
      print("<You are now sorting data in the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table = input("Choose the table to perform sorting: ")
      user_input_order = input("Choose whether to sort in ascending or descending order[ASC, DESC]: ")
      user_input_column = input("Input the column you want to sort with: ")
      option_modified_sql_input = ("SELECT * FROM {} ORDER BY {} {};").format(user_input_table, user_input_column, user_input_order)
      print(option_modified_sql_input)

#Connect to database1
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")

#Case seven:joining data
elif (user_choice == "7"):
      
      #print schema page to help users with input
      print("<You are now joining data in the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table1 = input("Input the first table you want to join: ")
      user_input_table2 = input("Input the second table you want to join: ")
      user_input_join_column1 = input("Input the column in first table to join on")
      user_input_join_column2 = input("Input the column in second table to join on")
      option_modified_sql_input = (f"SELECT * FROM {user_input_table1} JOIN {user_input_table2} ON {user_input_table1}.{user_input_join_column1} = {user_input_table2}.{user_input_join_column2};")
      print(option_modified_sql_input)

#Connect to database1
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")

#Case eight:grouping data
elif (user_choice == "8"):
      
      #print schema page to help users with input
      print("<You are now grouping data in the database")
      schema_display()
      #retrieve user query to be performed on the database
      user_input_table1 = input("Input the first table you want to join: ")
      user_input_table2 = input("Input the second table you want to join: ")
      user_input_join_column1 = input("Input the column in first table to join on")
      user_input_join_column2 = input("Input the column in second table to join on")
      option_modified_sql_input = (f"SELECT * FROM {user_input_table1} JOIN {user_input_table2} ON {user_input_table1}.{user_input_join_column1} = {user_input_table2}.{user_input_join_column2};")
      print(option_modified_sql_input)

#Connect to database1
      connection()
    
#recall the interface for multiple actions.
      interface()

#ask for another choice
      user_choice = input("Enter your choice here (1-12):")


      
      