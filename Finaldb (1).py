import streamlit as st
import sqlite3


# Connect to the SQLite database
conn = sqlite3.connect(r"C:\Users\Sejal\OneDrive\Documents\vs_codes\Table10.db") #path of already created table
cursor = conn.cursor()


# Function to execute SQL command
def execute_sql(sql_command, data=None):
    try:
        with conn:
            cursor = conn.cursor()
            if data:
                cursor.execute(sql_command, data)
            else:
                cursor.execute(sql_command)
            st.success("Operation successful")
    except sqlite3.Error as e:
        st.error(f"SQLite error: {e}")


# Function to insert data into the Events table
def insert_event(event_id, event_name, event_date, event_location, event_description):
    # Check if the event_id already exists
    cursor.execute("SELECT EventID FROM Events WHERE EventID=?", (event_id,))
    existing_event = cursor.fetchone()

    if existing_event:
        st.error(f"Event with EventID {event_id} already exists.")
        return
    #Insert Data
    sql_command = "INSERT INTO Events (EventID, EventName, EventDate, EventLocation, EventDescription) VALUES (?, ?, ?, ?, ?)"
    data = (event_id, event_name, event_date, event_location, event_description)
    
    execute_sql(sql_command, data)
# Function to insert data into the Attendees table

def insert_attendee(attendee_id, first_name, last_name, email, phone, registration_date, event_id):
    # Check if the attendee_id already exists
    cursor.execute("SELECT AttendeeID FROM Attendees WHERE AttendeeID=?", (attendee_id,))
    existing_attendee = cursor.fetchone()

    if existing_attendee:
        st.error(f"Attendee with AttendeeID {attendee_id} already exists.")
        return
    
   
    sql_command = "INSERT INTO Attendees (AttendeeID, FirstName, LastName, Email, Phone, RegistrationDate, EventID) VALUES (?, ?, ?, ?, ?, ?, ?)"
    data = (attendee_id, first_name, last_name, email, phone, registration_date, event_id)
    
    execute_sql(sql_command, data)

# Function to update data in the Events table
def update_event(event_id, event_name, event_date, event_location, event_description):
    sql_command = "UPDATE Events SET EventName=?, EventDate=?, EventLocation=?, EventDescription=? WHERE EventID=?"
    data = (event_name, event_date, event_location, event_description, event_id)
    execute_sql(sql_command, data)

# Function to update data in the Attendees table
def update_attendee(attendee_id, first_name, last_name, email, phone, registration_date, event_id):
    sql_command = "UPDATE Attendees SET FirstName=?, LastName=?, Email=?, Phone=?, RegistrationDate=?, EventID=? WHERE AttendeeID=?"
    data = (first_name, last_name, email, phone, registration_date, event_id, attendee_id)
    execute_sql(sql_command, data)

# Function to delete data from the Events table
def delete_event(event_id):
    sql_command = "DELETE FROM Events WHERE EventID=?"
    data = (event_id,)
    execute_sql(sql_command, data)

# Function to delete data from the Attendees table
def delete_attendee(attendee_id):
    sql_command = "DELETE FROM Attendees WHERE AttendeeID=?"
    data = (attendee_id,)
    execute_sql(sql_command, data)
# Function to Truncate Table
def truncate_table(table_name):
    sql_command = f"DELETE FROM {table_name}"
    execute_sql(sql_command)
# Sidebar for table 
selected_table = st.sidebar.radio("Select a Table", ["Events", "Attendees"])
selected_action = st.sidebar.radio("Select an Action", ["Insert", "Update", "Delete","Truncate"])

if selected_table == "Events":
    st.header("Events Table")

    if selected_action == "Insert":
        # Insert Data
        st.subheader("Insert Data")
        event_id = st.number_input("Event Id")
        event_name = st.text_input("Event Name")
        event_date = st.date_input("Event Date")
        event_location = st.text_input("Event Location")
        event_description = st.text_area("Event Description")

        if st.button("Insert Event"):
            insert_event(event_id,event_name, event_date, event_location, event_description)

    elif selected_action == "Update":
        # Update Data
        st.subheader("Update Data")
        event_id = st.number_input("Event ID")
        event_name = st.text_input("Event Name")
        event_date = st.date_input("Event Date")
        event_location = st.text_input("Event Location")
        event_description = st.text_area("Event Description")

        if st.button("Update Event name"):
            sql_command=f"UPDATE Events SET EventName = '{event_name}' WHERE EventID = {event_id }"
            execute_sql(sql_command)
        if st.button("Update Event date"):
            sql_command=f"UPDATE Events SET EventDate = '{event_date}' WHERE EventID = {event_id }"
            execute_sql(sql_command)
        if st.button("Update Event Location"):
            sql_command = f"UPDATE Events SET EventLocation = '{event_location}' WHERE EventID = {event_id }"
            execute_sql(sql_command)
        if st.button("Update Event description"):
            sql_command=f"UPDATE Events SET EventDescription = '{event_description}' WHERE EventID = {event_id }"
            execute_sql(sql_command)
        

    elif selected_action == "Delete":
        st.subheader("Delete Data")
        event_id = st.number_input("Event ID")

        if st.button("Delete Event"):
            delete_event(event_id)
    elif selected_action == "Truncate":
        st.subheader("Truncate Data")
        table_name = st.text_input("Table Name")

        if st.button("Truncate Table"):
            truncate_table(table_name)

elif selected_table == "Attendees":
    st.header("Attendees Table")

    if selected_action == "Insert":
        st.subheader("Insert Data")
        attendee_id = st.number_input("Attendee ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.number_input("Phone")
        registration_date = st.date_input("Registration Date")
        event_id = st.number_input("Event ID")

        if st.button("Insert Attendee"):
            insert_attendee(attendee_id, first_name, last_name, email, phone, registration_date, event_id)

    elif selected_action == "Update":
        st.subheader("Update Data")
        attendee_id = st.number_input("Attendee ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.number_input("Phone")
        registration_date = st.date_input("Registration Date")
        event_id = st.number_input("Event ID")
        if st.button("First_name update"):
            sql_command = f"UPDATE Attendees SET FirstName = '{first_name}' WHERE AttendeeID = {attendee_id}"
            execute_sql(sql_command)
        if st.button("Last_name update"):
            sql_command = f"UPDATE Attendees SET LastName = '{last_name}' WHERE AttendeeID = {attendee_id}"
            execute_sql(sql_command)
        if st.button("Email update"):
            sql_command = f"UPDATE Attendees SET Email = '{email}' WHERE AttendeeID = {attendee_id}"
            execute_sql(sql_command)
        if st.button("Phone update"):
            sql_command = f"UPDATE Attendees SET Phone = '{phone}' WHERE AttendeeID = {attendee_id}"
            execute_sql(sql_command)
        if st.button("Registeration_date update"):
            sql_command = f"UPDATE Attendees SET RegisterationDate = '{registration_date}' WHERE AttendeeID = {attendee_id}"
            execute_sql(sql_command)
        if st.button("EventID Update"):
            sql_command = f"UPDATE Attendees SET EventID = '{event_id}' WHERE AttendeeID = {attendee_id}"
            execute_sql(sql_command)

    elif selected_action == "Delete":
        st.subheader("Delete Data")
        attendee_id = st.number_input("Attendee ID")

        if st.button("Delete Attendee"):
            delete_attendee(attendee_id)
    elif selected_action == "Truncate":
        st.subheader("Truncate Data")
        table_name = st.text_input("Table Name")

        if st.button("Truncate Table"):
            truncate_table(table_name)



