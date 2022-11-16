"""
Application to detect current Earth Quake
This Application will scrape data from earthquake.usgs.gov and bmkg.go.id
Maintain by. MSF
"""


def data_extraction():
    """
    Info Gempa Mag:5.3, 16-Nov-22 16:22:45 WIB, Lok:5.38 LS, 102.38 BT (12 km Tenggara ENGGANO-BENGKULU), Kedlmn:26 Km #BMKG
    date_eq : 16-Nov-22
    time_eq : 16:22:45 WIB
    magnitudo_eq : 5.3
    location_place_eq : 12 km Tenggara ENGGANO - BENGKULU
    location_eq : 5.38 LS, 102.38 BT
    deepth_eq : 26 km
    :return:
    """
    scrape_result = dict()
    scrape_result['date_eq'] = '16-Nov-22'
    scrape_result['time_eq'] = '16:22: 45 WIB'
    scrape_result['magnitudo_eq'] = '5.3'
    scrape_result['location_place_eq'] = '12 km Tenggara TENGGANO - BENGKULU'
    scrape_result['location_eq'] = {'ls': 5.38 , 'bt': 102.38}
    scrape_result['depth_eq'] = '26 km'
#    print(scrape_result)
    return scrape_result


def show_data(result):
    print('Latest Eart Quake')
    print(f"Date : {result['date_eq']}")
    print(f"Time : {result['time_eq']}")
    print(f"Magnitudo : {result['magnitudo_eq']}")
    print(f"Epicentrum : {result['location_place_eq']}")
    print(f"Location : LS={result['location_eq']['ls']}, BT={result['location_eq']['bt']}")
    print(f"Depth : {result['depth_eq']}")
    return result


if __name__ == '__main__':
    print('Main Application')
    result = data_extraction()
    show_data(result)

