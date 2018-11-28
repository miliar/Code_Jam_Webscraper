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

bool debugging = false;
#define DBGDO(X) ({ if(debugging) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })


void printCase(ll cnum) {
	//string hi = "hello";
	//DBGDO(hi);

	cout << "Case #" << cnum << ": ";
}

vector<double> speeds;
vector<double> maxdist;

vector<vector<double>> distances;

vector<vector<double>> shortest;
ll N, Q;

void init() {
	ll N = 100;
	speeds.assign(N, 0.0);
	maxdist.assign(N, 0.0);
	shortest.resize(N);
	distances.resize(N);

	FOR(i, 0, N) {
		shortest[i].assign(N,-1);
		distances[i].assign(N, -1);
	}
}

void findshortest(ll i) {
	double maxDist = maxdist[i];
	double speed = speeds[i];

	queue<pair<ll, double>> steps;
	steps.push(mp(i, 0.0));

	while (!steps.empty()) {
		pair<ll, double> curr = steps.front();
		steps.pop();

		ll pos = curr.xx;
		double distance_so_far = curr.yy;

		FOR(j, 0, N) {
			if (distances[pos][j] >= 0.0) {
				double dist_next = distance_so_far + distances[pos][j];
				if (dist_next > maxDist) {
					continue;
				}
				else {
					double time = dist_next / speed;
					if (shortest[i][j] <0 || shortest[i][j] > time) {
						shortest[i][j] = time;
						steps.push(mp(j, dist_next));
					}
				}
			}
		}
	}
}

void generateGraph() {
	FOR(i, 0, N) {
		findshortest(i);
	}
	//DBGDO("finished");
}

void printGraph() {
	FOR(i, 0, N) {
		FOR(j, 0, N) {
			cout << "(" << i << "," << j << ") : " << shortest[i][j] << " ; ";
		}
		cout << endl;
	}

}

double findShortestFromTo(ll source, ll target) {
	queue<pair<ll, double>> candidates;

	candidates.push(mp(source, 0.0));
	vector<double> optTime;

	optTime.assign(N, numeric_limits<double>::max());
	optTime[source] = 0;

	double minTime = numeric_limits<double>::max();


	while (!candidates.empty()) {
		pair<ll, double> curr = candidates.front();
		candidates.pop();

		ll pos = curr.xx;
		double so_far = curr.yy;

		if (pos == target) {

			//cerr << "changed? -> " << minTime << " ::: " << so_far;
			if (so_far < minTime) {
				minTime = so_far;
			}
			continue;
		}

		FOR(j, 0, N) {
			if (shortest[pos][j] >= 0.0) {
				double next_time = so_far + shortest[pos][j];
				
				if (next_time >= minTime) {
					continue;
				}
				if (next_time >= optTime[j]) {
					continue;
				}
				optTime[j] = next_time;
				//cerr << "pushed: " << j << " at " << next_time << endl;

				//DBGDO(j);
				//DBGDO(next_time);
				candidates.push(mp(j, next_time));
			}
		}

	}

	return minTime;
}

int main() {
	ll n; 

	cin >> n;
		
	FOR(cnum, 1, n + 1) {
		//if (cnum == 60) {
		//	debugging = true;
		//}

		cin >> N >> Q;
		init();
		FOR(i, 0, N) {
			double E;
			double S;

			cin >> E >> S;

			maxdist[i] = E;
			speeds[i] = S;
		}

		FOR(i, 0, N) {
			FOR(j, 0, N) {
				double dist;
				cin >> dist;
				distances[i][j] = dist;
			}
		}

		generateGraph();

		//printGraph();

		printCase(cnum);
		FOR(i, 0, Q) {

			ll U, V;

			cin >> U >> V;
			//cerr << (U-1) << " ~~~ " << (V-1) << endl;
			cout << setprecision(9) << fixed << findShortestFromTo(U-1, V-1) << " ";
		}
			
		cout << endl;
	}

	return 0;
}