#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;
#define lli long long int
const int N = 1e8;
lli t[N];
 
int main() {
    ios_base::sync_with_stdio();
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		memset(t, 0, N*sizeof(lli));
		cout << "Case #" << (qq + 1) << ": ";
		lli n, k;
		cin >> n >> k;
		lli ans = n;
		map<lli, lli> m;
		m[n] = 1;
		bool second = true;
		while (m.size()) {
			pair<lli, lli> it = *m.rbegin();
			ans = it.first / 2;
			if (it.first & 1) {
				if (ans < N) t[ans] += 2 * it.second;
				else m[ans] += 2 * it.second;
				second = 0;
			}
			else {
				if (ans < N) t[ans] += it.second;
				else m[ans] += it.second;
				--ans;
				if (ans < N) t[ans] += it.second;
				else m[ans] += it.second;
				second = 1;
			}
			k -= it.second;
			m.erase(--m.end());
			if (k <= 0) break;
		}
		for (int i = N - 1; i && k > 0; --i) {
			if (t[i]) {
				k -= t[i];
				ans = i / 2;
				if (i & 1) { t[ans] += 2 * t[i]; second = 0; }
				else {
					t[ans] += t[i];
					--ans;
					t[ans] += t[i];
					second = 1;
				}
			}
		}
		cout << (ans + (second ? 1 : 0)) << ' ' << ans << endl;
	}
    return 0;
}