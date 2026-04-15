<<<<<<< Updated upstream
=======
# KiCAD Setup

This is written with the assumption that the user has a basic understanding of KiCAD and already has made a PCB in the program. Your PCB should be made and ready to go when starting this guide.

## Getting Started

To get this started you'll need:

- Your PCB File
- KiCAD (any version) installed 
- The 'Converter Tool' folder with all content 
- KiCAD.py downloaded

## File Setup

The setup here is easy. As of right now, this is what has been working for me. I believe there is a spot to better position the PCB for the Converter Tool, but I have not found it (better detail in [notes](#Notes)). <br>

The best away to position your PCB is at the top left of the workspace, with its bottom-left corner touching the top-left corner of the workspace's square. This aligns things at 0,0 and makes it easy for the csv to be right with the positions. Doesn't need to be perfect, we can fix things with calibration, just get the PCB edge as close as possible without going over.

![Binary Counter in KiCAD file](/Files/images/binarycounter.jpg)

## Exporting

With your PCB in the correct spot, you can now export. <br><br>

To do this:

1. Click *File*
2. Go to *Fabrication Outputs*
3. Set an output directory
4. Select *Component Placement (.pos)*
5. Under *Format* select 'csv'
6. Under *Units* select 'millimeters'
7. Under *Files* select 'Separate files for front, back'
8. Make sure 'Include only SMD footprints' and 'Use drill/place file origin' are checked
9. Click 'Generate Position File'

You should now have two files generated, one front file, and one back file. Depending on what you are populating you may only need the front file to run. You can now continue to the python tool.

![KiCAD export window](/Files/images/kicadexport.png)<br>
(ignore the SMD box not being checked, I'll fix this later)

## Python Tool

For the Converter Tool to properly read your csv in, there needs to be some changes made to it to get the correct output. The image below shows the correct formatting of a csv.

Running it is simple, you don't need to run a Python shell, you can just run it from the program itself. Make sure your newly generated csv's are in the same folder and double click the script. It'll walk you through choosing your file and naming it for an export, just remember to include '.csv' in your file names.  

The Python script attached that will do this for you (from KiCAD export, doesn’t work with other programs). <br>
![Sample CSV Setup](/Files/images/csv.png)

## Notes

I haven't played around with the KiCAD setup too much, the only thing I've noticed with having the PCB placed where it is is that the voltage regulators are off by a rotation of 180 degrees, everything else seems to be fine. These all can and will be fixed in the Converter Tool, just be vigilant and check tape setup and rotation in the tool.
>>>>>>> Stashed changes
