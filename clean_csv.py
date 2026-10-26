import sqlite3
import csv

# 1. Connect to your engineered database
conn = sqlite3.connect("quotes_database.db")
cursor = conn.cursor()

# 2. Query using your exact database column names
query = """
SELECT 
    Quote, 
    Author, 
    Tags, 
    Word_Count 
FROM clean_quotes;
"""
cursor.execute(query)
cleaned_rows = cursor.fetchall()

# 3. Write directly to a clean CSV using Python's native CSV module
with open("clean_quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    # Write matching column headers for your spreadsheet
    writer.writerow(["Quote_Text", "Author", "Tags", "Word_Count"])
    
    # Write all the processed rows
    writer.writerows(cleaned_rows)

print("🚀 Success! 'clean_quotes.csv' has been generated.")

# Close the database connection
conn.close()
