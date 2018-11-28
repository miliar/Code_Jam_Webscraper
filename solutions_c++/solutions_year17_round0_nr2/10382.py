#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <set>
#include <cstring>
#include <sstream>

using namespace std;

bool isTidy(double num) {
	//cout << strlen(num) << endl;
	stringstream ss;
	ss << num;
	string str = ss.str();
	for (unsigned int i = 0; i < str.size(); i++)
	{
		if (i == str.size()- 1) {
			return true;
		}
		if ((int)(str[i]-'0') > (int)(str[i+1]-'0')) {
			//cout << num[i] << " " << num[i+1] << endl;
			return false;
		}
	}
}

int lastTidy(char num[]) {
	double number = atof(num);
	for (double i = number; i > 0; i--) {
		if (isTidy(number)) return number;
		number--; 
	}
}

int main() {
    ifstream myReadFile;
 	myReadFile.open("B-small-attempt1.in");

 	ofstream myfile;
    myfile.open ("tidyNumbersAnswer.txt");
    //myfile << "Writing this to a file.\n";

 	char output[100];
 	int i = 0;
 	int input;
 	if (myReadFile.is_open()) {
	 	while (!myReadFile.eof()) {
		    myReadFile >> output;
		    if (i == 0) {
		    	input = atoi(output);
			}
	 		if (i == input + 1) break;
		    
		    if (i != 0) {
		    	myfile << "Case #" << i << ": ";
		    	myfile << lastTidy(output);
		    	if (i != input) myfile << endl;
		    
			    //call function
		    }
	    	//cout << output << endl;
	    	i++;
	 	}
	}
	myReadFile.close();
    myfile.close();
  	return 0;
}