import pandas
import pandas as pd
Rishta_profile = {
    "name" : ["Moheeb","Muneeb","Sohaib","Mudassir","Obaid"],
    "gender" : ["m","m","m","m","m"],
    "prefered_cast" : ["Bihari","Bihari","Rajput","Pathan","Bihari"],
    "prefered_area" : ["North karachi","Water pump","Nazimabad","Baldia","Gulshan"],
    "Profession" : ["IT", "IT", "Accounts","Teacher","IT"],
    "no_of_siblings" : [4,4,2,5,3]
}
df_Rishta = pd.DataFrame(Rishta_profile)
df_Rishta["age"] = [22,23,25,26,28]
print(df_Rishta)

print(df_Rishta[df_Rishta["prefered_cast"]=="Pathan"])
print(df_Rishta[df_Rishta["no_of_siblings"] >2])
print(df_Rishta[df_Rishta["prefered_area"] == "DHA"])
print(df_Rishta[(df_Rishta["prefered_area"] == "Nazimabad") & (df_Rishta["gender"] == "f")])
df_Rishta["Marital_Status"] = ["Single","Widow","Divorce","Single","Divorce"]
del df_Rishta["Profession"]
df_Rishta["Nationality"] = ["Pakistan","Pakistan","Pakistan","Pakistan","Pakistan"]
print(df_Rishta)