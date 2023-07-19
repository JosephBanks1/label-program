# take in info from closed workbooks
# populate the tables in the data tab with the info from closed workbooks (MAL)
# clear buttons clear all data in form fill area
# print buttons print selected label area to current selected printer
# Menu button returns screen to menu
# all tabs except for the one bening used are hidden
# COMING FROM VBA- MODULES MAY NOT NEED TO BE SEPERATED
# MIL= master item list data
# MAL= master address list data

"""
FORMS
menu
buttons: 8 labels 
logo up top and desc next to button
label 1
-4 input fields: 2 inputs (item number,machine) and 2 dependents from data (plant(sp,ct,pf,rn,mi,ml,ky), copies
buttons:clear, print, menu, next
-reference box beside label w/ item type: (data from MIL)
-info line on bottom(L to R):plant-machine, current date, alt lookups, website(genovapipe.com)
 
label 2
buttons:clear, print, menu
label 3
buttons:clear, print, menu
label 4
buttons:clear, print, menu
label 5
buttons:clear, print, menu
label 6
buttons:clear, print, menu
label 7
buttons:clear, print, menu
label 8 (SHEET 10(LABEL 8))
DONE -9 input fields: 4 inputs (Genova order number, pkg, weight, customer order number) and 5 dependents from data (plant(sp,ct,pf,rn,mi,ml,ky), pkg type, ship via, customer, location( dependent of customer))
# when address is selected populate dependent dropdown list without empty spaces
# customer list refreshes with a list of unique names only (pulls from data tab, but populates from outside workbooks) when first opened
# dependent list refreshes from MAL when new name is selected
# if no location options then default address gets populated
buttons:clear, print, menu
"""



"""
#Module 1- button functions
DONE -clear label
print label 

change image on label 1 based on input file
refresh image everytime a new item number is loaded
"""


"""
#Module 2- creates barcodes for box labels
-if theres an error move on to the next one
-screen updates with everychange
-takes in the upc
-calcluates check didgit for 11 digit number
-calculates check digit for 13 digit number
-displays barcode and upc digits

auto hides all sheets except the menu
"""



"""
#Module 3
-open master item list- this is to establish the link for the box labels
-close master item list
-open master address list- this is to establish the link for the address labels
-close master address list

unlock the DATA tab
-populate "customers" in the correct table on the DATA tab and change the size of the table to match the current number of customers in that table
-popupalte "locations" in the correct table on the DATA tab and change the size of the table to match the current number of customers in that table
-lock the DATA tab
-refresh the locations dependent list 
"""


