#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

#define EPS 1e-9

using namespace std;

typedef pair<int, int> ii;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef pair<ll, ll> llll;
typedef vector<llll> vllll;


int main() {

	int t; cin >> t;
	int cas = 1;
	while (t--) {
		cout << "Case #" << cas << ": ";
		cas++;

		int ac, aj; cin >> ac >> aj;
		vi cs = vi(ac, -1);
		vi ce = vi(ac, -1);
		vi js = vi(aj, -1);
		vi je = vi(aj, -1);

		for (int i = 0; i < ac; i++) {
			cin >> cs[i] >> ce[i];
		}

		for (int i = 0; i < aj; i++) {
			cin >> js[i] >> je[i];
		}

		bool poss = false;
		// brute force - try all possible 2 transfers, and if not, then 4
		for (int t1 = 0; t1 <= 719 && !poss; t1++) {
			int t2 = (t1 + 720) % 1440;

			//cout << "trying " << t1 << " - " << t2 << endl;
			bool cfirst = false;
			bool csecond = true;
			bool jfirst = false;
			bool jsecond = true;

			// check within t1 and t2
			if (ac == 0) {
				cfirst = true;
			}
			else if (t1 <= *(min_element(cs.begin(), cs.end())) && (t2 >= *(max_element(ce.begin(), ce.end())))) {
				//cout << "determined c can be first" << endl;
				cfirst = true;
			}
			if (aj == 0) {
				jfirst = true;
			}
			else if (t1 <= *(min_element(js.begin(), js.end())) && (t2 >= *(max_element(je.begin(), je.end())))) {
				//cout << "determined j can be first" << endl;
				jfirst = true;
			}

			// check if all c's fall outside of t1 and t2
			if (ac > 0) {
				for (int i = 0; i < ac; i++) {
					//cout << "checking " << cs[i] << " to " << ce[i] << endl;
					if ((ce[i] > t1 && ce[i] <= t2) || (cs[i] < t2 && cs[i] >= t1)) {
						//cout << "determined c cannot be second" << endl;
						csecond = false;
					}
				}
			}

			// check if all j's fall outside of t1 and t2
			if (aj > 0) {
				for (int i = 0; i < aj; i++) {
					if ((je[i] > t1 && je[i] <= t2) || (js[i] < t2 && js[i] >= t1)) {
						//cout << "determined j cannot be second" << endl;
						jsecond = false;
					}
				}
			}

			//cout << jfirst << " " << csecond << endl;

			if ((cfirst && jsecond) || (csecond && jfirst)) {
				//cout << "possible transitions are " << t1 << " - " << t2 << endl;
				poss = true;
			}
		}

		if (poss)
			cout << 2 << endl;
		else
			cout << 4 << endl;
	}
	return 0;
}