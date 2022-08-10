# Planet App
This is a quick application used to find a number of factors using data from the [open exoplanet catalogue](https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets). 
This app requires no input and should update automatically with changes provided in the catalogue.
###### Data that is pulled in this app:
- The number of planets with no star (AKA Orphan Planets).
- The planet with the hottest star.
- The number of planets discovered each year sorted by size.

## Developer Info
This application was built in Python 3.10, so you may encounter an issue with running in older editions. In an effort to keep the code concise and efficient the only import is the requests module. 
You can run this app by running this command: Python {path to src/main.py} 

### Testing
All the test done are automated unit test. You can run them with the command: python -m unittest test.TestSum in {filepath to test folder}

### Questions
1. why did you make the design choice you made?
   - I wanted the app to be lightweight and easy to use. I also decided to use Python as it is a loosely coupled language that would make short work of this kind of use case.
2. What assumptions did you make and why?
   - The biggest assumption I made was how to decide if a planet is an orphan. Since there were 4 fields pertaining to a star I decided only if all 4 were blank would it be considered an orphan.
   - I alos maade the assumption that the year data would be a number and decided not to do a validation for the year other than a null check.
3. Why did you choose not to do some things?
    - Most of the decisions I made were in the interest of keeping the app lightweight and efficient.
