#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>

#define IN_FILE "A-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		int cnt[4] = { 0,0,0,0 };
		int n,p;
		cin >> n >> p;
		for (int i = 0; i < n; i++) {
			int g;
			cin >> g;
			cnt[g%p]++;
		}
		ll ans = cnt[0];
		if (p == 2) {
			ans += (cnt[1] >> 1) + (cnt[1] & 1);
		}
		else if (p == 3) {
			int cancel = min(cnt[1], cnt[2]);
			cnt[1] -= cancel;
			cnt[2] -= cancel;
			ans += (cnt[1] / 3) + ((cnt[1] % 3)>0);
			ans += (cnt[2] / 3) + ((cnt[2] % 3) > 0);
			ans += cancel;
		}
		else if (p == 4) {
			int cancel = min(cnt[1], cnt[3]);
			cnt[1] -= cancel;
			cnt[3] -= cancel;
			ans += cancel;
			ans += (cnt[2] / 2);
			cnt[2] = (cnt[2] & 1);
			if (cnt[1]) {
				int pack = cnt[1] / 4;
				cnt[1] -= (pack * 4);
				ans += pack;
				if (!cnt[2])
					ans += (cnt[1] > 0);
				else {
					if (!cnt[1])
						ans++;
					else if (cnt[1] == 3)
						ans += 2;
					else
						ans++;
				}
			}
			else if (cnt[3]) {
				int pack = cnt[3] / 4;
				cnt[3] -= (pack * 4);
				ans += pack;
				if (!cnt[2])
					ans += (cnt[3] > 0);
				else {
					if (!cnt[3])
						ans++;
					else if (cnt[3] == 3)
						ans += 2;
					else
						ans++;
				}
			}
			else if (cnt[2])
				ans++;
		}
		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
