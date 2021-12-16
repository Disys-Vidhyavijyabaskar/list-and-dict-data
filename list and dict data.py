db={"customer":{"1000":{"ID":"1000","name":"john smith","DOB":"01/01/2000","gender":"f","age":"20","zipcode":"08122-2324","amount":"1500.20"},"2000":{"ID":"2000","name":"jim MCDonald","DOB":"02/02/2020","gender":"m","age":"25","zipcode":"08136-2324","amount":"1500.20"},"20":{"ID":"20","name":"jim MCDonald","DOB":"02/02/1999","gender":"m","age":"25","zipcode":"08124-6565","amount":"1500.20"}}}

for i in db.values():
    #print(i)
    for j in i.values():
        for k,l in j.items():
            if k=="Age" and int(l)>25:
                print(j,l)
            else:
                print("no customer found in the database")
            break
        
