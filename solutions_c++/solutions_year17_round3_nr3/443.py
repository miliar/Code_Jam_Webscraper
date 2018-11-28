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
double u;

map<double, int> db;

void solve() {
	cin >> n >> k >> u;
	db.clear();
	db[1] = 1;
	for (int i = 0; i < n; i++) {
		double p;
		cin >> p;
		db[p]++;
	}
	while (u > 1e-7) {
		double min_p = db.begin()->first;
		int min_cnt = db.begin()->second;
		map<double, int>::iterator mit = db.begin();
		mit++;
		double p2 = mit->first;
		double need = (p2 - min_p) * min_cnt;
		double get = min(need, u);
		db.erase(min_p);
		db[min_p + get / min_cnt] += min_cnt;
		u -= get;
	}
	double res = 1;
	for (map<double, int>::iterator mit = db.begin(); mit != db.end(); mit++)
		for (int i = 0; i < mit->second; i++)
			res *= mit->first;
	cout << fixed << setprecision(6) << res << endl;
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
