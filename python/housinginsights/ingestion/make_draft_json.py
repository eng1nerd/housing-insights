##########################################################################
## Summary
##########################################################################

'''
Loads our flat file data into the Postgres database
'''


##########################################################################
## Imports & Configuration
##########################################################################
#external imports
import logging
import json
import pandas as pandas
import sys

#configuration
#See /logs/example-logging.py for usage examples
logging_filename = "../../logs/ingestion.log"
logging.basicConfig(filename=logging_filename, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())     #Pushes everything from the logger to the command line output as well.

#############################
#CONSTANTS
#############################


#############################
#FUNCTIONS
#############################

def make_draft_json(csv_filename = "../data_small/example.csv", table_name = "example"): #use the name from constants as default
    '''
    Load the csv file into Pandas, use Pandas to guess the appropriate data type.
    Output a file called "table_name.json", which follows the format of meta.json
    User will run this function on a new data source, manually review the table_name.json
      and then manually copy the updated version into meta.json.

    Starter list of errors to handle:
    - file not found
    '''
    pass

    #be sure to do these transformations to create draft 'sql_name' from the 'source_name'
        #convert to lowercase
        #replace ' ' with '_'
        #replace '.' with '_'


if __name__ == '__main__':

    #use command line arguments to pass (relative) filepath and table_name.
    #we should use positional arguments in the command line
    #sys.argv is how to access command line arguments.
    for arg in sys.argv:
        print(arg)

    csv_filename = ''
    table_name = ''
    make_draft_json(csv_filename = csv_filename, table_name = table_name)

    