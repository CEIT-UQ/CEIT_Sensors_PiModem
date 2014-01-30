'''
Created on Nov 22, 2012
@author: Buddhika De Seram
'''
class MQTT:
    database5 = None
    threed_pub = None
    client_cosm = "LIB_cosm"
    client_ts = "LIB_ts"
    client_3d = "LIB_3d"
    client_sense = "LIB_sense"
    client_3bpub = "3dPub"
    server = "winter.ceit.uq.edu.au"
    client = "LIB_temp"
    client_dblib = "lib_database"
    topic_db = "/LIB/config/level"
    topic_temp = "/LIB/level4/climate_raw"
    topic_3d = "/LIB/3d/data"
    packet = {"id":"11.11.11", "value":0}
    directory = "/home/pi/CEIT_Sensors_PiModem"
    rc = None
    pi_id = None
    config = {'1.13.0':'402','15.11.0':'401','15.12.0':'401','17.11.0':'401','17.12.0':'401','17.13.0':'401','22.11.0':'402','22.12.0':'402','22.13.0':'402','23.11.0':'402','23.12.0':'402','23.13.0':'402','25.11.0':'402','25.12.0':'402','255.11.0':'401','255.12.0':'401','255.13.0':'401','27.11.0':'402','27.12.0':'402','29.11.0':'401','29.12.0':'401','30.11.0':'402','30.12.0':'402','30.13.0':'402','31.13.0':'401','32.11.0':'401','32.12.0':'401','33.11.0':'402','33.12.0':'402','34.11.0':'402','34.12.0':'402','39.11.0':'401','39.12.0':'401','40.11.0':'402','40.12.0':'402','40.13.0':'402','42.11.0':'402','42.12.0':'402','43.11.0':'401','43.12.0':'401','45.11.0':'401','45.12.0':'401','51.13.0':'402','54.11.0':'402','54.12.0':'402'}
