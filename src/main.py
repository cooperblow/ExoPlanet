import requests

s = requests.Session()

def check_if_orphan(planet):
    if str(planet["HostStarMassSlrMass"]) == "" \
            and str(planet["HostStarRadiusSlrRad"]) == "" \
            and str(planet["HostStarMetallicity"]) == "" \
            and str(planet["HostStarTempK"]) == "" \
            and str(planet["HostStarAgeGyr"]) == "":
        return True
    else:
        return False

def check_size(year_dic, planet):
    if str(planet["DiscoveryYear"]) == "":
        year = "unknown years"
    else:
        year = str(planet["DiscoveryYear"])
    if planet["RadiusJpt"] == "":
        status = 0
    else:
        status = float(planet["RadiusJpt"])
    if str(year) not in year_dic.keys():
        year_dic[year] = {}
        year_dic[year]["small"] = 0
        year_dic[year]["medium"] = 0
        year_dic[year]["large"] = 0
    if status < 1:
        year_dic[year]["small"]+=1
    elif status < 2:
        year_dic[year]["medium"]+=1
    elif status >= 2:
        year_dic[year]["large"]+=1
    return year_dic

def check_hottest_star(planet,hottestP,hottestST):
    if planet["HostStarTempK"] != "" and int(planet["HostStarTempK"]) >= hottestST:
        if int(planet["HostStarTempK"]) == hottestST:
            hottestP = "{} and {}".format(hottestP,planet["PlanetIdentifier"])
        else:
            hottestP = planet["PlanetIdentifier"]
            hottestST = planet["HostStarTempK"]
    return hottestP, hottestST

def planet_program():
    # getting data
    r = s.get("https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets")
    dic = r.json()
    year_dic = {}
    hottestP = ""
    hottestST = 0
    orphanC = 0
    for planet in dic:
        # checking star temperature
        hottestP, hottestST = check_hottest_star(planet,hottestP,hottestST)
        # check if the year exist in the year dictionary and planet size
        year_dic = check_size(year_dic,planet)
        # checking if the planet has a star
        if check_if_orphan(planet):
            orphanC += 1
    print("The number of planets with no star is {}".format(orphanC))
    print("The planet with the hottest star is {}".format(hottestP))
    # wanted to print the years in order
    print(year_dic)
    for i in sorted(year_dic.keys()):
        print("In {} we discovered {} small planets, {} medium planets, and {} large planets.".format(i,year_dic[i]["small"],year_dic[i]["medium"],year_dic[i]["large"]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    planet_program()

