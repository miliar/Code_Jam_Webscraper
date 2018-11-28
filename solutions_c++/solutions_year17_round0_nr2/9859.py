/*
 ============================================================================
 Name        : problem_b_tidy_numbers.cpp
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C++,
 ============================================================================
 */

#include <iostream>
#include <string>
using namespace std;

string getTidy(string N){
	string retVal;
	size_t len = N.size();
	size_t curPos;
	size_t nextPos;

	if ( len ){
		retVal = N;
		// start at last digit
		curPos = len - 1;
		do{
			if ( curPos ){
				nextPos = curPos - 1;
				if ( N.at(curPos) < N.at(nextPos) ){
					// next digit higher than current

					// so back to highest possible here and afterwards
					retVal.replace(curPos, len - curPos, len - curPos, '9');
					// and next one downwards in original
					N.replace(nextPos, 1, 1, N.at(nextPos) - 1);
				}
				else{
					retVal.replace(curPos, 1, 1, N.at(curPos));
				}
			}
			else{
				retVal.replace(curPos, 1, 1, N.at(curPos));
			}
		} while (curPos--);
		// erase leading Zeros
		while ( retVal.at(0) == '0' ){
			retVal.erase(0,1);
		}
	}
	return retVal;
}


int main(void) {
	int t;
	string N;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> N;  // read N
		cout << "Case #" << i << ": " << (getTidy(N)) << endl;
	}
	return 0;
}


