#include <bits/stdc++.h> 
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <cassert>
using namespace std; 
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
#define DBGDO(X) ({ if(1) //cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })


void printCase(ll case_id) {
	cout << "Case #" << case_id << ": ";
}



int main() {
	ll tc;
	cin >> tc;
		
	FOR(case_id, 1, tc + 1) {
		ll N, P;

		cin >> N >> P;

		vll group_weights;
		group_weights.assign(P, 0);
		ll total = N;

		FOR(i, 0, N) {
			ll weight;
			cin >> weight;

			group_weights[weight%P] = group_weights[weight%P] + 1;
		}
		FOR(l, 0, P) {
			//cerr << "#" << l << ": " << group_weights[l] << endl;
		}
		ll fresh = group_weights[0];
		total -= group_weights[0];
		//cerr << "initially: " << fresh << endl;
		group_weights[0] = 0;

		FOR(j, 1, P/ 2+1) {
			if (j * 2 == P) {
				ll minTot = group_weights[j] / 2;
				total -= minTot + minTot;
				fresh += minTot;
				//cerr << "after using-pairs of" << j << " & " << (j) << ": " << fresh << endl;
			}
			else {
				ll minTot = min(group_weights[j], group_weights[P - j]);
				total -= minTot + minTot;
				fresh += minTot;
				//cerr << "after using-pairs of" << j << " & " << (P - j) << ": " << fresh << endl;
				group_weights[j] -= minTot;
				group_weights[P - j] -= minTot;
			}
		}

		if (P == 3) {
			ll triples = group_weights[1] / 3 + group_weights[2] / 3;
			total -= 3 * triples;
			fresh += triples;
			group_weights[1] %= 3;
			group_weights[2] %= 3;
			//cerr << "after triples #1: " << fresh << endl;
		}
		else if (P == 4) {
			ll minTot = min(group_weights[1]/2, group_weights[2]);
			fresh += minTot;
			total -= 3 * minTot;
			//cerr << "after three-triples #1: " << fresh << endl;
			group_weights[1] -= 2 * minTot;
			group_weights[2] -= minTot;
			minTot = min(group_weights[3] / 2, group_weights[2]);
			fresh += minTot;
			total -= 3 * minTot;
			//cerr << "after three-triples #1: " << fresh << endl;
			group_weights[3] -= 2 * minTot;
			group_weights[2] -= minTot;
			fresh += group_weights[1] / 4 + group_weights[3] / 4;
			group_weights[1] %= 4;
			group_weights[3] %= 4;
			//cerr << "after 4-tuples: " << fresh << endl;
		}

		if (total > 0) {
			//cerr << "additional lucky group" << endl;
			fresh++;
		}

		/*FOR(l, 0, P) {
			//cerr << "#" << l << ": " << group_weights[l] << endl;
		}*/
		printCase(case_id);
		cout << fresh << endl;
	}


	return 0;
}