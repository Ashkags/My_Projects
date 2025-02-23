import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

#sample dataset: Transactions with products
transactions = [
    ['Laptop', 'Mouse', 'Keyboard'],
    ['laptop', 'Headphones'],
    ['Phone', 'Charger'],
    ['Laptop', 'Mouse'],
    ['Phone', 'Charger']
]

#convert to Dataframe
df = pd.DataFrame(transactions)

#stack and reset index
stacked_df = df.stack().reset_index()
print(stacked_df)