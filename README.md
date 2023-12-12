# Customer-Segmentation

This is group 12 Project Exhibition:  
 
Priyam jain  
Subham Mishra  
Rishabh Gupta  
Yashaswi Patel  

please run the MAAIN.py
before running file updater

This model groups customer based on their income and spending habbits

The purpose of the <b>file_writer_updated_cv.py</b> is to take the updated customer data from an existing CSV file, append it to a new CSV file called updated_data.csv, and then pass that updated file to another script for further processing.

## Here is how to run this customer segmentation project runs:

- The initial customer data would be loaded from Mall_Customers.csv as seen in MAAIN.py.

- MAAIN.py contains the core logic to preprocess data, run clustering algorithms, label data and save results. This file needs to be run first.

- New customer data would be collected periodically (let's say hourly) through a Google Form and saved to a CSV file.

- file_writer_updated_cv.py acts as a scheduler. It monitors this CSV for new records and appends them to updated_data.csv

- When the number of new records exceeds 50, it calls the algo() function from MAAIN.

- MAAIN then reads updated_data.csv, combines it with original labeled data, reprocesses and refits the model.

-  This updates the model incrementally with new data as it arrives hourly.

-  The updated model can then be used for predicting clusters of new customers in real-time.
