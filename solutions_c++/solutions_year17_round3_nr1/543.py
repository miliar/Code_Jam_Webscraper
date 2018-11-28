#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <iomanip>

#define IN_FILE "A-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

pair< pair<ld, int>, int > pnk[1003];
set< pair< pair<ld, int>, int > > pset;

ld LPI = 3.1415926535897932384626433;

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
		pset.clear();
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> pnk[i].first.second >> pnk[i].first.first;
			pnk[i].first.first = 2 * LPI*pnk[i].first.first*pnk[i].first.second;
			pnk[i].second = i;
			pset.insert(pnk[i]);
		}
		ld ans = -1;
		for (int i = 0; i < n; i++) {
			pset.erase(pnk[i]);
			ld tmpans = LPI*pnk[i].first.second*pnk[i].first.second;
			tmpans += pnk[i].first.first;
			int cnt = 1;
			auto rit = pset.rbegin();
			while (rit != pset.rend()&&cnt<=k-1) {
				if (rit->first.second <= pnk[i].first.second) {
					cnt++;
					tmpans += rit->first.first;
				}
				rit++;
			}
			if (ans == -1 || ans < tmpans)
				ans = tmpans;
			pset.insert(pnk[i]);
		}
		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
