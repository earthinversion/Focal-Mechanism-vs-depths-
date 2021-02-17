# ==================================================================
# Title:  Plot focal mechanism on depth vs lat/lat 
# Author: Utpal Kumar
# Date:   17 Feb 2021
# ==================================================================

import pandas as pd
import pygmt

dataFileName = 'focal_2020.dat'
df = pd.read_csv(dataFileName, sep='\s+')

lons = df['long'].values
lats = df['latitude'].values
depths = df['Depth'].values
strikes = df['str'].values
dips = df['dip'].values
rakes = df['rake'].values
magnitudes = df['mb'].values


### depth vs longitude
fig = pygmt.Figure()
fig.basemap(region=[lons.min()-5, lons.max()+5, depths.min()-5, depths.max()+5], projection="x1c", frame=["a1f1", 'WSne', "x+llongitudes", "y+ldepths"])


for ln, lt, st, dp, rk, dpth, mag in zip(lons, lats, strikes, dips, rakes, depths, magnitudes):
    print(ln, lt, st, dp, rk, dpth, mag)
    # store focal mechanisms parameters in a dict
    focal_mechanism = dict(strike=float(st), dip=float(dp), rake=float(rk), magnitude=float(mag))

    fig.meca(focal_mechanism, scale="0.1c", longitude=float(ln), latitude=float(dpth), depth=float(dpth))


fig.savefig('depth-long-plot.png', crop=True, dpi=720)
allformat = 0

if allformat:
    fig.savefig("depth-long-plot.pdf", crop=True, dpi=720)
    fig.savefig("depth-long-plot.eps", crop=True, dpi=300)
    fig.savefig("depth-long-plot.tif", crop=True, dpi=300, anti_alias=True)


### depth vs latitude
fig = pygmt.Figure()
fig.basemap(region=[lats.min()-5, lats.max()+5, depths.min()-5, depths.max()+5], projection="x1c", frame=["a1f1", 'WSne', "x+llatitudes", "y+ldepths"])


for ln, lt, st, dp, rk, dpth, mag in zip(lons, lats, strikes, dips, rakes, depths, magnitudes):
    print(ln, lt, st, dp, rk, dpth, mag)
    # store focal mechanisms parameters in a dict
    focal_mechanism = dict(strike=float(st), dip=float(dp), rake=float(rk), magnitude=float(mag))

    fig.meca(focal_mechanism, scale="0.1c", longitude=float(lt), latitude=float(dpth), depth=float(dpth))


fig.savefig('depth-lat-plot.png', crop=True, dpi=720)
allformat = 0

if allformat:
    fig.savefig("depth-lat-plot.pdf", crop=True, dpi=720)
    fig.savefig("depth-lat-plot.eps", crop=True, dpi=300)
    fig.savefig("depth-lat-plot.tif", crop=True, dpi=300, anti_alias=True)