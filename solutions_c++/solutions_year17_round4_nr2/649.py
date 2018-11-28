#include <bits/stdc++.h>
#define ll long long
#define mk make_pair
using namespace std;
 
const int N = 1e3 + 5;
const int mod = 1e9 + 7;
const int inf = 1e9;

int n, m, c, p[N], b[N];
int cntc[N], cntp[N], ans;

bool check(int x) {
	ans = 0;
	int sum = 0;
	for (int i = 1; i <= n; i++) {
		if (cntp[i] > x) {
			ans += cntp[i] - x; // cout << "/";
		//
		}
		sum += cntp[i];
		if (sum > i * x) return 0;
	}
	return 1;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d", &n, &c, &m);
		int l = 0, r;
		for (int i = 1; i <= max(n, c); i++) cntc[i] = cntp[i] = 0;
		for (int i = 1; i <= m; i++) {
			scanf("%d %d", p + i, b + i);
			cntp[p[i]]++;
			cntc[b[i]]++;
			l = max(l, cntc[b[i]]);
		}  //for (int i = 1; i <= n; i++) cout << cntp[i] << "/";
		r = 1e6;  //check(2);  cout << "??????";
		while (l < r) {
			int mid = l + r >> 1;
			if (check(mid)) r = mid;
			else l = mid;
			if (l + 1 == r) {
				if (check(l)) r--;
				else l++;
			}
		}
		check(l);
		printf("Case #%d: %d %d\n", ++cas, l, ans);
	}
}
