import pywavefront
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def return_csv(obj_file):
    
    target = pywavefront.Wavefront(str(obj_file), collect_faces = True)
    target_vertices = np.array(target.vertices, dtype = "f").transpose()
    df = pd.DataFrame(columns = ["X", "Y", "Z"])
    
    for i, j in enumerate(df.columns):
        df[j] = target_vertices[i]
        
    return df

def return_np(obj_file):
    
    target = pywavefront.Wavefront(str(obj_file), collect_faces = True)
    target_vertices = np.array(target.vertices, dtype = "f").transpose()
    
    return target_vertices

def make_3d_plot(df,i,j):

    fig = plt.figure(figsize = (i,j))
    ax = plt.axes(projection="3d")
    ax.scatter(df['X'], df['Y'], df['Z'], 'grey')
    plt.show()


def sample_data(df, value):
    
    if value < 1:
        sample = df.sample(frac = value, random_state = 4444)
    
    if value > 1:
        sample = df.sample(n = value, random_state = 4444)
        
    return sample

