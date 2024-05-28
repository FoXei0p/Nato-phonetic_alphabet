import pandas
row_data = pandas.read_csv("nato.csv")
data = {row.letter: row.code for (index, row) in row_data.iterrows()}

user = input("Enter a letter OR word: ").upper()
print([data[letter] for letter in user])



