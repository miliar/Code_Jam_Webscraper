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

int d, n;
double k[1000], s[1000];

void solve() {
	cin >> d >> n;
	double t = 0;
	for (int i = 0; i < n; i++) {
		cin >> k[i] >> s[i];
		t = max(t, (d - k[i]) / s[i]);
	}
	cout << fixed << setprecision(7) << d / t << endl;
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
