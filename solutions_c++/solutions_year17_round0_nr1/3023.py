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
										 /// ({ ... }) avoids some problems: http://kernelnewbies.org/FAQ/DoWhile0
										 /// In non-contest code it is probably better to use: do { ... } while(0)
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })


void printCase(ll cnum, ll turns) {
	//string hi = "hello";
	//DBGDO(hi);

	cout << "Case #" << cnum << ": ";

	if (turns >= 0) {
		cout << turns;
	}
	else {
		cout << "IMPOSSIBLE";
	}
		
	cout << endl;
}


int main() {
	ll n; 

	cin >> n;
	char comb = '-' + '+';
		
	FOR(cnum, 1, n+1){
		string s;
		ll K;

		cin >> s >> K;

		ll turns = 0;

		FOR(i, 0, s.length() - K + 1) {
			//cerr << s << endl;
			if (s[i] != '+') {
				turns++;
				FOR(j, i, i + K) {
					s[j] = comb - s[j];
				}
			}
		}
		//cerr << s << endl;

		bool good = true;
		FOR(i, s.length() - K + 1, s.length()) {
			if (s[i] != '+') {
				good = false;
				break;
			}
		}

		if (good) {
			printCase(cnum, turns);
		}
		else {
			printCase(cnum, -1);
		}
	}

	return 0;
}