import pywavefront
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def return_csv(obj_file):
    
    target = pywavefront.Wavefront(str(obj_file), collect_faces = True)
    target_vertices = np.array(target.vertices, dtype = "f").transpose()
    df = pd.DataFrame(columns = ["X", "Z", "Y"])
    
    for i, j in enumerate(df.columns):
        df[j] = target_vertices[i]
        
    return df

def return_np(obj_file):
    
    target = pywavefront.Wavefront(str(obj_file), collect_faces = True)
    target_vertices = np.array(target.vertices, dtype = "f").transpose()
    
    return target_vertices

class ObjectFile:
    
    def __init__(self, obj_file, *sample_size):
        
        self.obj_file = obj_file
        self.df = return_csv(self.obj_file)
        self.np_array = return_np(self.obj_file)
        
        if sample_size:
            
            self.sample_size = sample_size[0]
            self.sample_df = self.sample_data(self.sample_size)
    
    def make_3d_plot(self, i):

        fig = plt.figure(figsize = (i,i))
        ax = plt.axes(projection="3d")
        ax.scatter(self.df['X'], self.df['Z'], self.df['Y'])
        plt.show()
        
        
    def make_3d_sampled_plot(self, i):
        
        fig = plt.figure(figsize = (i,i))
        ax = plt.axes(projection="3d")
        ax.scatter(self.sample_df['X'], self.sample_df['Z'], self.sample_df['Y'])
        plt.show()
            
    def sample_data(self, value):
        
        if value < 1:
            sample = self.df.sample(frac = value, random_state = 4444)
        
        if value > 1:
            sample = self.df.sample(n = value, random_state = 4444)
            
        return sample


