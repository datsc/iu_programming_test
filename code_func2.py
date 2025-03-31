import pandas as pd
import sys


user_name  = sys.argv[1]
file_name = sys.argv[2]

print(user_name)


def writing_data(df, file_name, user_name):

	df.to_csv(file_name)
	print(f"""{user_name} wrote the following to file {file_name}:
	   {df}""")
	return df

data = pd.DataFrame(data={'Day':[1,5,19],'Activity':['swimming','reading','cycling']})

df_written = writing_data(data, file_name, user_name)

