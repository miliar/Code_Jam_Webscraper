#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>

#define IN_FILE "C-small-1-attempt0.in"
#define OUT_FILE "out.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

ld p[52];
ld eps = 1e-12;

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(8);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		int n,k;
		ld u;
		cin >> n >> k >> u;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		p[n] = 1;
		sort(p, p + n);
		for (int focus = 1; focus <= n; focus++) {
			int cnt = focus;
			ld tgt = p[focus];
			ld costper = tgt - p[0];
			ld cost = costper*cnt;
			if (u >= cost) {
				u -= cost;
				for (int i = 0; i < cnt; i++)
					p[i] = tgt;
			}
			else {
				for (int i = 0; i < cnt; i++)
					p[i] += u/cnt;
				u = 0;
				break;
			}
		}
		ld ans = 1;
		for (int i = 0; i < n; i++)
			ans *= p[i];
		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
