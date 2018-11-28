#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>

#include <string>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

#define INPUT_FILE  "c:\\cj2017\\A-large.in"
#define OUTPUT_FILE "c:\\cj2017\\A-large.out"


int main () {
	string line1;
	ifstream infile;
	infile.open(INPUT_FILE);
	ofstream outfile;
	outfile.open (OUTPUT_FILE);
	if (infile.is_open()) {
		getline (infile,line1);
		cout << line1 << cout;
		int numberOfTests = atoi(line1.c_str());


		for (int t = 1; t <= numberOfTests; t++) {

			//std::vector<int >     data;


			std::string   line;
			std::getline(infile, line);

			//std::vector<int>   lineData;
			std::stringstream  lineStream(line);

			
			string pencakes;
			lineStream >> pencakes ;
			string flipSizeStr;
			lineStream >> flipSizeStr;
			int flipSize = atoi(flipSizeStr.c_str());
			
			//int pcSize = pencakes.size();
			//char a[pcSize];
			char a[pencakes.size()+1];//as 1 char space for null is also required
			strcpy(a, pencakes.c_str());

			int flipCounter = 0;
	        bool isImpossible = false;
	        for(int i = 0; i< pencakes.length(); i++){
        	if(a[i] == '-'){
        		if ((flipSize + i -1) < pencakes.length() ) {
        	
	        		for(int j = i; j < i+flipSize; j++){
	        			if(a[j] == '-'){
	        				a[j] = '+';
	        			} else {
	        				a[j] = '-';
	        			}
	        		}
	        		flipCounter++;
	        	} else {
	        		isImpossible = true;
	        	}
        	}
        }
        
        std::ostringstream ss;
        ostringstream convert; 
        convert << flipCounter;
			outfile<< "Case #" << t << ": " << ((isImpossible) ? "IMPOSSIBLE" : convert.str()) << endl;
		}
	}

	infile.close();
	outfile.close();
	return 0;
}
