# API Request JSON Processing

 **Objective**

To fetch JSON data from [https://dummyjson.com/users/](https://dummyjson.com/users/) using Python, manipulate the data, and export the processed data into Excel format with the expected output.

For this task, I have set up a virtual environment to maintain a unified development environment (no actually pushed into this repo).


The main script is `task1.py`. While the script is mostly self-explanatory, let's break down the steps taken:

For the dependencies, we use Pandas for handling datasets, Requests for making HTTP requests, and Openpyxl for Excel file operations. Install these libraries using:


```python
pip install pandas requests openpyxl
```

We then imported these libraries into our script:

```python
import pandas as pd
import requests
```
Next, we create three variables: `url`, which holds the API endpoint; `response`, the result of the GET request using requests.get(), and `data`, which stores the JSON content of the response converted into a dictionary.

```python
url = 'https://dummyjson.com/users'
response = requests.get(url)
data = response.json()
```
We now define `users` as a list containing the first 4 user records from the API response, as instructed. The slicing ([:4]) selects only the first 4 items.

```python
users = data['users'][:4]
```

In order to get the data as required, we imported datetime from the datetime module.
Inside the loop, we extracted the DOB string from the user dictionary (user['birthDate']).
We defined the original format of the DOB string (replaced "%Y-%m-%d" with the actual format).
We then used datetime.strptime to parse the DOB string into a datetime object and defined the new desired format ("%d/%m/%Y" for DD/MM/YYYY in this case).
We used date_obj.strftime(new_format) to format the datetime object into the desired string format.
We updated the 'DOB' key in the dictionary with the formatted string:

```python
processed_data = []

for user in users:
    # Extract DOB as string
    dob_str = user['birthDate']

    # Use strptime to parse the existing format
    from datetime import datetime
    original_format = "%Y-%m-%d"  # Replace with the actual format if known
    date_obj = datetime.strptime(dob_str, original_format)

    # Use strftime to format the date in DD/MM/YYYY
    new_format = "%d/%m/%Y"
    formatted_dob = date_obj.strftime(new_format)

    processed_data.append({
        'Name': f"{user['firstName']} {user['lastName']}",
        'Email Address': user['email'],
        'Age': user['age'],
        'Gender': user['gender'].capitalize(),
        'Phone': user['phone'],
        'Latitude': user['address']['coordinates']['lat'],
        'Longitude': user['address']['coordinates']['lng'],
        'DOB': formatted_dob
    }
   )
```

We created an empty list `processed_data` to store the processed user data.
The `for user in users` loop iterates through each user in the users list. Using the `f"..."` syntax (f-strings), we perform data extraction: for each user, we extract required fields and populate a dictionary with formatted data such as `Name` (concatenating `firstName` and `lastName`), `Email Address` (extracting the email), and so forth.


To create the data, we use the DataFrame() function from Pandas:

```python
df = pd.DataFrame(processed_data)
```

This function uses the `processed_data` list created earlier, where each dictionary in the list corresponds to a row in the DataFrame.

Finally, we use the Openpyxl library to save the data to an Excel spreadsheet:

```python
output_path = 'processed_users.xlsx'
df.to_excel(output_path, index=False)
print(f"Data has been saved to {output_path}")
```


So `output_path` specifies the Excel file where the data will be saved.
`df.to_excel(output_path, index=False)` saves the DataFrame to the specified Excel file. The `index=False` parameter ensures that the row indices are not included in the Excel file.
Finally, `print(f"Data has been saved to {output_path}")` prints a message confirming that the data has been saved.
