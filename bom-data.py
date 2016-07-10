import numpy as np
import json
import os
import urllib

path = "/Users/cherief/kateandcat/assets/bom"
#path = ""

url_cbr = "http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"


compass = {"N":0,"NNE":1,"NE":2,"ENE":3,"E":4,"ESE":5,"SE":6,"SSE":7,"S":8,"SSW":9,"SW":10,"WSW":11,"W":12,"WNW":13,"NW":14,"NNW":15,"CALM":0}

urllib.urlretrieve(url_cbr, os.path.join(path,"IDN60903.94926.json"))

def read_json():

    ffile = os.path.join(path,"IDN60903.94926.json")
    jsondata = open(ffile).read()
    data = json.loads(jsondata)["observations"]["data"]
    date,air_temp,apparent_t,wind_dir,wind_kmh,wind_color= ["date"],["temp"],["apparent"],["wind_dir"],["wind_kmh"],["wind_color"]
    for i in xrange(0,len(data)):
        d,t,a,w,k = data[i]["local_date_time_full"],data[i]["air_temp"],data[i]["apparent_t"],data[i]["wind_dir"],data[i]["wind_spd_kmh"]
        date.append(d)
        air_temp.append(t)
        apparent_t.append(a)



        w_convert = compass.get(w)*(2.*np.pi/16.)
        print w,w_convert



        wind_dir.append(w_convert)
        wind_kmh.append(k)

        if k <= 20:
            c = 0.
        elif 20 < k <= 25:
            c = 1.
        elif 25 < k <= 30:
            c = 2.
        elif 30 < k <= 35:
            c = 3.
        else:
            c = 4.


        wind_color.append(c)

    data = np.column_stack((date,air_temp,apparent_t,wind_dir,wind_kmh,wind_color))
    np.savetxt(os.path.join(path,'bom-data.csv'),data,fmt="%s",delimiter=",")

read_json()    

  
