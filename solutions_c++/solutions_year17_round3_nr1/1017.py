#include <iostream>
//#include <conio.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <stdlib.h>
#include <ctime>
#define _USE_MATH_DEFINES
#include <cmath>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
#include <bitset>
//#include <sstream>
//#include <iomanip>
using namespace std;
typedef long long ll;
const ll mod = 1000000007;
const int inf = 1000000006;
const ll INF = 1000000000000000000;
#define y1 jghrdtslgblrsdjg
#define y0 shgeupisrhgasdfg
#define j1 hufvhvuifgragresgse

int r[1005], h[1005];

bool cmp(long long a, long long b) {
	return a > b;
}

bool next_combination(vector<int> & a, int n) {
	int k = (int)a.size();
	for (int i = k - 1; i >= 0; --i)
		if (a[i] < n - k + i + 1) {
			++a[i];
			for (int j = i + 1; j<k; ++j)
				a[j] = a[j - 1] + 1;
			return true;
		}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> r[i] >> h[i];
		long double res = 0;
		for (int i = 0; i < n; i++) {
			vector<long long> p;
			for (int j = 0; j < n; j++)
				if (i != j && r[j] <= r[i])
					p.push_back((long long)r[j] * h[j]);
			if (p.size() < k - 1)
				continue;
			sort(p.begin(), p.end(), cmp);
			long double ans = 0;
			for (int i = 0; i < k - 1; i++)
				ans += p[i];
			ans *= (long double)M_PI * 2;
			ans += (long double)M_PI * 2 * r[i] * h[i];
			ans += (long double)M_PI * r[i] * r[i];
			res = max(res, ans);
		}
		/*
		vector<int> v;
		for (int i = 1; i <= k; i++)
			v.push_back(i);
		long double res3 = 0;
		do {
			long double rmax = 0;
			long double res2 = 0;
			for (int i = 0; i < k; i++) {
				res2 += (long double)M_PI * 2 * r[v[i] - 1] * h[v[i] - 1];
				rmax = max(rmax, (long double)r[v[i] - 1]);
			}
			res2 += (long double)M_PI * rmax * rmax;
			res3 = max(res3, res2);
		} while (next_combination(v, n));
		if (abs(res3 - res) > 1e-6) {
			cout << ' ' << res3 << endl << ' ' << res << ' ' << abs(res3 - res) << ' ' << t << endl;
			//return 0;
		}*/

		cout.precision(30);
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}