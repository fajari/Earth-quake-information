"""
Application to detect current Earth Quake
This Application will scrape data from earthquake.usgs.gov and bmkg.go.id
Maintain by. MSF abcdefg
"""
import earthquake_alert

if __name__ == '__main__':
    result = earthquake_alert.data_extraction()
    earthquake_alert.show_data(result)
