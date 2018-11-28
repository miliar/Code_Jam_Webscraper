#include <bits/stdc++.h>                 // [PRIMES]               1777 ~2^10.80
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <cassert>
using namespace std;         //                       10333 ~2^13.33
using ll = long long;
using vll = vector<ll>;
using pll = pair<ll,ll>;

const double eps = 1e-9;                
#define all(c) begin(c),end(c)          
#define mp make_pair                    
#define mt make_tuple                  
#define pb push_back                    
#define eb emplace_back                 
#define xx first                      
#define yy second                       
#define has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (int i=(a); i<(b); i++)       
#define FORD(i,a,b) for (int i=int(b)-1; i>=(a); i--)
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })


void printCase(ll cnum) {
	//string hi = "hello";
	//DBGDO(hi);

	cout << "Case #" << cnum << ": ";
}

ll N, R, O, Y, G, B, V;

unordered_map<char, bool> printed;

void printComplement(char color) {
	switch (color) {
	case 'R':
		FOR(i, 0, G) {
			cout << "GR";
		}
		break;
	case 'B':
		FOR(i, 0, O) {
			cout << "OB";
		}
		break;
	case 'Y':
		FOR(i, 0, V) {
			cout << "VY";
		}
		break;
	}
}

void printCol(char color) {
	cout << color; 
	//cerr << "printed? " << color << ": " << printed[color] << endl;
	if(!printed[color]){
		printed[color] = true;
		printComplement(color);
	}
}

int main() {
	ll n;
	cin >> n;
		
	FOR(cnum, 1, n + 1) {
		printed['R'] = false;
		printed['B'] = false;
		printed['Y'] = false;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		printCase(cnum);
		if (R == G && R + G == N) {
			FOR(i, 0, G) {
				cout << "GR";
			}
			cout << endl;
			continue;
		}
		if (B == O && B + O == N) {
			FOR(i, 0, O) {
				cout << "BO";
			}
			cout << endl;
			continue;
		}
		if (Y == V && Y + V == N) {
			FOR(i, 0, V) {
				cout << "YV";
			}
			cout << endl;
			continue;
		}
	
		R -= G;
		Y -= V;
		B -= O;
		if (R <= 0 && G > 0 || Y <= 0 && V > 0 || B <= 0 && O > 0) {
			goto impossible;
		}
		
		char maxCol, medCol, minCol;
		ll maxCount, medCount, minCount;

		if (R > Y && R > B) {
			maxCol = 'R';
			maxCount = R;

			if (Y > B) {
				medCol = 'Y';
				medCount = Y;

				minCol = 'B';
				minCount = B;
			}
			else {
				minCol = 'Y';
				minCount = Y;

				medCol = 'B';
				medCount = B;
			}
		}
		else {
			if (B > Y) {
				maxCol = 'B';
				maxCount = B;

				if (Y > R) {
					medCol = 'Y';
					medCount = Y;

					minCol = 'R';
					minCount = R;
				}
				else {
					minCol = 'Y';
					minCount = Y;

					medCol = 'R';
					medCount = R;
				}
			}
			else {
				maxCol = 'Y';
				maxCount = Y;

				if (B > R) {
					medCol = 'B';
					medCount = B;

					minCol = 'R';
					minCount = R;
				}
				else {
					minCol = 'B';
					minCount = B;

					medCol = 'R';
					medCount = R;
				}
			}

		}

		if (maxCount > medCount + minCount) {
			goto impossible;
		}

		while (maxCount > 1) {
			printCol(maxCol);
			maxCount--;
			if (medCount > minCount) {
				printCol(medCol);
				medCount--;
			}
			else {
				printCol(minCol);
				minCount--;
			}
		}
		printCol(maxCol);
		maxCount--;

		while (medCount > 0 && minCount >0) {
			printCol(medCol);
			printCol(minCol);
			minCount--;
			medCount--;
		}
		if (medCount > 0) {
			printCol(medCol);
		}

		cout << endl;
		continue;

		impossible:
		cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}