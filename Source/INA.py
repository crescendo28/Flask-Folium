import folium
import folium.features
import pandas as pd
import geopandas as gpd

ipm_ina = pd.read_csv("IPM INA.csv")
geo_indo = gpd.read_file("indonesia-prov.geojson")

    
df_merge = geo_indo.merge(ipm_ina, how="inner", left_on = "Propinsi", right_on="Provinsi")


#ipm_ina['bins'] = pd.qcut(ipm_ina['IPM'],
#                          q=[0,.2,.4,.6,.8,1])

#max_ipm = ipm_ina["IPM"].max()
#min_ipm = ipm_ina["IPM"].min()

ina = folium.Map(location=(-2.49607,117.89587), zoom_start=5, tiles="cartodb positron")
folium.GeoJson(geo_indo).add_to(ina)

folium.Choropleth(
    geo_data= geo_indo,
    data=ipm_ina,
    columns=["Provinsi","IPM"],
    key_on= "feature.properties.Propinsi",
    bins=[60,68.5,71,71.5,72.5,81],
    fill_color="Blues",
    fill_opacity=0.8,
    line_color="Grey",
    line_opacity=0.3,
    legend_name="Tingkat IPM Per Provinsi di Indonesia",
    name="Nilai IPM per Provinsi di Indonesia"
).add_to(ina)
folium.LayerControl().add_to(ina)

#nambah pointer per provinsi
style_func = lambda x: {"fillColor":"#ffffff", 
                        "color":"#000000",
                        "fillOpacity":0.1,
                        "weight":0.1}

highlight_func = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}

#pop-up tooltip

NIL = folium.features.GeoJson(
    data=df_merge,
    style_function=style_func,
    control=False,
    highlight_function=highlight_func,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Provinsi','IPM'],
        aliases=['Provinsi','IPM'],
        style=('background-color: white; color:#333333; font-family: arial; font-size:12px; padding: 10px;')
    )
)

ina.add_child(NIL)
ina.keep_in_front(NIL)

ina.save("ina.html")