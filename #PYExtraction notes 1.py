#PYExtraction notes 1
#Extracting data from a pdf on a website using python using jupyterlab
# we first need to import the necessary libraries
import requests
import pdfplumber
import pandas as pd

# Then we extract the data from the website using the requests library
url = "https://www.chisambacouncil.gov.zm/wp-content/uploads/2025/12/2024-CDF-APPROVED-COMMUNITY-PROJECTS-CHISAMBA-1-2.pdf"
response = requests.get(url, verify=False)
print(response.status_code)
print(len(response.content))

#rename and save the pdf file to a local directory
with open( "Chisamba2024.pdf","wb") as f:
    f.write(response.content)
print("PDF saved Successfully")

# Now we can use the pdfplumber library to extract the data from the pdf file
with pdfplumber.open("chisamba2024.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
print(tables)

# Now we can convert the extracted data into a pandas dataframe for further analysis
all_rows = []
with pdfplumber.open("Chisamba2024.pdf") as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        all_rows.extend(table)
df = pd.DataFrame(all_rows[1:], columns=all_rows[0])
df

# Now we can save the dataframe to a csv file for further analysis
df.to_csv("Chisamba2024_raw.csv" , index=False)
print("Raw dataset saved")

#Push to github for other collaborators to work on.