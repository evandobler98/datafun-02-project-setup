''' 
Module: Dobler Data: Delivering Baseball Insights

This module provides functions for creating a series of project folders. 
'''

import pathlib
import time 
import utils_dobler
import os



# Create a path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create new if it doesn't exist
data_path.mkdir(exist_ok=True)


'''
Create folders for a given range of years.
Arguments:
start_year -- The starting year of the range.
end_year -- The ending year of the range.
''' 


def create_folders_for_range(start_year: int, end_year: int) -> None:
    start_year = 2020
    end_year = 2023
    duration_secs = 5

    for year in range(start_year, end_year + 1 ):
        year_path = project_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
        time.sleep(duration_secs)
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")



def create_folders_from_list(folder_list: list, to_lowercase=True, remove_spaces=True) -> None:
    folder_name = ['data-csv', 'data-excel', 'data-json']
      
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        os.makedirs(folder_name, exist_ok = True)
        print(f"FUNCTION CALLED: create_folders_from_list with '{folder_name}'")




def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    folder_name = ['csv', 'excel', 'json']
    prefix = 'format-'  
    
    for folder_name in folder_list:
        new_folder_name = f"{prefix}{folder_name}"
        os.makedirs(new_folder_name, exist_ok = True)
        print(f"CREATED FOLDER: {new_folder_name}")





def create_folders_periodically(folder_count: int, duration_seconds: int) -> None:
    reg_name = "folder"
    created_folders = 0 

    while created_folders < folder_count:
        folder_name = f"{reg_name}_{created_folders + 1}"
        os.makedirs(folder_name, exist_ok = True)
        print(f"CREATED FOLDER: {folder_name}")
    
        created_folders += 1

        if created_folders < folder_count:
            time.sleep(duration_seconds)



def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("# Starting execution of main()")

    # Print get_byline() from imported module
    print(f"Byline: {utils_dobler.get_byline()}")

    # Call function 1
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 
    create_folders_periodically(folder_count = 3, duration_seconds = 5)
 
    # Call your function to test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("# Completed execution of main()")


if __name__ == '__main__':
    main()
