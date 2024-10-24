 
import pandas as pd
from sqlalchemy import create_engine
# Create a database connection
connection_string = ''
engine = create_engine #(conexão)
# Define your SQL query
query = """

# colunas

"""
# Read SQL data into a DataFrame
df = pd.read_sql(query, engine)
# Display the DataFrame
df.to_excel('output.xlsx', index=False)
 
 


