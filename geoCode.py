from pygeocoder import Geocoder

#opens original file
f = open("ORIGINAL_FILE.txt", "r")
#creates new file
n = open("NEW_FILE.txt", "w")

cities = []

i = 1
for line in f:
  #build columns by delimiting lines by tab; change to "," for CSV
  fields = line.split("\t")
  #take in fields, tell python to concatenate the last and 2nd to last fields with a comma
  location = fields[-1].strip()+", "+fields[-2]
  
  #add all of the cities to the cities list
  cities.append(location)

#Creates a set of unique/countd of city names
cities = list(set(cities))

#test: count # of cities; API limit is 2500 per day
#print len(cities)

results = Geocoder.geocode(location)
print(results[0].coordinates)


#polish it off by putting the cities with their geo-coordinates
for city in cities:
  results = Geocoder.geocode(city)
  n.write(city+","+str(results[0].coordinates)+"\n")


#for testing the printout, we can tell it to test on just 2 items
#for city in cities[:2]:
#results = Geocoder.geocode(city)
#n.write(city+","+str(results[0].coordinates)+"\n")
