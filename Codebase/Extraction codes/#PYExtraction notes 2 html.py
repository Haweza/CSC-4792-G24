#Extracting data from website page using python
import requests

url = "https://www.chisambacouncil.gov.zm/?p=2290"

response = requests.get(url, verify=False)

print(response.status_code)
print(len(response.text))

#This will give us the page's readable text.
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(" ", strip=True)

print(text[:5000])

#Let's create one record representing this disbursement event
data = {
    "Date": "2025-11-14",
    "Total_Disbursed_Kwacha": 4100200,
    "Beneficiary_Groups": 24,
    "Wards_Covered": 12,
    "CDF_Subprogram": "Loans",
    "Business_Areas": "Livestock farming; Fish farming; Butchery operations; Irrigation farming; Transport services",
    "Event_Location": "Civic Center",
    "Source": "Chisamba Town Council"
}

cdf_loans_df = pd.DataFrame([data])

cdf_loans_df

#Then save the raw extracted dataset:
cdf_loans_df.to_csv("Chisamba2025_CDF_Loan_Disbursement_raw.csv", index=False)