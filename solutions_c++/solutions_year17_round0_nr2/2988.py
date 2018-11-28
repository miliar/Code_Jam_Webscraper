#include <bits/stdc++.h>                 // [PRIMES]               1777 ~2^10.80
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <cassert>
using namespace std;                     //                       10333 ~2^13.33
const double eps = 1e-9;                 //                100200400777 ~2^36.54
#define all(c) begin(c),end(c)           //              10200300500777 ~2^43.21
#define mp make_pair                     //             100200300400777 ~2^46.51
#define mt make_tuple                    //            1200300400600999 ~2^50.09
#define pb push_back                     //           10200300400600111 ~2^53.18
#define eb emplace_back                  //          100200300400600333 ~2^56.48
#define xx first                         //         1200300400500800999 ~2^60.06
#define yy second                       
#define has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (int i=(a); i<(b); i++)       
#define FORD(i,a,b) for (int i=int(b)-1; i>=(a); i--)
										 /// ({ ... }) avoids some problems: http://kernelnewbies.org/FAQ/DoWhile0
										 /// In non-contest code it is probably better to use: do { ... } while(0)
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

int checkInc(string& num) {

	int len = num.length();

	char curr = '0';
	FOR(i, 0, len) {
		if (num[i] >= curr) {
			curr = num[i];
		}
		else {
			return i;
		}
	}
	return -1;
}

void printCase(int cnum, string& num) {
	//string hi = "hello";
	//DBGDO(hi);

	cout << "Case #" << cnum << ": ";

	bool hasStarted = false;
	FOR(i, 0, num.length()) {
		
		if (!hasStarted && num[i] != '0') {
			hasStarted = true;
		}

		if (hasStarted) {
			cout << num[i];
		}
	}
	cout << endl;
}

void correctFor(string& num, int startoff) {

	assert(startoff > 0);
	FOR(i, startoff, num.length()) {
		num[i] = '9';
	}

	while (startoff >= 1) {
		//cerr << num[startoff - 1] << endl;
		if (num[startoff - 1] == '0') {
			num[startoff - 1] = '9';
			startoff--;
			continue;
		}
		else {
			num[startoff - 1]--;
			if (startoff == 1) {
				break;
			}
			else {
				if (num[startoff - 1] >= num[startoff - 2]) {
					break;
				}
				else {
					continue;
				}
			}
		}
	}
	//cerr << "num: " << num << endl;
}

int main() {
	int n; 

	cin >> n;
		
	FOR(cnum, 1, n+1){
		string num;

		cin >> num;
		//cerr << num.length() << endl;

		while (true) {
			int res = checkInc(num);
			//DBGDO(res);
			if (res < 0) {
				//cerr << "test";
				printCase(cnum, num);
				break;
			}
			else {
				correctFor(num, res);
			}
		}
	}

	return 0;
}