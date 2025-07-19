from random import choice

import pandas as pd
import lxml
dishes = {
    "Food_name" : ["Biryani","Zinger","Pizza","Finger Fish","Daal Chawal","Karahi"],
    "Price": [250, 300, 400, 800, 200,1500],
    "Category" : ["Desi","Fast Food","Fast Food","Sea Food","Desi","Desi"],
    "Main_ingredient" : ["Rice","Chicken","Dough","Fish","Daal","mutton"],
    "Quantity" : [5,7,4,4,6,3],
    "Status" : ["Available", "Available", "Not Available","Available","Available","Available"],
}
df_dis = pd.DataFrame(dishes)
print(df_dis)

df_dis["Country"] = ["Pakistan","USA","USA","Pakistan","Pakistan","Pakistan"]

df_dis["Sale_Price"] = ["200","250","350","700","150","1400"]

print(df_dis[df_dis["Price"] > 500])

print(df_dis[df_dis["Status"] == "Available"])

print(df_dis[(df_dis["Status"] == "Available") & (df_dis["Category"] == "Fast Food")])

print(df_dis[df_dis["Food_name"] == "Biryani"])

print(df_dis[(df_dis["Food_name"] == "Available") & (df_dis["Price"] > 1500)])

choice = input("Enter c - CSV\nx -XML\ne - Excel")
if choice.lower() == "c":
    df_dis.to_csv("MYCSVFILE", index= False)
elif choice.lower() == "x":
    df_dis.to_xml("MYXMLFILE.xml")
elif choice.lower() == "j":
    df_dis.to_xml("MYJSONFILE.js")
elif choice.lower() == "e":
    df_dis.to_xml("MYEXCELFILE.xlsx")
else :
    print("Invalid Input")




