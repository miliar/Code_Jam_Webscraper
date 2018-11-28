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
#include <math.h>

//Cookie clicker alpha 2014

using namespace std;

// double cost, increase, win_amount;
unsigned long long maxNum;

void processLine();
int main() {

	/**************************************/
	//input and output files:

	ifstream file("../B-large.in");
	// ifstream file("sampe.in");
	freopen("output2large.txt","w",stdout);
	/***************************************/



	string str;
	getline(file, str);
	int numLines;
	istringstream stream_num_lines(str);
	stream_num_lines >> numLines;
	// cout << "numLines = " << numLines << endl;


	for(int i = 0; i < numLines; i++) {
		// cout << "line: " << str;
		getline(file,str);
		istringstream stream(str);
		stream >> maxNum;
		cout << "Case #" << i+1 << ": ";
		processLine();
		// cout << str << endl;
		// Process str
	}

	// while (getline(file, str))
	// {
		
	// }
}

long long isTidy(unsigned long long x) {

	// cout << "Testing" << x << endl;
	int curDigit = x % 10;
	x/=10;
	int counter = 0;
	int digits[20]; //

	digits[0] = curDigit;

	if(x == 0)
		return -1;

	while(x > 0) {
		curDigit = x % 10;
		x/=10;
		counter++;
		digits[counter] = curDigit;
		// int prevDigit = curDigit;
		// curDigit = x % 10;
		// if(curDigit > prevDigit) {
		// 	return false;
		// }
		// x/=10;
	}

	for(int i = counter; i > 0; i--) {
		int nextDigit = digits[i-1];
		curDigit = digits[i];
		if(nextDigit < curDigit) {
			int numConsec = 0;

			for(int j = i; j > 0; j--) {
				int nextNextDigit = digits[j-1];
				if(nextNextDigit == nextDigit) {
					// cout << "nextNextDigit" << nextNextDigit << endl;
					
					numConsec++;
				} else {
					break;
				}
			}
			// cout << "i-numConsec: " << i-numConsec << endl;

			long long powResult = 1;
			int power = i-numConsec-1;
			if(power == 0)
				return 1;
			if(power == 1)
				return 10;

			for(int k = 0; k < power; k++) {
				powResult *= 10;
				// cout << " pow result: " << powResult << endl;
			}
			// cout << " returning pow result: " << powResult << endl;
			return powResult;
			// return (long long) pow(10,i-numConsec);
		}
	}


	return -1;
}

void processLine() {
	int result = 1;
	for(long long i = maxNum; i > 1; i--) {
		long long tidyOffset = isTidy(i);
		if(tidyOffset == -1) {
			cout << i << endl;
			// exit(0);
			return;
		} else {
			// cout << "subbing: " << tidyOffset << endl;
			if(tidyOffset < 0) {
				// cout << "PROBLEM" << endl;
				exit(0);
			}
			long long oldi = i;
			i-= tidyOffset;
			i++;

			// cout << "oldi: " << oldi << endl << "newi: " << i-1 << endl;

			// if(oldi < i) {
			// 	cout << "oldi" << endl;
			// }
		}

	}


	// cout << setprecision(10) << potential_win_time << endl;
	cout << 1 << endl;


}