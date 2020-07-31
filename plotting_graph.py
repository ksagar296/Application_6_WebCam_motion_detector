from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource


df["Start_string"] = df["START"].dt.strftime("%y-%m-%d %H:%M:%S")
df["End_string"] = df["END"].dt.strftime("%y-%m-%d %H:%M:%S")


cds = ColumnDataSource(df)

p= figure(x_axis_type='datetime',height=100,width=500, sizing_mode='scale_width', title="Motion Graph")

p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("START","@Start_string"),("END","@End_string")])

p.add_tools(hover)


q = p.quad(left="START",right="END",bottom=0,top=1,color='green',source=cds)

output_file("Motion_graph.html")

show(p)