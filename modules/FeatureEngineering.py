from cmath import nan
import glob
import os.path
from numpy import NaN
import pandas as pd
import math
from modules.Data import Data
class FeatureEngineering:
    def __init__(self,data:Data):
        self.data = data
        self.result = pd.DataFrame()
        self.dataFrameInitlize()

        
    def dataFrameInitlize(self):
       
      self.result["trackId"] = self.data.tracks_df["trackId"].unique()
        
# Ahmad
    def calculate_speed_deviation(self,row):
        track_id = int(row['trackId'])
        velocity = row['xVelocity']
        return math.sqrt(math.pow((velocity - self.data.avg_velocities[track_id]), 2) / len(self.data.tracks_df.index))


    # Ahmad
    def calculate_long_a_deviation(self,row):
        track_id = int(row["trackId"])
        long_a = row["xAcceleration"]
        return math.sqrt(math.pow(long_a - self.data.avg_accelerations[track_id], 2) / len(self.data.tracks_df.index))


    # Nasser
    def calculate_speed_variation(self,row):
        track_id = int(row["trackId"])
        DV1 = row["DV1"]
        mean = self.data.tracks_df[self.data.tracks_df["trackId"]==track_id]["xVelocity"].mean()
        return 100*(DV1/mean)


    # Ahmad
    def calculate_acceleration_variation(self,row):  # Use only the positive values from xAcceleration
        track_id = int(row["trackId"])


    # Omar
    def calculate_deceleration_variation(self,row):  # Use only the negative values from xAcceleration
        track_id = int(row["trackId"])


    # Karam
    def calculate_abs_speed_deviation(self,row):
        track_id = int(row["trackId"])


    # Yaseen
    def calculate_abs_acceleration_deviation(self,row):  # Use only positive values from xAcceleration
        track_id = int(row["trackId"])


    # Nasser
    def calculate_quantile_co_speed(self,row):
        track_id = int(row["trackId"])
        
        Q1 = ((self.data.tracks_df[self.data.tracks_df["trackId"]==track_id]["xVelocity"]).quantile(0.25))
        Q3 = ((self.data.tracks_df[self.data.tracks_df["trackId"]==track_id]["xVelocity"]).quantile(0.75))
        if((Q3+Q1 )== 0):
            return 0
        result =  100*((Q3-Q1)/(Q3+Q1))
        return result


    # Omar
    def calculate_quantile_co_acceleration(self,row):  # Use only the positive values for xAcceleration
        track_id = int(row["trackId"])
        trackDF = self.data.tracks_df[self.data.tracks_df["trackId"]==track_id]
        Acceleration = trackDF[trackDF["lonAcceleration"]>0]
        Q1 =Acceleration["lonAcceleration"].quantile(0.25)
        Q3 = Acceleration["lonAcceleration"].quantile(0.75)
        if Q1 + Q3 == 0 :
            return 0
        return 100*((Q3-Q1)/(Q3+Q1))
        



    # Hmouda
    def calculate_quantile_co_deceleration(self,row):  # Use only the negative values for xAcceleration
        track_id = int(row["trackId"])


    # Karam
    def calculate_percentage_time_speed(self,row):
        track_id = int(row["trackId"])


    # Yaseen
    def calculate_percentage_time_acceleration(self,row):  # Use only the positive values for xAcceleration
        track_id = int(row["trackId"])


    # Hmouda
    def calculate_percentage_time_deceleration(self,row):  # Use only the negative values for xAcceleration
        track_id = int(row["trackId"])
        dec1 = self.data.tracks_df[self.data.tracks_df["tracID"]==track_id]
        sd = row["DV2"]
        dec = dec1[dec1["xAcceleration"]<0]
        mean  =  dec["xAcceleration"].mean()
        count = dec[dec["xAcceleration"]>=mean+(2*sd)].count()
        return 100* (count/dec.count())
        

    def apply_dv1(self):
        self.data.tracks_df["DV1"] = self.result.apply(self.calculate_speed_deviation, axis=1)



    def apply_dv2(self):
        self.data.tracks_df["DV2"] = self.result.apply(self.calculate_long_a_deviation, axis=1)


    def apply_dv3(self):
        self.result["DV3"] = self.result.apply(self.calculate_speed_variation, axis=1)


    def apply_dv4(self):
        self.data.tracks_df["DV4"] = self.result.apply(self.calculate_acceleration_variation, axis=1)


    def apply_dv5(self):
        self.data.tracks_df["DV5"] = self.result.apply(self.calculate_deceleration_variation, axis=1)


    def apply_dv6(self):
        self.data.tracks_df["DV6"] = self.result.apply(self.calculate_abs_speed_deviation, axis=1)


    def apply_dv7(self):
        self.data.tracks_df["DV7"] = self.result.apply(self.calculate_abs_acceleration_deviation, axis=1)


    def apply_dv8(self):
         self.result["DV8"] = self.result.apply(self.calculate_quantile_co_speed, axis=1)
         print(self.result)


    def apply_dv9(self):
        self.result["DV9"] = self.result.apply(self.calculate_quantile_co_acceleration, axis=1)


    def apply_dv10(self):
        self.result["DV10"] = self.result.apply(self.calculate_quantile_co_deceleration, axis=1)


    def apply_dv11(self):
        self.result["DV11"] = self.result.apply(self.calculate_percentage_time_speed, axis=1)


    def apply_dv12(self):
        self.result["DV12"] = self.result.apply(self.calculate_percentage_time_acceleration, axis=1)


    def apply_dv13(self):
       self.result["DV13"] =  self.result.apply(self.calculate_percentage_time_deceleration, axis=1)


