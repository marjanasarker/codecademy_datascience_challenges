# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def float_damages(damages):
    new_list=[]
    for damage_num in damages:
        if damage_num!= 'Damages not recorded':
            if damage_num[-1]=='M':
                num_only=damage_num[:-1]
                new_damage=float(num_only)
                
                float_damage=new_damage*1000000
                damage_num=float_damage
                #print(float_damage)
            elif damage_num[-1]=='B':
                num_only=damage_num[:-1]
                new_damage=float(num_only)
                float_damage=new_damage*1000000000
                damage_num=float_damage
                #print(float_damage)
        new_list.append(damage_num)
    return new_list
converted_damages = float_damages(damages)
#print(float_damages(damages))
def hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths):
    hurricanes_desc=dict()
    for i in range(len(names)):
    #use get to add key 
    #hurricanes_desc[names[item]]["Name"]=names[item]
        hurricanes_desc[names[i]]={"Name":names[i],
                            "Month":months[i],
                            "Year":years[i],
                            "Max Sustained Wind":max_sustained_winds[i],
                            "Areas Affected": areas_affected[i],
                            "Damage":converted_damages[i],
                            "Deaths":deaths[i]}
    return hurricanes_desc

#print(hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths))

hurricanes=hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)

# write your construct hurricane by year dictionary function here:
def year_hurricane_dictionary(hurricanes):
    # created a new empty dictionary
    hurricanes_by_year=dict()
    # execute a for loop on hurricanes dictionary, go through each nested dictionary and assigning all element details to a variable
    # the year in the element will be stored in another variable to be assigned as key
    for hurricane_name in hurricanes: 
        current_year=hurricanes[hurricane_name]["Year"]
        current_rec=hurricanes[hurricane_name]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year]=[current_rec]
        else:
            hurricanes_by_year[current_year].append(current_rec)
    return hurricanes_by_year

    #use get to add key 
    #hurricanes_desc[names[item]]["Name"]=names[item]
hurricanes_by_year = year_hurricane_dictionary(hurricanes)
#print(hurricanes_by_year[1932])       

# write your count affected areas function here:
# separate dictionary for just the areas so I could use areas affected 

#all_areas = [place for places in areas_affected for place in places] # nice, taking away all the sublists from that list#
#print(all_areas)

def affected_areas_count(hurricanes):
    areas_affected_dict = {}
    for each_hurricane in hurricanes:
        for area in hurricanes[each_hurricane]['Areas Affected']:
            if area not in areas_affected_dict:
                areas_affected_dict[area]=1
            else:
                areas_affected_dict[area]+=1
    return areas_affected_dict
   
#print(areas_affected_dict)
affected_areas_counted=affected_areas_count(hurricanes)
# write your find most affected area function here:
def max_hurricane_area(affected_areas_counted):
    # to get key with max value
    key_max = max(affected_areas_counted, key=affected_areas_counted.get)
    all_values = affected_areas_counted.values()
    max_value = max(all_values)
    return key_max, max_value

max_hurricane=max_hurricane_area(affected_areas_counted)
#print(max_hurricane)

# write your greatest number of deaths function here:
# function should take the hurricanes dictionary, then query for deaths, find max deaths and return name associated
# with that 
def max_mortality_hurricane(hurricanes):
    max_death = max(deaths)
    #{}
    for each_hurricane in hurricanes:
        if hurricanes[each_hurricane]["Deaths"]==max_death:
            return hurricanes[each_hurricane]["Name"], max_death
    #return max_death
#print(max_mortality_hurricane(hurricanes))

# write your catgeorize by mortality function here:
def mortality_scale_category(hurricanes):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    mortality_category={0:[],1:[],2:[],3:[],4:[]}
    for each_hurricane in hurricanes:
        if hurricanes[each_hurricane]['Deaths']==0:
            mortality_category[0].append(hurricanes[each_hurricane]["Name"])
        elif hurricanes[each_hurricane]['Deaths']>0 and hurricanes[each_hurricane]['Deaths']<=100:
            mortality_category[1].append(hurricanes[each_hurricane]["Name"])
        elif hurricanes[each_hurricane]['Deaths']>100 and hurricanes[each_hurricane]['Deaths']<=500:
            mortality_category[2].append(hurricanes[each_hurricane]["Name"])
        elif hurricanes[each_hurricane]['Deaths']>500 and hurricanes[each_hurricane]['Deaths']<=1000:
            mortality_category[3].append(hurricanes[each_hurricane]["Name"])
        elif hurricanes[each_hurricane]['Deaths']>1000 and hurricanes[each_hurricane]['Deaths']<=10000:
            mortality_category[4].append(hurricanes[each_hurricane]["Name"])
    return mortality_category

print(mortality_scale_category(hurricanes))

# write your greatest damage function here:







# write your catgeorize by damage function here:
