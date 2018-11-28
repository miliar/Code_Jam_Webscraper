#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <map>
#include <string>
using namespace std;
typedef long double ld;
typedef long long ll;
typedef vector<int> vint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
#define mp(a,b)	make_pair(a,b)
#define fst	first
#define scn second
const double eps = 1e-9;

int main() {
	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int d, n;	cin >> d >> n;
		vector<int> k(n+1), s(n+1);
		for (int i = 0; i < n; i++)	cin >> k[i] >> s[i];
		double times = 0;
		for (int i = 0; i < n; i++) {
			times = max(times, (double)(d - k[i]) / s[i]);
		}
		printf("%.9lf\n", d/times);
	}
	return 0;
}