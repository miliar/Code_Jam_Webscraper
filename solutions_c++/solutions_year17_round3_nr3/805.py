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


vd p;

double prob_success() {
	double prob = 1.0;
	for (double d : p) {
		prob *= d;
	}
	return prob;
}

int main() {
	
	int t; cin >> t;
	int cas = 1;
	while (t--) {
		cout << "Case #" << cas << ": ";
		cas++;

		int n, k; cin >> n >> k;


		double u; cin >> u;

		p = vd(n, -1.0);
		for (int i = 0; i < n; i++) {
			cin >> p[i];
		}

		// make them all equal 
		sort(p.begin(), p.end());
		for (int i = 0; i < n - 1; i++) {
			double add = (p[i + 1] - p[i]) * (i + 1);
			//cout << "consuming " << add << " to equalize" << endl;
			if (add < u + EPS) {
				for (int j = 0; j <= i; j++) {
					u -= (p[i + 1] - p[j]);
					p[j] = p[i + 1];
				}
			}
			else {
				// divide remaining into all equally
				for (int j = 0; j <= i; j++) {
					p[j] += u / (i + 1);
				}
				u = 0.0;
				//cout << "DONE!  Remaining u is " << u << endl;
				break;
			}

			/*cout << "p is now: ";
			for (auto prob : p) {
				cout << prob << " ";
			}
			cout << "; remaining " << u << endl;*/
		}

		if (u > EPS) {
			//cout << "further dividing remainder" << endl;
			// divide remaining equally
			for (int i = 0; i < n; i++) {
				p[i] += u / n;
			}

			/*cout << "p is finally: ";
			for (auto prob : p) {
				cout << prob << " ";
			}
			cout << "; remaining " << u << endl;*/
		}


		cout << fixed << setprecision(7) << prob_success() << endl;
	}
	return 0;
}