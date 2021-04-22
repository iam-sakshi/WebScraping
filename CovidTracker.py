from covid import Covid
covid= Covid()
cntry = input("enter the name of the country you want to see status:")
cases=covid.get_status_by_country_name(cntry)
for x in cases :
    print(x," : ",cases[x])
