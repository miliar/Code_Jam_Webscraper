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

const int size = 1000 + 23;

const int N = 4;

int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;

	int it;
	vector <pair <double, double> > h;
	cin >> it;
	for (int t = 1; t <= it; t++) {
		cout << "Case #" << t << ": ";
		int n;
		double d;
		cin >> d >> n;
		h.clear();
		for (int i = 0; i < n; i++) {
			double kk, ss;
			cin >> kk >> ss;
			h.push_back(make_pair(kk, ss));
		}
		sort(h.begin(), h.end());
		double last = 0;
		for (int i = n-1; i >= 0; i--) {
			if (last < (d - h[i].first) / h[i].second) {
				last = (d - h[i].first) / h[i].second;
			}
		}
		cout.precision(19);
		cout << d / last << endl;
	}


	return 0;
}