**Overall Objective**
To identify the layout of the chemical manufacturing industry involving different departments and to design a chemical manufacturing industry system to monitor and maintain parameters with surrounding environment.

**Specific Objectives**
Assignment Task 1
1. To monitor the parameters of input raw materials.
2. To simulate sequential flow process.
3. To account and simulate the dispatch of manufactured products.
Assignment Task 2
1. To report events to headquarters via writing to Excel file.
2. To use web publishing tools to make the system monitorable from anywhere in the world.
3. To update the price of raw materials according to the world market.

**Overal System Flow Chart**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/5b7cb16f-d852-4c80-b98c-29b0644b343a)

**Tank Filling from Absorption Tower**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/63c6484c-66a7-4a94-83d7-23c4e74f77ca)

**Acid Dispesing Flow Chart**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/042282e7-6d80-40bf-a334-d6227084b7a6)

**Fault-Reporting Flowchart**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/dd7474af-3d64-4798-91bc-08a8f67f4516)

**Data Socket Flowchart**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/95c8db5a-bdee-4b8a-9b97-364f84bcf7ef)

**Implementation**
**Front Panel**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/83c43196-e5da-4523-bc5b-3fca541d2a12)

**Main Program VI Block Diagram**
![image](https://github.com/kkimanzi/LabVIEW-Control-System-For-The-Ostwald-Process/assets/62201012/1ec758aa-d3be-4d06-ad22-24195c9f6275)


**Running Instructions**

1) the file path to the HTML was hard-coded in this.

-> To change it to your path, open the data-socket.VI as shown in video socket-change-path.mmp4

-> Change the path to match your location

-> Then save 

2) Ensure that the path to the Excel file is provided before begining the simulation.
Preferably : manually type the path to a non-existent (file shall be created automatically) on the source directory e.g C:\Users\Admin\Documents\ostwalds\source\faults.xls

The file extension should be .xls
.xlsx files require more formatting options

Check out the video walkthrough.mp4 for this
