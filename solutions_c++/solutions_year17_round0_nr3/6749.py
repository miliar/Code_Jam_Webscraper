#include <bits/stdc++.h>

#define pii pair <int, int>
#define pll pair <ll, ll>
#define rep(i, n) for (long long i = 0; i < (long long)n; i++)
#define REP(i, n, m) for (long long i = (long long)n; i < (long long)m; i++)
#define prep(i, n) for (long long i = 1; i <= (long long)n; i++)
#define per(i, n) for (long long i = n; i >= 0; i--)
#define pb push_back
#define vi vector <int>
#define vl vector <ll>
#define vvi vector <vector <int> >
#define vvl vector <vector <ll> >
#define fi first
#define se second
#define mp make_pair


typedef long long ll;
typedef long double ld;


using namespace std;

ifstream fin("C-small-1-attempt0.in");
ofstream fout("ans.txt");

int main() {
	int t;
	fin >> t;
	rep(i, t) {
		fout << "Case #" << i + 1 << ": ";
		int n, k;
		fin >> n >> k;
		bool a[n + 2];
		fill (a, a + n + 2, false);
		a[0] = true;
		a[n + 1] = true;
		rep (j, k) {
			pii temp[n + 2];
			for (int j2 = 1; j2 < n + 1; ++j2) {
				int l = n + 2;
				int r = 0;
				for (int i2 = 0; i2 < n + 2; ++i2) {
					if (a[i2]  && i2 < j2) {
						l = i2;
					}
					if (a[i2] && i2 > j2) {
						r = i2;
						break;
					}
				}
				temp[j2] = {j2 - l - 1, r - j2 - 1};
			}
			int idx = -1;
			for (int i2 = 1; i2 < n + 1; ++i2) {
				//cout << temp[i2].fi << " " << temp[i2].se << endl;
				if (!a[i2] && (idx == -1 || min(temp[idx].fi, temp[idx].se) <  min(temp[i2].fi, temp[i2].se ))) {
					idx = i2;
					continue;
				}
				if (!a[i2] && (idx == -1 || min(temp[idx].fi, temp[idx].se) ==  min(temp[i2].fi, temp[i2].se) && max(temp[idx].fi, temp[idx].se) <  max(temp[i2].fi, temp[i2].se))) {
					idx = i2;
					continue;
				} 
			}
			//cout << endl << endl;
			a[idx] = true;
			if (j + 1 == k) {
				fout << max(temp[idx].fi, temp[idx].se) << " " << min(temp[idx].fi, temp[idx].se) << endl;
			}
		}
	}
	return 0;
}

