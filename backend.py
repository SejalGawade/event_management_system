import sqlite3 as sql
conn = sql.connect("Table10.db")  

    # Create a cursor object to execute SQL commands
cursor = conn.cursor()

    # Create a table if it doesn't exist
cursor.execute('''CREATE TABLE Events (
    EventID INT PRIMARY KEY,
    EventName VARCHAR(255) NOT NULL,
    EventDate DATE NOT NULL,
    EventLocation VARCHAR(255),
    EventDescription TEXT)
''');
cursor.execute('''CREATE TABLE Attendees (
    AttendeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(15),
    RegistrationDate DATE NOT NULL,
    EventID INT, 
    CONSTRAINT FK_Event FOREIGN KEY (EventID) REFERENCES Events(EventID))
''');

    # Insert values into the table

data1=[(1, "Tech Conference 2023","2023-11-15","Mumbai","Annual technology conference featuring keynote speakers and tech workshops."),
 (2,"Music Festival","2023-07-28 ","Pune","Three-day music festival with live performances by various artists."),
 (3,"Startup Workshop","2023-09-10","Ahemedabad","Workshop for aspiring entrepreneurs on building successful startups."),
(4,"Charity Gala","2023-12-05","Delhi","Annual charity gala fundraiser for a local nonprofit organization."),
(5,"Art Exhibition Opening","2023-10-07","Punjab","Opening reception for a new art exhibition showcasing local artists.")]    
data2=[
    (101,'Aarav', 'Kumar', 'aarav.kumar@email.com', 1234, '2023-09-22', 1),
    (102,'Isha', 'Sharma', 'isha.sharma@email.com', 5678, '2023-09-22 ', 2),
    (103,'Advait', 'Patel', 'advait.patel@email.com', 9876, '2023-09-22 ', 1),
    (104,'Ananya', 'Singh', 'ananya.singh@email.com', 4321, '2023-09-23 ', 3),
    (105,'Diya', 'Rajput', 'diya.rajput@email.com', 8765, '2023-09-23 ', 2)]
for i in data1:
    cursor.execute('''INSERT INTO Events(EventID,EventName,EventDate,EventLocation,EventDescription) VALUES (?, ?,?,?,?)''',i)   
for j in data2:
    cursor.execute('''INSERT INTO Attendees (AttendeeID,FirstName, LastName, Email, Phone, RegistrationDate, EventID)
                      VALUES (?,?, ?, ?, ?, ?, ?)''',j)

    # Commit changes to the database
conn.commit()

    # Close the database connection
conn.close()
