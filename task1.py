# David Coldeira - A demo code 17/06/2024


import pandas as pd
import requests

# Fetch data from an API
url = 'https://dummyjson.com/users'
response = requests.get(url)
data = response.json()

# Process the data (limit to the first 4 records)
users = data['users'][:4]
processed_data = []

for user in users:
    processed_data.append({
        'Name': f"{user['firstName']} {user['lastName']}",
        'Email Address': user['email'],
        'Age': user['age'],
        'Gender': user['gender'].capitalize(),
        'Phone': user['phone'],
        'Latitude': user['address']['coordinates']['lat'],
        'Longitude': user['address']['coordinates']['lng'],
        'DOB': user['birthDate']
    })

# Convert to DataFrame
df = pd.DataFrame(processed_data)

# Save to Excel
output_path = 'processed_users.xlsx'
df.to_excel(output_path, index=False)

print(f"Data has been saved to {output_path}")
