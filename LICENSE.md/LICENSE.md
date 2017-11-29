#======================================================================#
#                          Christianah Adigun                          #
#                          adigu002@d.umn.edu                          #

#                           INSTRUCTION MANUAL                         #

#    A Step by step guide to creating hashes with my                   #
#            NSC (Not-So-Craptographic) Hash function.                 #
#======================================================================#

----------------------------------------
Linux Terminal Command Line Arguments
----------------------------------------
Q. How to hash the input of a single file
python hash.py DIR_PATH/YOUR_FILE_NAME

Q. How to create a log where the lines alternate between two slightly different orig and mod files:
$ rm LOG_FILE; for I in $(seq start end); do python hash.py DIR_PATH/orig/$I >> LOG_FILE; python hash.py DIR_PATH/mod/$I >> LOG_FILE; done

----------------------------------------
IDLE Environment arguments
----------------------------------------

Q. How to hash the input of a single file
	o Open the file hash.py with IDLE
	o Select "Run" and click "Run Module"
	o >>> chash('DIR_PATH/YOUR_FILE_NAME')

The output of the hashed text is a 32-bit hex value. This algorithm has been analyzed based on the following critera:
	o Uniform distribution of outputs
	o Strict Avalanche Criterion (SAC): two inputs that differ by one or more bits should have “completely unrelated” hash outputs (all bits change with P(0.48), which is the equivalent of a new random bitstring).
	o Collision resistance
	o Preimage resistance
  
  
  
----------------------------------------
Evaluating hash results
----------------------------------------
All values of input files can be written to a log file.
The script evaluate.py analyzes each hex value for all inputs.

On Linux:
	o Run from the terminal
	  python evaluate.py LOG_FILE
	o The program writes values of average ratio of 1s in Columns to CSV file :: columns.csv
	o The program writes values of differences to CSV file :: differences.csv


On Windows:
	o Open the file evaluate.py with IDLE
	o Select "Run" and click "Run Module"
	o Type evaluate('LOG_FILE') and press enter key
	o The program writes values of average ratio of 1s in Columns to CSV file :: columns.csv
	o The program writes values of differences to CSV file :: differences.csv
