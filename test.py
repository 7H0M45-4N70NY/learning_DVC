import pandas as pd  

Data=[{"Name":"Thomas","Age":200,"location":"Koattayam"},
      {"Name":"john","Age":20,"location":"Kottayam"},
      {"Name":"Sunny","Age":30,"location":"Bangalore"},
      {"Name":"Krish","Age":35,"location":"Bhopal"}]

Data= pd.DataFrame(Data)

Data.to_csv("data/data.csv")