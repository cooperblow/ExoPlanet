import unittest

from src.main import check_hottest_star
from src.main import check_size
from src.main import check_if_orphan

default_dic = {
    "PlanetIdentifier": "Kepler-389 c",
    "TypeFlag": 0,
    "PlanetaryMassJpt": "",
    "RadiusJpt": 0.13305,
    "PeriodDays": 14.51143,
    "SemiMajorAxisAU": "",
    "Eccentricity": "",
    "PeriastronDeg": "",
    "LongitudeDeg": "",
    "AscendingNodeDeg": "",
    "InclinationDeg": "",
    "SurfaceTempK": "",
    "AgeGyr": "",
    "DiscoveryMethod": "transit",
    "DiscoveryYear": 2014,
    "LastUpdated": "14/02/26",
    "RightAscension": "19 27 50",
    "Declination": "+44 54 00",
    "DistFromSunParsec": 1101.76,
    "HostStarMassSlrMass": "",
    "HostStarRadiusSlrRad": 0.792,
    "HostStarMetallicity": "",
    "HostStarTempK": 5376,
    "HostStarAgeGyr": ""
  }

class TestSum(unittest.TestCase):
    def test_orphan_1(self):
        result = check_if_orphan(default_dic)
        self.assertEqual(result,False)

    def test_orphan_2(self):
        default_dic["HostStarRadiusSlrRad"] = ""
        result = check_if_orphan(default_dic)
        self.assertEqual(result,False)

    def test_orphan_3(self):
        default_dic["HostStarRadiusSlrRad"] = ""
        default_dic["HostStarTempK"] = ""
        result = check_if_orphan(default_dic)
        self.assertEqual(result,True)

    def test_orphan_4(self):
        default_dic["HostStarRadiusSlrRad"] = ""
        default_dic["HostStarTempK"] = ""
        default_dic["HostStarMassSlrMass"] = 5
        result = check_if_orphan(default_dic)
        self.assertEqual(result,False)

    def test_orphan_5(self):
        default_dic["HostStarRadiusSlrRad"] = ""
        default_dic["HostStarTempK"] = ""
        default_dic["HostStarMetallicity"] = 5
        result = check_if_orphan(default_dic)
        self.assertEqual(result,False)

    def test_orphan_6(self):
        default_dic["HostStarRadiusSlrRad"] = ""
        default_dic["HostStarTempK"] = ""
        default_dic["HostStarAgeGyr"] = 5
        result = check_if_orphan(default_dic)
        self.assertEqual(result,False)

    def test_year_addtion_1(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 1, 'medium': 0, 'large': 0}}
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_2(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 0, 'medium': 1, 'large': 0}}
        default_dic["RadiusJpt"] = 1.0
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_3(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 0, 'medium': 1, 'large': 0}}
        default_dic["RadiusJpt"] = 1
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_4(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 0, 'medium': 0, 'large': 1}}
        default_dic["RadiusJpt"] = 2
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_5(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 0, 'medium': 0, 'large': 1}}
        default_dic["RadiusJpt"] = 100
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_6(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 1, 'medium': 0, 'large': 0}}
        default_dic["RadiusJpt"] = -100
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_7(self):
        year_dic = {}
        exp_year_dic = {'2014': {'small': 1, 'medium': 0, 'large': 0}}
        default_dic["RadiusJpt"] = -100
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_year_addtion_8(self):
        year_dic = {}
        exp_year_dic = {'1': {'small': 1, 'medium': 0, 'large': 0}}
        default_dic["DiscoveryYear"] = 1
        result = check_size(year_dic, default_dic)
        self.assertEqual(result,exp_year_dic)

    def test_hottest_star_1(self):
        hottestP = "test planet"
        hottestST = 1000
        # hottestP = planet["PlanetIdentifier"]
        # hottestST = planet["HostStarTempK"]
        result, result2 = check_hottest_star(default_dic, hottestP, hottestST)
        self.assertEqual(result,"Kepler-389 c")
        self.assertEqual(result2,5376)

    def test_hottest_star_2(self):
        hottestP = "test planet"
        hottestST = 10000
        # hottestP = planet["PlanetIdentifier"]
        # hottestST = planet["HostStarTempK"]
        result, result2 = check_hottest_star(default_dic, hottestP, hottestST)
        self.assertEqual(result,"test planet")
        self.assertEqual(result2,10000)

    def test_hottest_star_3(self):
        hottestP = "test planet"
        hottestST = 5376
        # hottestP = planet["PlanetIdentifier"]
        # hottestST = planet["HostStarTempK"]
        result, result2 = check_hottest_star(default_dic, hottestP, hottestST)
        self.assertEqual(result,"test planet and Kepler-389 c")
        self.assertEqual(result2,5376)

if __name__ == '__main__':
    unittest.main()