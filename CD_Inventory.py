#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AHernandez, 2021-Mar-05, Added code to CD class, Getters and Setters.  
# AHernandez, 2021-Mar-06, Added Exeption handeling on several IO methods  

#------------------------------------------#
import pathlib
# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
strErrorType= ''
blnErrorflag = False

class CD:
    """Stores data about a CD:
    
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def __init__(self,cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, new_cd_id):
        if type(new_cd_id) == int:
            self.__cd_id = new_cd_id
        else:
            raise Exception('You must enter a base 10 Integer')
    
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, new_cd_title):
        if type(new_cd_title) == str:
            self.__cd_title = new_cd_title
        else:
            raise Exception('You must enter a string')
            
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, new_cd_artist):
        if type(new_cd_artist) == str:
            self.__cd_artist = new_cd_artist
        else:
            raise Exception('You must enter a string')

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod

    def apend_inventory(strID, strTitle, strArtist, lst_Inventory):
        """Function to Apend a new entry to the inventory

        Args:
            strID (string): ID for the new CD added to the inventory
            strTitle (string):Title for the new CD added to the inventory
            strArtist (string):Artist for the new CD added to the inventory
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None.
        """
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lst_Inventory.append(dicRow)
        
    # TODO Add code to process data from a file        
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D list
        (list of dicts) list one line in the file represents one dictionary row in list.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            error_type (string): returns the class name of the error that was thrown
        """
        lst_Inventory.clear()  # this clears existing data and allows to load data from file
        error_type = ''
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                lst_Inventory.append(dicRow)
            objFile.close()
        except Exception as e:
            error_type = e.__class__.__name__
        return error_type 
       
    # TODO Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D list
        (list of dicts) list one line in the file represents one dictionary row in list.

        Args:
            file_name (string): name of file used to write the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            error_type (string): returns the class name of the error that was thrown 
        """
        error_type = ''
        try:
            objFile = open(file_name, 'w')
            # for row in lstTbl:
            for row in lst_Inventory:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        except Exception as e:
            error_type = e.__class__.__name__
        return error_type 


# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    """displays data and prompts about the CD inventory program:
    
    properties:
        none.
    methods:
        print_menu(): -> None
        file_status(strFileName): -> None  
        menu_choice(): -> choice
        show_inventory(lst_Inventory): -> None
        showload_inventory(): -> strYesNo
        showadd_inventory(): -> strID, strTitle, strArtist,error_type,error_flag  
        error_status(error_type): -> None
        
    """
    # TODO add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod         
    def file_status(strFileName):
        """Displays a status if the file exists in the directory 


        Args:
            strFileName(string) The CD inventory text file name

        Returns:
            None.

        """
        print('The File {} does not exists!'.format(strFileName))
        print('\n') 
        

    # TODO add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Function to get user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODO add code to display the current data on screen
    @staticmethod
    def show_inventory(lst_Inventory):
        """Function to Display current inventory lst_Inventory
        
        Args:
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        if not lst_Inventory:
            print('The Inventory is currently empty \n')
        else:
            for row in lst_Inventory:
                print('{}\t{} (by: {})'.format(*row.values()))
        print('======================================\n')
        

    @staticmethod
    def showload_inventory():
        """Display the messages when loading the inventory from a file.
        
        Args:
            None.

        Returns:
            strYesNo (string): User input to check if users want to continue loading file.

        """

        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
        return strYesNo

    # TODO add code to get CD data from user
    @staticmethod    
    def showadd_inventory(): 
        """Displays the User Input Questions for adding a new CD to the inventory

        Args:
            showadd_inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            strID (int): CD Id to add to the inventory
            strTitle(string):Title to add to the inventory
            strArtist(string): Artist to add to the inventory
            error_type (string): returns the class name of the error that was thrown
            error_flag (bool): returns false if user enters not int to strID
        """
        error_type =''
        strID = -1
        strTitle =''
        strArtist =''
        error_flag = False
        while not error_flag:
            try:
                strID = int(input('Enter ID: '))
                strTitle = input('What is the CD\'s title? ').strip()
                strArtist = input('What is the Artist\'s name? ').strip()
                error_type =''
                error_flag = True
                break
            except Exception as e:
                error_type = e.__class__.__name__
                error_flag = False
                break
        return strID, strTitle, strArtist,error_type,error_flag

    @staticmethod         
    def error_status(error_type):
        """Displays error messages depending on the error class name 


        Args:
            error_type (string): This is the class name in string form


        Returns:
            None.

        """
        if error_type == 'FileNotFoundError':
            print('The File {} does not exists!'.format(strFileName))
            print('\n') 
        elif error_type == 'ValueError':
            print('The Value entered is not an integer base 10')

# -- Main Body of Script -- #
# TODO Add Code to the main body

# Load data from file into a list of CD objects on script start
file = pathlib.Path(strFileName)
if file.exists():
    FileIO.load_inventory(strFileName, lstOfCDObjects)
else:
    IO.file_status(strFileName)
while True:
    
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()   

    # let user exit program
    if strChoice == 'x':
        break

    # let user load inventory from file    
    elif strChoice == 'l':

        if file.exists():

            strYesNo = IO.showload_inventory()
                
            if strYesNo.lower().strip() == 'yes':
                print('reloading...')
                FileIO.load_inventory(strFileName, lstOfCDObjects)
                IO.error_status(strErrorType)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
  
            IO.show_inventory(lstOfCDObjects)
        
        else:
            IO.file_status(strFileName)
                    
        continue # start loop back at top.
        
    # let user add data to the inventory        
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        while True:
            str_id, str_title, str_artist,strErrorType,blnErrorflag = IO.showadd_inventory()
            if str_id == -1:
                IO.error_status(strErrorType)
            else:
                cd = CD(str_id, str_title, str_artist)
                FileIO.apend_inventory(cd.cd_id, cd.cd_title, cd.cd_artist, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
                break
            # 3.3.2 Add item to the list
        continue  # start loop back at top.
        
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            IO.error_status(strErrorType)
            print(f"The inventory has been saved to file {strFileName}")
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('Invalid option was selected')        










