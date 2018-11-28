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


void printCase(ll cnum, ll high, ll low) {
	//string hi = "hello";
	//DBGDO(hi);

	cout << "Case #" << cnum << ": "<< high << " " << low << endl;
}


int main() {
	ll n; 

	cin >> n;
		
	FOR(cnum, 1, n+1){
		ll N, K;
		priority_queue<ll> sizes;
		unordered_map<ll, ll> intervals;

		cin >> N >> K;


		sizes.push(N);
		intervals[N] = 1;

		while (true) {
			ll curr = sizes.top();
			sizes.pop();

			ll amount = intervals[curr];

			ll up = (curr) / 2;
			ll down = (curr - 1) / 2;

			if (amount >= K) {
				printCase(cnum, up, down);
				break;
			}
			else {
				K -= amount;
				//cerr << "used " << amount << " intervals of size " << curr << " and obtained sizes " << up << " & " << down << endl;
				if (!intervals[up]) {
					sizes.push(up);
				}
				intervals[up] = intervals[up] + amount;
				if (!intervals[down]) {
					sizes.push(down);
				}
				intervals[down] = intervals[down] + amount;
			}
		}
	}

	return 0;
}