f = open("genfile.txt", "w")

rangegen = 300
string = "		{ \"predicate\": { \"custom_model_data\": "
string1 = "}, \"model\": \"custom/item"

for x in range(rangegen):
  f.write(string + str(x+1) + string1 + str(x+1) + "\" }," + "\n")  

f.close()