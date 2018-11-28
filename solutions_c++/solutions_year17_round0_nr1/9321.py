#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

int unHappy(string S) {
	for(int i = 0; i < S.size(); i++) {
		if(S.at(i) == '-') {
			return i;
		}
	}
	return -1;
}

string UseFlipper(string pancakes, int flipperSize) {
	int numPancakes = pancakes.size();
	int FirstUnhappyIndex = unHappy(pancakes);
	
	
	
		for(int i = FirstUnhappyIndex; i < (FirstUnhappyIndex + flipperSize); ++i) {
			
			if(pancakes.at(i) == '+') {
				pancakes.at(i) = '-';
			}
			else {
				pancakes.at(i) ='+';
			}
		}
	
	return pancakes;
}

string Reduce(string pancakes) {
	if(pancakes.find('-') != string::npos) {
		return pancakes.substr(pancakes.find('-'));
	}
	return "";
}

int Flip(string pancakes, int flipperSize) {
	int count = 0;
	int index = unHappy(pancakes);
	
	while(index != -1) { //check if there is any 0
		if((flipperSize > (pancakes.size())) || ((index + flipperSize) > pancakes.size())){ 
			return -1;
		}
		pancakes = UseFlipper(pancakes, flipperSize); 
		pancakes = Reduce(pancakes);
		count++;
		
		index = unHappy(pancakes);
		
	}
	return count;

}

 

int main() {
	int NumTests = 0;
	string testcase;
	string input;
	string pancakes;
	int flipperSize = 0;
	int flips = 0;
	
	getline(cin,input);
	
	NumTests = atoi( input.c_str() );
	
	
	
		for(int i = 1; i <= NumTests; i++) {
			getline(cin, testcase);
			
			for(int j = 0; j < testcase.size(); j++) {
				if(testcase.at(j) == ' ') {
					pancakes = testcase.substr(0, j);
					flipperSize = atoi( testcase.substr(j + 1, testcase.size() - j - 1).c_str() );
				}
			}

			flips = Flip(pancakes, flipperSize);
			//cout << "P: " << pancakes << " f: " << flipperSize;
			if (flips > -1) {
				cout << "Case #" << i << ": " << flips << endl;
				
			}
			else {
			
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				
		}
		
	}

}