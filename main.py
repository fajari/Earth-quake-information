"""
Application to detect current Earth Quake
This Application will scrape data from earthquake.usgs.gov and bmkg.go.id
Maintain by. MSF
"""
# from earthquake_alert import data_extraction, show_data
import IndonesiaLatestEarthQuakeAlert

if __name__ == '__main__':
    result = data_extraction()
    show_data(result)
