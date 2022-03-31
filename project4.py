#-------------------------------------------------------------------------------
# FILE NAME:      project4.py
# DESCRIPTION:    uses python3 to create and use databases
# USAGE:          python3 project4.py
#                 python3 project4.py < PA4_test.sql
# notes:          can run program manually or with test script
#                 Project 4 is a continuation of projects 1,2,&3
#
# MODIFICATION HISTORY
# Author               Date           version
#-------------------  ------------    ---------------------------------------
# Annette McDonough   2021-09-17      1.0 first version 
# Annette McDonough   2021-09-18      1.1 adding make directory function
# Annette McDonough   2021-09-20      1.2 finally got create directory to work
# Annette McDonough   2021-09-21      1.3 working on drop directory
# Annette McDonough   2021-09-22      1.4 drop directory now works
# Annette McDonough   2021-09-23      1.5 working on use
# Annette McDonough   2021-09-24      1.6 working on create table
# Annette McDonough   2021-09-25      1.7 table is finally working
# Annette McDonough   2021-09-25      1.8 starting drop table 
# Annette McDonough   2021-09-25      1.9 working on select
# Annette McDonough   2021-09-26      2.0 cleaning up code
# Annette McDonough   2021-09-27      2.1 adding more comments
# Annette McDonough   2021-10-06      2.2 starting project 2
# Annette McDonough   2021-10-07      2.3 working on whereS
# Annette McDonough   2021-10-08      2.4 adding tableS
# Annette McDonough   2021-10-09      2.5 modifiying selectT
# Annette McDonough   2021-10-10      2.6 starting insertT
# Annette McDonough   2021-10-11      2.7 fixed bug in insertT
# Annette McDonough   2021-10-12      2.8 starting deleteT
# Annette McDonough   2021-10-13      2.9 working on deleteT
# Annette McDonough   2021-10-15      3.0 attempting update table 
# Annette McDonough   2021-10-16      3.1 working on bugs
# Annette McDonough   2021-10-17      3.2 fixed huge bug that had infinate loop
# Annette McDonough   2021-10-17      3.3 working on comments
# Annette McDonough   2021-10-18      3.4 finishing up comments
# Annette McDonough   2021-10-28      3.5 starting in on proj3 w/ joins
# Annette McDonough   2021-10-29      3.6 working on inner join
# Annette McDonough   2021-10-31      3.7 starting on left outer join
# Annette McDonough   2021-11-01      3.8 debugging left outter join
# Annette McDonough   2021-11-01      3.9 Left outer join working!!!
# Annette McDonough   2021-11-06      4.0 adding more comments and cleaning up
# Annette McDonough   2021-11-09      4.1 Starting on begin transaction function
# Annette McDonough   2021-11-10      4.2 working on temp function to hold values 
# Annette McDonough   2021-11-15      4.3 working on commit function
# Annette McDonough   2021-11-16      4.4 using traceback to find bugs
# Annette McDonough   2021-12-03      4.5 cleaning up code and comments
#-----------------------------------------------------------------------------

# using python libraries
import os  
import sys
import traceback


# creating a directory
dbDirectory = ""

#------------------------------------------------------------------------------------------
# FUNCTION:     createDb(userI)
# DESCRIPTION:  Creates a database
# notes:        used Geeks for Geeks to understand how to create a directory
#-----------------------------------------------------------------------------------------
def createDb(userI):
    
    try:
        dbName = userI.split(" ")[3]
        # if directory doesn't exist create it
        if not os.path.isdir(dbName):
            os.mkdir(dbName)
            print("Database " + dbName + " created")
        else:
            print("Failed to create database " + dbName + " because it exists already")
    except:
        print("Command is invalid")


#-----------------------------------------------------------------------------------------
# FUNCTION:       dropDb(userI)
# DESCRIPTION:    deletes a database
# notes;          https://www.geeksforgeeks.org/python-os-path-isdir-method/
#----------------------------------------------------------------------------------------
def dropDb(userI):
    
    global dbDirectory

    try:
        # split and grab the 3rd word "db_?"
        dbName = userI.split(" ")[3]
        # if the database exists remove it
        if os.path.isdir(dbName):
            os.system("rm -r " + dbName)
            print("Database " + dbName + " deleted")
            if dbName == dbDirectory:
                dbDirectory = ""
        else:
            print("!Failed to delete " + dbName + " because it does not exists.")
    except:
        print("Invalid command.")

#---------------------------------------------------------------------------------------
# FUNCTION:        useDb(userI)
# DESCRIPTION:     Allows user to use the databases created
# notes:           https://www.geeksforgeeks.org/python-os-path-isdir-method/
#---------------------------------------------------------------------------------------
def useDb(userI):
    
    global dbDirectory
    
    try:
        # split and grab 2nd word "db_?"
        dbName = userI.split(" ")[2]
        if os.path.isdir(dbName):
            dbDirectory = dbName
            print("using database " + dbDirectory + ".")
        else:
            print("!Failed to use database " + dbName + " because it does not exist.")
    except:
        print("Invalid command.")

#---------------------------------------------------------------------------------------
# FUNCTION:        createT(userI)
# DESCRIPTION:     creates a table in a database
# notes:           https://www.geeksforgeeks.org/python-os-path-isfile-method/
#                  https://www.w3schools.com/python/python_file_handling.asp
#                  https://www.geeksforgeeks.org/os-module-python-examples/
#---------------------------------------------------------------------------------------
def createT(userI):

    global dbDirectory

    if dbDirectory != "":
        try:
            # split and grab 3rd word "tbl_?"
            tName = userI.split(" ")[3]
            tName = tName.split("(")[0]
            fName = os.path.join(dbDirectory, tName)
            if not os.path.isfile(fName):
                with open(fName, "w") as table:
                    print("Table " + tName + " created.")
                    if "(" in userI:
                        # remove brackets
                        dataI = userI.split("(", 1)[1]
                        dataI = dataI.rsplit(")", 1)[0]
                        dataI = " " + dataI
                        # storing vars in database
                        for x in range(dataI.count(",") + 1):
                            dataI2 = dataI.split(",")[x]
                            # remove white space
                            while ") " in dataI2 or ") " in dataI2 or "( " in dataI2 or ") " in dataI2:
                                dataI2 = dataI2.replace(" )", ")")
                                dataI2 = dataI2.replace(") ", ")")
                                dataI2 = dataI2.replace("( ", "(")
                                dataI2 = dataI2.replace(" (", "(")
                            if x in range(dataI.count(",")):
                                # adding in |
                                dataI2 = dataI2 + " |"
                            # ignore spaces, end line, carriage returns, tabs.
                            while "  " in dataI2 or "\t" in dataI2 or "\n" in dataI2 or "\r" in dataI2:
                                userI = userI.replace("  ", " ")
                                userI = userI.replace("\r", " ")
                                userI = userI.replace("\t", " ")
                                userI = userI.replace("\n", " ")
                            table.write(dataI2,)
            else:
                print("!Failed to create table " + tName + " because it already exists")
        except:
            print("Invalid command.")
    else:
        print("ERROR.")


#-------------------------------------------------------------------------------------------------------
# FUNCTION:      dropT(userI)
# DESCRIPTION:   drops a table from a database
# notes:         https://www.tutorialspoint.com/python3/os_listdir.htm
#-----------------------------------------------------------------------------------------------------
def dropT(userI):
    
    global dbDirectory

    if dbDirectory != "":
        try:
            # grab third word in split "db_?"
            tName = userI.split(" ")[3]
            for tName2 in os.listdir(dbDirectory):
                # force letters to uppercase
                if tName2.upper() == tName.upper():
                    tName = tName2
            fName = os.path.join(dbDirectory, tName)
            # If file name exists remove it
            if os.path.isfile(fName):
                os.system("rm " + fName)
                print("Table " + tName + " Deleted.")
            else:
                print("!Failed to delete " + tName + " because it does not exist.")
        except:
            print("Invalid command.")
    else:
        print("ERROR.")

#--------------------------------------------------------------------------------------------------
# FUNCTION:     fileS(fName)
# DESCRIPTION:  grabs a table 
# notes:        https://www.geeksforgeeks.org/python-os-path-isfile-method/
#               https://www.w3schools.com/python/python_file_handling.asp
#-------------------------------------------------------------------------------------------------
def fileS(fName):
    #open file for table
    with open(fName, "r") as table:
        dataI = table.read()
        while "'" in dataI: 
            dataI = dataI.replace("'", "")
        print(dataI)

#-------------------------------------------------------------------------------------------------
# FUNCTION:     insertT(userI)
# DESCRIPTION:  inserts records into a table
# notes:        https://docs.python.org/3/library/stdtypes.html
#------------------------------------------------------------------------------------------------
def insertT(userI):
    global dbDirectory
    if dbDirectory != "":

        try:
            # split user input and grab 3rd word
            tName = userI.split(" ")[3]
            for tName2 in os.listdir(dbDirectory):
                if tName2.upper() == tName.upper():
                    tName = tName2
            fName = os.path.join(dbDirectory, tName)
            if os.path.isfile(fName):
                with open(fName, "a") as table:
                    if "(" in userI:
                        # remove the ( and )
                        dataI = userI.split("(", 1)[1]
                        dataI = dataI.rsplit(")", 1)[0]
                        dataI = " " +  dataI
                        table.write("\n")
                        line = ""
                        for x in range(dataI.count(",") + 1):
                            dataI2 = dataI.split(",")[x]
                            if x in range(dataI.count(",")):
                                # add | to the line to print
                                line += dataI2 + " | "
                            else:
                                line += dataI2
                        # take care of white space
                        while("  " in line or "\n" in line or "\r" in line or "\t" in line
                                or " (" in line or "( " in line or " )" in line or ") " in line):
                            line = line.replace("  ", " ")
                            line = line.replace("\n", " ")
                            line = line.replace("\r", " ")
                            line = line.replace("\t", " ")
                            line = line.replace(" (", "(")
                            line = line.replace("( ", "(")
                            line = line.replace(" )", ")")
                            line = line.replace(") ", ")")
                        # write line to table
                        table.write(line)
                print("1 new record inserted")
            else:
                print("Failed to insert into table " + tName + " because it doesn't exist")
        except:
            print("Invalid command")
    else:
        print("ERROR")


#------------------------------------------------------------------------------------------------
# FUNCTION:     deleteT(userI)
# DESCRIPTION:  deletes a record from a table
# notes:        https://docs.python.org/3/library/asyncio-stream.html
#-----------------------------------------------------------------------------------------------
def deleteT(userI):
    global dbDirectory
    # initialive var to 0
    dataI = 0
    if dbDirectory != "":
        try:
            # split and grab 3rd word
            tName = userI.split(" ")[3]
            for tName2 in os.listdir(dbDirectory):
                if tName2.upper() == tName.upper():
                        tName = tName2
            fName = os.path.join(dbDirectory, tName)
            dataI2 = ""
            # open file path with filename
            if os.path.isfile(fName):
                    with open(fName, "r") as table:   
                        tLine = table.readline()
                        dataI2 = tLine
                        nums = tLine.split(" ")
                        whereNum = userI.split(" ")[5]
                        whereCount = -1
                        for x in range(0, tLine.count("|") + 1):
                            if whereNum == nums[3 * x + 1]:
                                whereCount = x
                        tLine = table.readline()
                        dataI2 = dataI2.replace("  ", " ")
                        while tLine != "":
                            nums = tLine.split("|")
                            nums[len(nums) - 1] += " "
                            nums[len(nums) - 1] = nums[len(nums) - 1].replace("  ", " ")
                            nums[len(nums) - 1] = nums[len(nums) - 1].replace("\n", " ")
                            # for loop to replace space with no space
                            for x in range(0, len(nums)):
                                nums[x] = nums[x].replace(" ", "")
                            if not(("=" in userI.split(" ")[6] and (userI.split(" ")[7] == nums[whereCount]))
                                    or (">" in userI.split(" ")[6] and (float(nums[whereCount]) > float(userI.split(" ")[7])))
                                    or ("<" in userI.split(" ")[6] and (float(nums[whereCount]) < float(userI.split(" ")[7])))):
                                        dataI2 += tLine            
                            else:
                                # increment dataI 
                                dataI += 1
                            nums[len(nums) - 1] = nums[len(nums) - 1].replace("  ", " ")
                            tLine = table.readline()
                    with open(fName, "w") as table:
                        # while there is a double space replace with single space
                        while "  " in dataI2:
                            dataI2 = dataI2.replace("  ", " ")
                        if dataI2.rsplit("\n", 1)[1] == "":
                            dataI2 = dataI2.rsplit("\n", 1)[0]
                        # write data to table
                        table.write(dataI2)
                    # choose plural or single word
                    if dataI == 1 or dataI == 0:
                        print(dataI, "record deleted")
                    else:
                        print(dataI, "records deleted")

        except:
            print("invalid command")
    else:
        print("ERROR")

#---------------------------------------------------------------------------------------------------
# FUNCTION:     updateT
# DESCRIPTION:  updates records in a table
# notes:        https://docs.python.org/3/library/asyncio-stream.html
#--------------------------------------------------------------------------------------------------
def updateT(userI):
    global dbDirectory
    global var

    if dbDirectory != "":
        
        try:
            tName = userI.split(" ")[2]
            # flag to modify file 
            if var == 1:
                tempF(userI)
            # lock the table flag
            elif var == 0:
                print("ERROR: Table ", tName, "is locked!")
            elif var == 2:
                for tName2 in os.listdir(dbDirectory):
                    if tName2.upper() == tName.upper():
                        tName = tName2
                fName = os.path.join(dbDirectory, tName)
                dataI2 = ""
                modified = 0
                if os.path.isfile(fName):
                    # open  file and read in file
                    with open(fName, "r") as table:
                        tLine = table.readline()    
                        dataI2 = tLine
                        nums = tLine.split(" ")
                        setNum = userI.split(" ")[4]
                        whereNum = userI.split(" ")[8]
                        setCount = -1
                        whereCount = -1
                        # use for loop to check for x
                        for x in range(0, tLine.count("|") + 1):   
                            if setNum == nums[3 * x + 1]:
                                setCount = x
                            if whereNum == nums[3 * x + 1]:
                                whereCount = x
                        tLine = table.readline()
                        dataI2 = dataI2.replace("  ", " ")
                        # while tLine != "" take care of \n and extra spaces
                        while tLine != "":
                            nums = tLine.split("|")
                            nums[len(nums) - 1] += " "
                            nums[len(nums) - 1] = nums[len(nums) - 1].replace("  ", " ")
                            nums[len(nums) - 1] = nums[len(nums) - 1].replace("\n", " ")
                            for x in range(0, len(nums)):
                                nums[x] = nums[x].replace(" ", "")
                            # split and replace space with no space 
                            userI2 = userI.split(" ")[10].replace(" ", "")
                            # split and replace \n with no space
                            userI2 = userI.split(" ")[10].replace("\n", "")

                            # updated condition for project 4 
                            if(("=" in userI.split(" ")[9] and (userI2 == nums[whereCount]))
                                or (">" in userI.split(" ")[9] and (float(nums[whereCount]) > float(userI.split(" ")[10])))
                                or ("<" in userI.split(" ")[9] and (float(nums[whereCount]) < float(userI.split(" ")[10])))):
                                # split and grab 6th word and assign to nums[]
                                nums[setCount] = userI.split(" ")[6]
                                tLine = " "
                                for x in range(0, len(nums)):
                                    if x != len(nums) - 1:
                                        tLine += nums[x] + " | "
                                    else:
                                        tLine += nums[x] + "\n"
                                dataI2 += tLine
                                # increment counter
                                modified += 1
                            else:
                                dataI2 += tLine
                            # replace double space with single space
                            nums[len(nums) - 1] = nums[len(nums) - 1].replace("  ", " ")
                            tLine = table.readline()
                            dataI2 = dataI2.replace("  ", " ")
                    with open(fName, "w") as table:
                        while "  " in dataI2:
                            dataI2 = dataI2.replace("  ", " ")
                        if dataI2.rsplit("\n", 1)[1] == "":
                            dataI2 = dataI2.rsplit("\n", 1)[0]
                        table.write(dataI2)
                    # print plural or single use
                    if modified == 1 or modified == 0:
                        print(modified, "record modified")
                    else:
                        print(modified, "records modified")
        except:
            # using taceback function to trace entries
            traceback.print_exc()
            print("invalid command")
    else:
        print("ERROR")

#--------------------------------------------------------------------------------------------------
# FUNCTION:     tempF(useI)
# DESCRIPTION:  stores a record until the lock is gone and can the update
# notes:        Using flags as a lock
#-------------------------------------------------------------------------------------------------
def tempF(userI):
    global dbDirectory
    global var

    if dbDirectory != "" and var == 1 and userI != "":
        try:
            fName = os.path.join(dbDirectory, "TempFile")
            ## create file if it doesn't exist
            if not os.path.isfile(fName):
                # open file and write to it
                with open(fName, "w") as table:
                    table.write(userI +"\n")
            # if file exist open file and write
            elif os.path.isfile(fName):
                with open(fName, "a") as table:
                    table.write(userI + "\n")

        except:
            print("Invalid command.")
    else:
        print("ERROR.")

#-------------------------------------------------------------------------------------------------
# FUNCTION:     beginTrans(userI)
# DESCRIPTION:  finds the processing thread and starts the locking process
# notes:        https://docs.python.org/3/library/traceback.html
#               https://docs.python.org/3/library/os.html
#------------------------------------------------------------------------------------------------
def beginTrans(userI):
    global dbDirectory
    global var

    if dbDirectory != "":
        try:
            # print start of transaction
            print(" Transaction starts.")
            # create a temp file
            tName = "tempFile.txt"
            # create file path
            fName = os.path.join(dbDirectory, tName)
            # if file doesn't exist create it
            if not os.path.isfile(fName):
                # open file then write to it
                with open(fName, "w") as table:
                    # write lock table to file
                    table.write("Lock file \n")
                    # get process ID
                    pid = os.getpid()
                    # write process ID to file
                    table.write(str(pid))
                # allow to be modified
                var = 1
            else:
                # flag to not modify
                var = 0
        except:
            # using traceback 
            traceback.print_exc()
            print("Invalid command.")
    else:
        print("ERROR.")

#-------------------------------------------------------------------------------------------------
# FUNCTION:     commitTrans(userI)
# DESCRIPTION:  checks conditions to see if file can be modified or locked  
# notes:        https://www.geeksforgeeks.org/traceback-in-python/
#-------------------------------------------------------------------------------------------------
def commitTrans(userI):
    global dbDirectory
    global var

    if dbDirectory != "":

        try:
            if var == 0:
                print("Transaction abort.")
            elif var == 1:
                # update var
                var = 2
                tempName = os.path.join(dbDirectory, "TempFile")
                # check to see if file exists
                if os.path.isfile(tempName):
                    with open(tempName, "r") as table:
                        for line in table:
                            # force to upper
                            if " UPDATE" in line.upper():
                                # call update
                                updateT(line)
                # check to see if file is there
                if os.path.isfile(tempName):
                    # remove file
                    os.system("rm " + tempName)
                fName = os.path.join(dbDirectory, "tempFile.txt")
                # check to see if file exists if so remove it
                if os.path.isfile(fName):
                    os.system("rm " + fName)
                print("Transaction committed.")
                # reset var
                var = 0


        except:
            # use traceback to print exception along with stack entries
            traceback.print_exc()
            print("invalid command.")
    else:
        print("ERROR.")
    

#-------------------------------------------------------------------------------------------------
# FUNCTION:     tableS(fName, userI)
# DESCRIPTION:  will return data from a given table  
# notes:        added in for project 2
#-------------------------------------------------------------------------------------------------
def tableS(fName, userI):
    # group names
    gName = userI.split("select")[1]
    gName = gName.split("from")[0]
    gSubset = gName.split(",")
    whereCount = []
    # open file and read it in
    with open(fName, "r") as table:
        tLine = table.readline()
        tLine2 = tLine
        nums = tLine.split(" ")
    
        for x in gSubset:
            for y in range(0, tLine.count("|") + 1):
                if x.rsplit() == nums[3 * y + 1].rsplit():
                    whereCount.append(y)
        if "WHERE" in userI.upper():
            whereNum = userI.split(" ")[-3]
            nums = tLine.split(" ")
            index = -1
            # use for loop and check for x
            for x in range(0, tLine.count("|") + 1):
                if whereNum == nums[3 * x + 1]:
                    index = x
            nums = tLine.split("|")
            print(nums[whereCount[0]].replace("  "," ").replace("\n", ""), end=' ')
            for x in range(1, len(whereCount)):
                print("|", nums[whereCount[x]].replace("  ", " ").replace("\n", ""), end=' ')
            print("")
            tLine = table.readline()
            while tLine != "":
                while "'" in tLine:
                    tLine = tLine.replace("'", "")
                nums = tLine.split("|")
                # parse through and print records/tuples
                if (("=" in userI.split(" ")[-2] and (userI.split(" ")[-1].rsplit() == nums[index].rsplit()) 
                    and not ("!=" in userI.split(" ")[-2]))
                    or ("!=" in userI.split(" ")[-2] and (userI.split(" ")[-1].rsplit() != nums[index].rsplit()))
                    or ("<" in userI.split(" ")[-2] and (float(nums[index]) < float(userI.split(" ")[-1])))
                    or (">" in userI.split(" ")[-2] and (float(nums[index]) > float(userI.split(" ")[-1])))):
                    print("", nums[whereCount[0]].split()[0], end=' ')
                    # check for x
                    for x in range(1, len(whereCount)):
                        print("|", nums[whereCount[x]].split()[0], end=' ')
                    print("")
                tLine = table.readline()
        else:
            nums = tLine.split("|")
            print(nums[whereCount[0]].replace("  ", " ").replpace("\n", ""), end=' ')
            for x in range(1, len(whereCount)):
                print("|", nums[whereCount[x]].replace("  ", " ").replace("\n", ""), end=' ')
            print("")
            # read in line assign to tLine
            tLine = table.readline()
            # nested while loop to replace ' with nothing
            while tLine != "":
                while"'" in tLine:
                    tLine = tLine.replace("'", "")
                nums = tLine.split("|")
                print(nums[whereCount[0]].split()[0], end=' ')
                # with for loop look for x in range
                for x in range(1, len(whereCount)):
                    print("|", nums[whereCount[x]].split()[0], end=' ')
                print("")
                tLine = table.readline()


#-----------------------------------------------------------------------------------------------------------------
# FUNCTION:     whereS(fName, userI)
# DESCRIPTION:  grabs the selected records
# notes:        Returns the selected tuples/records
#---------------------------------------------------------------------------------------------------------------
def whereS(fName, userI):
    # open file
    with open(fName, "r") as table:
        tLine = table.readline()
        dataI2 = tLine
        nums = tLine.split(" ")
        whereNum = userI.split(" ")[-3]
        whereCount = -1
        # find x in range
        for x in range(0, tLine.count("|") + 1):
            if whereNum == nums[3 * x + 1]:
                whereCount = x
        # read in data
        tLine = table.readline()
        # parse through data
        dataI2 = dataI2.replace("  ", " ")
        while tLine != "":
            while "'" in tLine:
                tLine = tLine.replace("'", "")
            nums = tLine.split("|")
            nums[len(nums) - 1] += " "
            nums[len(nums) - 1] = nums[len(nums) - 1].replace("  ", " ")
            nums[len(nums) - 1] = nums[len(nums) - 1].replace("\n", " ")
            # check to see if we have an =, <, or > 
            if(("=" in userI.split(" ")[-2] and (userI.split(" ")[-1].rsplit() == nums[whereCount].rsplit()))
                    or ("<" in userI.split(" ")[-2] and (float(nums[whereCount]) < float(userI.split(" ")[-1])))
                    or (">" in userI.split(" ")[-2] and (float(nums[whereCount]) > float(userI.split(" ")[-1])))):
                    dataI2 += tLine
            nums[len(nums) - 1] = nums[len(nums) - 1].replace("  ", " ")
            tLine = table.readline()

#---------------------------------------------------------------------------------------------------
# FUNCTION:     selectT(userI)
# DESCRIPTION:  selects from table
# notes:        https://www.geeksforgeeks.org/python-os-path-isfile-method/
#               modified from project 1 and 2
#               added joins in project 3
#---------------------------------------------------------------------------------------------------
def selectT(userI):
    global dbDirectory
    if dbDirectory != "":
        
        try:
    
            if "JOIN" in userI.upper() or ("," in userI.upper() and "*" in userI.upper()):
                if "INNER JOIN" in userI.upper():
                    innerJ(userI)
                elif "LEFT OUTER JOIN" in userI.upper():
                    leftOutJ(userI)
                else:
                    normalJ(userI)

            else:
                # check to see if WHERE was entered
                if "WHERE" in userI.upper():
                    # split and grab 5th element from the end of the array
                    tName = userI.split(" ")[-5]
                
                else:
                    # split and grab last element of array
                    tName = userI.split(" ")[-1]
                for tName2 in os.listdir(dbDirectory):
                    # force to upper case
                    if tName2.upper() == tName.upper():
                        tName = tName2
                fName = os.path.join(dbDirectory, tName)
                # check to see if file exists
                if os.path.isfile(fName):
                    if not "*" in userI:
                        tableS(fName, userI)
                    elif "WHERE" in userI.upper():
                        whereS(fName, userI)
                    else:
                        fileS(fName)
                else:
                    print("!Failed to query table " + tName + " because it does not exist.")
        except:
            print("Invalid command")
    else:
        print("ERROR")


#----------------------------------------------------------------------------------------------------
# FUNCTION:      innerJ(userI)
# DESCRIPTION:   inner Joins 
# notes:         https://docs.python.org/3/library/os.path.html     
#----------------------------------------------------------------------------------------------------
def innerJ(userI):
    
    global dbDirectory

    if dbDirectory != "":
        try:
            
            # list arrays
            tList = []
            nList = []
            jList = []
            fList = []

            # uses split and stores after from
            i = userI.split("from")[1]
            # splits at on and grabs from and to on
            j = i.split("on")[0]
            # splits at inner join
            j = j.split("inner join")
                
            # appends objectsto list that are passed in 
            for x in j:
                tList.append(x.split(" ")[1])
                nList.append(x.split(" ")[2])
            # split at on and grab after
            k = i.split("on")[1]
            k = k.split("=")
            
            for x in k:
                # appends object to list
                jList.append(x.split(".")[1])
            
            for x in range(len(tList)):
                fName = os.path.join(dbDirectory, tList[x])
                fList.append(fName)
            
            # see if file exists
            if os.path.isfile(fList[0]) and os.path.isfile(fList[1]):
                with open(fList[0], "r") as table1, open(fList[1], "r") as table2:
                    dataI1 = table1.read()
                    dataI2 = table2.read()
                    # split data at newline
                    line1 = dataI1.split("\n")
                    line2 = dataI2.split("\n")
                    # array for table1 and table2 values to compare
                    num1 = []
                    num2 = []
                    
                    # split at |
                    tLine1 = line1[0].split("|")

                    # use for loop for count
                    for x in range(0, line1[0].count("|") +1):
                        if jList[0] in tLine1[x]:
                            count1 = x
                    
                    # split at |
                    tLine2 = line2[0].split("|")
                    
                    # find count
                    for x in range(0, line2[0].count("|") +1):
                        if jList[1] in tLine2[x]:
                            count2 = x
                    
                    print(line1[0] + "|" + line2[0])
                    # nested for loop to join
                    for x in range(1, len(line1)):
                        for y in range(1, len(line2)):
                            num1 = line1[x].split("|")
                            num2 = line2[y].split("|")

                            # check to see if we match and add -- and | to the line
                            if num1[count1] == num2[count2]:
                                line = "--" + line1[x] + "|" + line2[y]
                                print(line)

        except:
            print("Invalid command.")
    else:
        print("ERROR")
        
#----------------------------------------------------------------------------------------------------
# FUNCTION:      leftOutJ(userI)
# DESCRIPTION:   Left outter Joins 
# notes:         almost a complete copy paste from innerJ
#----------------------------------------------------------------------------------------------------
def leftOutJ(userI):
    global dbDirectory

    if dbDirectory != "":
        try:
            tList = []
            jList = []
            nList = []
            fList = []
            
            # uses split and stores at from and after
            i = userI.split("from")[1]
            # splits at on and grabs from and to on
            j = i.split("on")[0]
            # splits at left outer join
            j = j.split("left outer join")

            # appends objects to list that are passed in
            for x in j:
                tList.append(x.split(" ")[1])
                nList.append(x.split(" ")[2])
            
            # split at on and grab after
            k = i.split("on")[1]
            k = k.split("=")
            
            for x in k:
                # appends object to list
                jList.append(x.split(".")[1])
            
            for x in range(len(tList)):
                fName = os.path.join(dbDirectory, tList[x])
                fList.append(fName)
            
            # see if file exists
            if os.path.isfile(fList[0]) and os.path.isfile(fList[1]):
                with open(fList[0], "r") as table1, open(fList[1], "r") as table2:
                    dataI1 = table1.read()
                    dataI2 = table2.read()
                    # split at newline
                    line1 = dataI1.split("\n")
                    line2 = dataI2.split("\n")
                    # array for table1 and table2 values to compare
                    num1 = []
                    num2 = []
                 
                    # split at |
                    tLine1 = line1[0].split("|")
                    # use for loop for count
                    for x in range(0, line1[0].count("|") +1):
                        if jList[0] in tLine1[x]:
                            count1 = x
                    # split the first line at |
                    tLine2 = line2[0].split("|")
                    for x in range(0, line2[0].count("|") +1):
                        if jList[1] in tLine2[x]:
                            count2 = x

                    print(line1[0] + "|" + line2[0])
                    # nested for loop to join as suggested
                    for x in range(1, len(line1)):
                        for y in range(1, len(line2)):
                            num1 = line1[x].split("|")
                            num2 = line2[y].split("|")


                            # check to see if we match and add -- and | to the line
                            if num1[count1] == num2[count2]:
                                line = "--" + line1[x] + "|" + line2[y]
                                print(line)
                                compare = True

                        if not compare:
                            print("--" + line1[x] + "|")
                        compare = False

        except:
            print("Invalid command.")
    else:
        print("ERROR.")


#--------------------------------------------------------------------------------------------------
# FUNCTION:       normalJ(userI)
# DESCRIPTION:    does a normal join
# notes:          almost a complete copy paste from innerJ and LeftOutJ
#--------------------------------------------------------------------------------------------------
def normalJ(userI):
    global dbDirectory

    if dbDirectory != "":
    
        try:
            tList = []
            nList = []
            jList = []
            fList = []
            
            # uses split and stores after from
            i = userI.split("from")[1]
            # splits at where and grabs from and to where
            j = i.split("where")[0]
            # splits at ,
            j = j.split(",")

            # appends objects to list that are passed in 
            for x in j:
                tList.append(x.split(" ")[1])
                nList.append(x.split(" ")[2])
            # split at wher and grab after
            k = i.split("where")[1]
            k = k.split("=")
            
            for x in k:
                # appends object to list
                jList.append(x.split(".")[1])
                                                            
            for x in range(len(tList)):
                fName = os.path.join(dbDirectory, tList[x])
                fList.append(fName)
            
            # see if file exists
            if os.path.isfile(fList[0]) and os.path.isfile(fList[1]):
                with open(fList[0], "r") as table1, open(fList[1], "r") as table2:
                    dataI1 = table1.read()
                    dataI2 = table2.read()
                    # split data at newline
                    line1 = dataI1.split("\n")
                    line2 = dataI2.split("\n")
                    # array for table1 and table2 values to compare
                    num1 = []
                    num2 = []
                    
                    # split at |
                    tLine1 = line1[0].split("|")
                    # use for loop for count
                    for x in range(0, line1[0].count("|") +1):
                        if jList[0] in tLine1[x]:
                            count1 = x

                    # split at |
                    tLine2 = line2[0].split("|")

                    # find count
                    for x in range(0, line2[0].count("|") +1):
                        if jList[1] in tLine2[x]:
                            count2 = x

                    print(line1[0] + "|" + line2[0])
                    # nested for loop to join
                    for x in range(1, len(line1)):
                        for y in range(1, len(line2)):
                            num1 = line1[x].split("|")
                            num2 = line2[y].split("|")


                            # check to see if we match and add -- and | to the line
                            if num1[count1] == num2[count2]:
                                line = "--" + line1[x] + "|" + line2[y]
                                print(line)


        except:
            print("Invalid command.")
    else:
        print("ERROR")

#----------------------------------------------------------------------------------------------------
# FUNCTION:      alterT(userI)
# DESCRIPTION:   alters tables
# notes:         https://www.tutorialspoint.com/python3/os_listdir.htm
#----------------------------------------------------------------------------------------------------
def alterT(userI):

    global dbDirectory

    if dbDirectory != "":
        try:
            # grab 3rd word "tbl_?"
            tName = userI.split(" ")[3]
            # list the directories
            for tName2 in os.listdir(dbDirectory):
                # force to upper case
                if tName2.upper() == tName.upper():
                    tName = tName2
            # join the path for the table file to the database
            fName = os.path.join(dbDirectory, tName)
            dataI2 = ""
            if os.path.isfile(fName):
                # open file for read if it doesn't exist error
                with open(fName, "r") as table:
                    addL = table.readline().replace("\n", " ")
                    addL += "| " + userI.split(" ")[5] + " " + userI.split(" ")[6] + "\n"
                    dataI2 = addL
                    # read the line in and replace endlines with a space
                    addL = table.readline().replace("\n", " ")
                    while addL != "":
                        dataI2 += addL + "| none\n"
                        addL = table.readline().replace("\n", " ")
                print("Table " + tName + " modified.")
                # open file and modify it. If it doesn't exist cretae it
                with open(fName, "w") as table:
                    if dataI2.rsplit("\n", 1)[1] == "":
                        dataI2 = dataI2.rsplit("\n", 1)[0]
                    # write altered table to file
                    table.write(dataI2)
            else:
                print("!Failed to modify table " + tName + " because it does not exist.")
        except:
            print("Invalid command.")
    else:
        print("ERROR.")



#-----------------------------------------------------------------------------------------------------
# FUNCTION:     main() 
# DESCRIPTION:  programs entry point
# note:         https://www.geeksforgeeks.org/python-string-replace/
#               https://www.w3schools.com/python/ref_string_rsplit.asp
#               https://www.w3schools.com/python/ref_string_split.asp
#-----------------------------------------------------------------------------------------------------

try:
    # parse through user input
    while True:
        # get user input
        userI = " " + input("--")
        # if the user inputs \n, \t, \r, or "  " replace it with " "
        while "  " in userI or "\t" in userI or "\r" in userI or "\t" in userI:
            userI = userI.replace("  ", " ")
            userI = userI.replace("\t", " ")
            userI = userI.replace("\r", " ")
            userI = userI.replace("\n", " ")
        #if -- is input or ; then ignor as long as its not .EXIT
        while("--" in userI or not ";" in userI) and not (userI.upper() == " .EXIT"):
            if "--" in userI:
                # make sure prompt and end of statement are together
                if userI.find("--") > userI.find(";"):
                    userI = userI.rsplit("--", 1)[0]
                else:
                    userI = " " + input()
            else:
                userI += " " + input();
            # replace tabs,return carriages, endlines, spaces with single space
            while "  " in userI or "\t" in userI or "\r" in userI or "\n" in userI:
                userI = userI.replace("  ", " ")
                userI = userI.replace("\t", " ")
                userI = userI.replace("\r", " ")
                userI = userI.replace("\n", " ")

        # force input to uppercase letters
        prompt = userI.upper()
        if prompt == " .EXIT":
            print("Exiting program")
            break
               
        userI = userI.split(";")[0]
        # function calls
        # had to put a space in front to get the calls to work
        if " CREATE DATABASE " in prompt:
            createDb(userI)
      
        elif " DROP DATABASE " in prompt:
            dropDb(userI)
 
        elif " USE" in prompt:
            useDb(userI)

        elif " CREATE TABLE" in prompt:
            createT(userI)

        elif " DROP TABLE" in prompt:
            dropT(userI)

        elif " SELECT" in prompt:
            selectT(userI)

        elif " ALTER TABLE" in prompt:
            alterT(userI)

        # Added for project 2 next 3 elif's
        elif " INSERT INTO" in prompt:
            insertT(userI)

        elif " DELETE FROM" in prompt:
            deleteT(userI)

        elif " UPDATE" in prompt:
            updateT(userI)
        # added for project 4
        elif " BEGIN TRANSACTION" in prompt:
            beginTrans(userI)
        elif " COMMIT" in prompt:
            commitTrans(userI)

        else:
            print("Command not found")


except(EOFError, KeyboardInterrupt) as error:
    print("Exiting program")




