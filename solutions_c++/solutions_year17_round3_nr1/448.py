#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define uint unsigned int
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

using namespace std;

int n, k;

void solve() {
	cin >> n >> k;
	vector<pair<int, int> > v;
	for (int i = 0; i < n; i++) {
		pair<int, int> pr;
		cin >> pr.first >> pr.second;
		v.push_back(pr);
	}
	sort(v.begin(), v.end());
	double opt = 0;
	for (int i = n - 1; i >= 0; i--) {
		double tmp = PI * v[i].first * 1.0 * v[i].first + 2.0 * PI * v[i].first * 1.0 * v[i].second;
		vector<double> h;
		for (int j = 0; j < i; j++)
			h.push_back(2.0 * PI * v[j].first * 1.0 * v[j].second);
		sort(h.begin(), h.end());
		for (int j = h.size() - 1, cnt = 0; j >= 0 && cnt < k - 1; j--, cnt++) {
			tmp += h[j];
		}
		opt = max(opt, tmp);
	}
	cout << fixed << setprecision(9) << opt << endl;
}

int main() {
	int t, i;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
