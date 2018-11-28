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
long long numStalls, numPeople;

bool bathroom[1002];

void processLine();
int main() {

	/**************************************/
	//input and output files:

	ifstream file("C-small-1-attempt0.in");
	// ifstream file("sampe.in");
	freopen("C-small-attempt0.out","w",stdout);
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
		stream >> numStalls >> numPeople;
		for (int j = 0; j < 1002; j++) {
			bathroom[j] = false;
		}
		bathroom[0] = true;
		bathroom[numStalls + 1] = true;
		cout << "Case #" << i + 1 << ": ";
		processLine();
		// cout << str << endl;
		// Process str
	}

	// while (getline(file, str))
	// {

	// }
}

bool isTidy(long long x) {

	cout << "Testing" << x << endl;
	int curDigit = x % 10;
	x /= 10;

	if (x == 0)
		return true;

	while (x > 0) {
		int prevDigit = curDigit;
		curDigit = x % 10;
		if (curDigit > prevDigit) {
			return false;
		}
		x /= 10;
	}


	return true;
}

long long leftEmpty(long long stallIndex) {

	long long distance = 0;
	for (int i = stallIndex; i > 0; i--) {
		if (bathroom[i] == false)
			distance++;
		else
			break;
	}
	return distance;
}

long long rightEmpty(long long stallIndex) {
	long long distance = 0;
	for (int i = stallIndex; i < numStalls + 1; i++) {
		if (bathroom[i] == false)
			distance++;
		else
			break;
	}
	return distance;
}
void processLine() {

	//we have numStalls and numPeople incoming

	long long bestIndex;
	long long bestMin = -1;
	long long bestMax = -1;
		// cout << "num people: " << numPeople <<  numStalls << endl;
	for (long long personX = 0; personX < numPeople; personX++) {
		bestIndex = -1;
		bestMin = -1;
		bestMax = -1;

		// cout << "placing person: " << personX << endl;

		for (long long j = 1; j < numStalls + 1; j++) {
			//compute left empty.
			//compute right empty
			//place this person

			if (bathroom[j] == true)
				continue;
			long long ls = leftEmpty(j);
			long long rs = rightEmpty(j);

			// cout << "rs: " << rs << endl;

			long long min = (ls < rs) ? ls : rs;
			long long max = (ls > rs) ? ls : rs;

			if (bestMin == -1)
				bestMin = min;
			if (bestMax == -1)
				bestMax = max;

			if (bestIndex == -1)
				bestIndex = j;

			//we want to maximize min
			if (bestMin < min) {
				bestMin = min;
				bestMax = max;
				bestIndex = j;
			}

			if (bestMin == min && bestMax < max) {
				bestMin = min;
				bestMax = max;
				bestIndex = j;
			}




		}

		// cout << "bestIndex: " << bestIndex << endl;
		// exit(0);
		bathroom[bestIndex] = true;
	}

	// int result = 1;
	// for(long long i = maxNum; i > 1; i--) {
	// 	if(isTidy(i)) {
	// 		cout << i << endl;
	// 		return;
	// 	}

	// }


	// // cout << setprecision(10) << potential_win_time << endl;
	cout << bestMax-1 << " " << bestMin-1 << endl;

}