#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <iomanip>
#include <stdlib.h>


// #include <vector>
// #include <list>
// #include <map>
// #include <set>
// #include <deque>
// #include <stack>
// #include <bitset>
// #include <algorithm>
// #include <functional>
// #include <numeric>
// #include <utility>
// #include <sstream>
// #include <iostream>
// #include <iomanip>
// #include <cstdio>
// #include <cmath>
// #include <cstdlib>
// #include <ctime>

//Cookie clicker alpha 2014

using namespace std;

// double cost, increase, win_amount;
int flipSize;
string s;

void processLine();
int main() {

	/**************************************/
	//input and output files:

	ifstream file("A-large.in");
	if (!file.is_open()) {
		cout << " file could not open";
		exit(0);
	}
	// ifstream file("sampe.in");
	freopen("output1large.txt","w",stdout);
	/***************************************/



	string str;
	getline(file, str);
	int numLines;
	istringstream stream_num_lines(str);
	stream_num_lines >> numLines;
	// cout << "numLines = " << numLines << endl;


	for (int i = 0; i < numLines; i++) {
		// cout << "line: " << str;
		getline(file, str);
		istringstream stream(str);
		stream >> s >> flipSize;
		// cout << "s: " << s << endl;
		cout << "Case #" << i + 1 << ": ";
		processLine();
		// cout << str << endl;
		// Process str
	}

	// while (getline(file, str))
	// {

	// }
}

bool pancakes[1000];
void displayPancakes() {
	// cout << endl << "debug cakes: ";
	for (int i = 0; i < s.length(); i++) {
		if (pancakes[i] == false)
			cout << '-';
		else
			cout << '+';
	}
	cout << endl;
}

void flipAt(int x) {
	for (int i = 0; i < flipSize; i++) {
		pancakes[x + i] = !pancakes[x + i];
	}
}

void processLine() {


	for (int i = 0; i < s.length(); i++) {
		if (s.at(i) == '-')
			pancakes[i] = false;
		else
			pancakes[i] = true;
	}

	// displayPancakes();


	int cursor = 0;
	int flipCount = 0;

	for (int i = 0; i < s.length() - flipSize+1; i++) {
		if (pancakes[i] == false) {
			flipAt(i);
			// cout << "flipping: ";
			// displayPancakes();
			flipCount++;
		}
	}

	for(int i = 0; i < s.length(); i++) {
		if(pancakes[i] == false) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}

	// cout << "flipcount : " << flipCount << endl; 
	cout << flipCount << endl; 


}