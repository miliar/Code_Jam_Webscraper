#pragma warning (disable:4996)

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

////

//A
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-l.out", "w", stdout);

	int t, cas = 1;
	cin >> t;
	while (t--) {
		string s;
		int k;
		cin >> s >> k;
		int n = (int)s.length();
		int ans = 0;
		for (int i = 0; i <= n - k; i++) {
			if (s[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++) {
					s[i + j] = (s[i + j] == '+' ? '-' : '+');
				}
			}
		}
		for (int i = n - k + 1; i < n; i++) {
			if (s[i] == '-') {
				ans = -1;
				break;
			}
		}
		cout << "Case #" << cas++ << ": ";
		if (ans >= 0) cout << ans << endl;
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}


//B
//bool check(ll x) {
//	int y = 9;
//	while (x) {
//		if (x % 10 > y) return false;
//		y = x % 10;
//		x /= 10;
//	}
//	return true;
//}
//
//int main() {
//	freopen("B-large.in", "r", stdin);
//	freopen("B-l.out", "w", stdout);
//
//	int t, cas = 1;
//	cin >> t;
//	while (t--) {
//		ll n;
//		cin >> n;
//		int m = log10(n);
//		ll d = 10;
//		ll x = n;
//		if (!check(x)) {
//			for (int i = 0; i < m; i++) {
//				x = (n / d - 1) * d + (d - 1);
//				if (check(x)) break;
//				d *= 10;
//			}
//		}
//		cout << "Case #" << cas++ << ": " << x << endl;
//	}
//	return 0;
//}