import numpy as np
from datetime import datetime 

ffile = "IDN60903.94926.axf"


(sort_order,wmo,name,history_product,local_date_time,local_date_time_full,aifstime_utc,
            air_temp,apparent_t,cloud,cloud_base_m,cloud_oktas,cloud_type,cloud_type_id,
            delta_t,dewpt,gust_kmh,gust_kt,lat,lon,press,press_msl,press_qnh,press_tend,
            rain_trace,rel_hum,sea_state,swell_dir_worded,swell_height,swell_period,vis_km,
            weather,wind_dir,wind_spd_kmh,wind_spd_kt) = np.genfromtxt(ffile,
            unpack=True,delimiter=',',skip_header=20, skip_footer=1,dtype='str')

air_temp = np.array(air_temp,dtype='float')
apparent_t = np.array(apparent_t,dtype='float')

dates = []
for d in local_date_time_full:
    date = datetime.strptime(d, '"%Y%m%d%H%M%S"')
    dates = np.append(dates,[date],axis=0)


data = np.column_stack((dates,air_temp,apparent_t))

np.savetxt('bom-data.csv',data,fmt="%s",delimiter=",",header="date,temp,apparent")