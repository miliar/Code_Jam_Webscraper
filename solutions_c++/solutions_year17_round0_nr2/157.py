#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
ll N;
int n, a[30], suf[30];
void trans(ll N) {
	n = 0;
	while (N > 0) {
		a[n++] = N % 10;
		N /= 10;
	}
	reverse(a, a + n);
}
ll solve() {
	ll ret = 0, x;
	bool flag = true;
	rep(i, 0, n) {
		if (i && a[i - 1] > a[i]) {
			flag = false;
			break;
		}
		if (i == 0 || a[i - 1] < a[i]) {
			x = 0, --a[i];
			rep(j, 0, i + 1)
				x = x * 10 + a[j];
			rep(j, i + 1, n)
				x = x * 10 + 9;
			++a[i];
			ret = max(ret, x);
		}
//		rep(j, 0, n)
//			printf("%d", a[j]);puts("");
	}
	if (flag)
		ret = N;
	return ret;
}
int main() {
	freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	rep(cas, 0, T) {
		cin >> N;
		trans(N);	
		cout << "Case #" << cas + 1 << ": " << solve() << endl;
	}
	return 0;
}
