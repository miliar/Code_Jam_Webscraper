#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000;

const int N = 4;
const double Pi = acos(-1);

vector <double> h;
vector <double> r;
vector <pair <double, int> > crem;


int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;

	int t;
	cin >> t;
	for (int it = 1; it <= t; it++) {
		cout << "Case #" << it << ": ";
		int k;
		h.clear();
		r.clear();
		crem.clear();
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			double rr, hh;
			cin >> rr >> hh;
			h.push_back(hh);
			r.push_back(rr);
		}
		for (int i = 0; i < n; i++) {
			crem.push_back(make_pair(2 * Pi * r[i] * h[i], i));
		}
		sort(crem.begin(), crem.end());
		reverse(crem.begin(), crem.end());
		// for (int i = 0; i < n; i++) {
		// 	cerr << crem[i].first << "   " << crem[i].second << endl;
		// }
		double ans = 0;
		// cerr << "k = " << k << endl;
		for (int i = 0; i < n; i++) {
			double loc_ans = Pi * r[i]*r[i] + 2 * Pi * r[i] * h[i];
			int loc_k = k - 1;
			for (int j = 0; j < n; j++) {
				if (loc_k == 0) {
					if (loc_ans > ans) {
						ans = loc_ans;
					}
					break;
				}
				if (crem[j].second == i) {
					continue;
				}
				// cerr << "loc_ans = " << loc_ans << endl;
				// cerr << "loc_k = " << loc_k << endl << endl;
				loc_ans += crem[j].first;
				loc_k--;
				// cerr << "loc_ans = " << loc_ans << endl;
				// cerr << "loc_k = " << loc_k << endl << endl;
			}
			if (loc_ans > ans)
				ans = loc_ans;
		}
		cout.precision(30);
		cout << ans << endl;
	}

	return 0;
}