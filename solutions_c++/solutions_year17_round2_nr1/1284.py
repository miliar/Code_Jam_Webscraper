#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

void solve() {
	ll dest, nh;
	fin >> dest >> nh;
	double res = 0;
	for (int i = 0; i < nh; i++) {
		ll cur, speed;
		fin >> cur >> speed;
		res = max(res, 1.0 * (dest - cur) / speed);
	}
	fout << fixed << setprecision(12);
	fout << dest/res << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	fin >> t;
	for (int i = 0; i < t; i++) fout << "Case #" << i+1 << ": ", solve();
}
