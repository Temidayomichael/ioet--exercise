
# ioet Position - Coding exercise

A brief description of what this project does and who it's for


## Overview

  In the given exercise, an employee salary is to be calculated based on the days and hours worked,
  the days are divided into 2 groups:
  
  - Monday - Friday (Weekdays)
  - Saturday - Sunday (Weekends)

  Each day in these categories are then sub-grouped into hourse with fixed price per hours range.

#### Examples   
  Input : ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
  
  Output: The amount to pay ASTRID is: 85 USD

  Input : RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
 
  Output : The amount to pay RENE is: 215 USD

## Architecture & Methodology
- **Read Input & Validate**
  
  Input datasets are in a **data.txt** file then read programmatically.
  
  All datasets must also match the given input format so **regex** was used to verify this format ( RENE=MO10:00-12:00,TU10:00-12:00 )

- **Data seperation**

  For each of the datasets, it was splitted into :
    
      Name
      Schedule
  Then for each of the Schedule the day is seperated from the start time and end time, then both times were passed along with the price constants to the calculate function.

- **Salary calculation**
    
    #### The salary is calculated in the following steps:
       - Determine if the schedule is in Weekdays or Weekends.
       - Check for the time range that employee started working for that day.
       - The hours in each time range is checked and multiplied with the fixed hour rate for that range.
       - Return the saray for eacvh scheduled hours worked.

- **Display the calculated salary for each person**
### **Assumption**

```
  An employee can start working in an hours range and end it in another. 
  i.e the range being, 
  01:00 - 09:00
  09:00 - 18:00
  ...

  An employee's start time could be 03:00(within first range) then ends at 15:00(within second range),
  so the extra hours being in the other range must be calculated with that particular range price then added to the other calculated hours.
```
### **Reults**
  #### Here are the Five test datasets and the returned results:
  **Inputs**

      RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
      DIANA=MO01:00-12:00,TU10:00-12:00,TH01:00-03:00,SA15:00-18:00,SU20:00-21:00
      ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
      DAYO=MO10:00-12:00,TH06:00-14:00,SU20:00-22:00
  **Outputs**

      The amount to pay RENE is: 215 USD
      The amount to pay DIANA is: 410 USD
      The amount to pay ASTRID is: 85 USD
      The amount to pay DAYO is: 230 USD


## Run Locally

Clone the project

```
  git clone https://github.com/Temidayomichael/ioet--exercise
```

Go to the project directory

```
  cd ioet--exercise
```
In order to fetch the datasets

Please Install live server plugin on Vscode

```
  https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer
```

Start the server

```
  Click to **Go Live from the status bar to turn the server on/off.
  OR 
  Cight-click on the editor and click on Open with Live Server
  OR
  Right click on the HTML file from Explorer Window and click on Open with Live Server.
```

