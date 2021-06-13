## gcode to dxf

#load modules
import ezdxf
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
gfilename = filedialog.askopenfilename(filetypes=(('gcode','*.gcode'),('all files','*.*')))

#open gcode file
gcode = open(gfilename, "r")

points = []
glines = []
#clean gcode to xy coordinates

lines = gcode.readlines()

#find only lines which have G1 header
for line in lines:
	if line.split(" ")[0] == 'G1' and line.find('F') < 0:
		a = line.split(" ")[1:3]
		glines.append(a)
#		print(a)

	
for gline in glines:
	x = float(gline[0].split("X")[1])
	y = float(gline[1].split("Y")[1])
	points.append([x,y])

#setup dxf file
doc = ezdxf.new()
msp = doc.modelspace()
#doc.units = units.mm

#create dxf
msp.add_lwpolyline(points)

#save as dxf
gsave = filedialog.asksaveasfilename(filetypes=(('dxf','*.dxf'),('all','*.*')))
doc.saveas(gsave)

#close text file
gcode.close
