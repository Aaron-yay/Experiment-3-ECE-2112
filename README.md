# Experiment-3-ECE-2112
#### Objectives: 
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

## Problem 1
### Instructions:
Using knowledge obtained from the experiment and demonstrations:
a. Load the corresponding .csv file into a data frame named cars using pandas </br>
b. Display the first five and last five rows of the resulting cars </br>
c. Save your file as Surname_Pandas-P1.py

#### Process:
To begin coding, I first needed access to the pandas library so the first line of code is:
- import pandas as pd

Next, to gain access to the file cars.csv, I used the pd.read_csv() function and assigned it to variable A to make the other functions easier to use:
- A = pd.read_csv('cars.csv')

To get the first 5 rows of the given data frame and get the output, I used the .head() pandas function as:
- A.head()

Similarly, to get the last 5 rows, I used the .tail() function:
- A.tail()

To save the file in a .py format, I went to the file tab, picked the "Save and Export Notebook As" option and clicked "Executable script"

## Problem 2
### Instructions:
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations. </b>

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. </br>
b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. </br>
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? </br>
d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 </br>
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. </br>
e. Save your file as Surname_Pandas-P2.py

#### Process:
Same as the first problem, I imported the pandas library and used pd.read_csv to gain access to cars.csv
- import pandas as pd
- C = pd.read_csv('cars.csv')

For problem 'a', I first needed to get the first 5 rows so I used the .head() function and assigned it to variable B so I can use it for other functions:
- B = C.head()

To isolate the odd-numbered columns, I then used the .iloc[] function as:
- B.iloc[:, 0:12:2]

Where the left of the brackets represent the rows (left empty since I already used the .head() function) and the right is the columns. By typing it as 0:12:2 I get the column starting from column 0 to column 12, at increments of 2. Which gives me the output of odd-numbered columns. </br>

Next, for problem 'b' I used the .loc function as it allows me to set specific conditions to get the output I want. I was able to plug-in the name of the column I wanted to iterate and the "value" I wanted to find which led to the code:
- B.loc[B['Model'] == 'Mazda RX4']

Similar to problem 'b' which is problem 'c', the same process happens except within the brackets, I added an extra condition indicating that I only wanted 1 specific output (which was the 'cyl') and ended up with the code:
- C.loc[C['Model'] == 'Camaro Z28', ['cyl']]

Finally, problem 'd' is similar to problem 'c' but now asks for more than 1 specific car. So I went and used the similar syntax for the code to solve problem 'c' and added more cars in the function by using the | key which means "OR" and allows me to return a value as long as one of the conditions is satisfied. All of this leads to the code:
- C.loc[(C['Model']=='Mazda RX4 Wag')|(C['Model']=='Ford Pantera L')|(C['Model']=='Honda Civic'), ['cyl','gear']]

Which outputs the 'cyl' and 'gear' of these 3 cars. With all the problems solved, I did the same process as in problem 1 to save problem 2 in a .py format

##### Note:
Notebook saved as well :)
