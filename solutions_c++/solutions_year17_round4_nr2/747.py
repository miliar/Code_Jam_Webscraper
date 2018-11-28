#include <bits/stdc++.h>
#define ll long long
using namespace std;
int n,m,p,c;
int P[1001],B[1001];
void solve() {
	cin >> n >> c >> m;
	for (int i=0;i<1001;i++) P[i] = 0;
	for (int i=0;i<1001;i++) B[i] = 0;
	int maxv = 0;
	for (int i=0;i<m;i++) {
		int x,y;
		cin >> x >> y;
		P[x]++;
		B[y]++;
		if (P[x] > maxv) maxv = P[x];
	}
	int ans = 0;
	if (B[1] > B[2]) ans = B[1];
	else ans = B[2];
	if (P[1] >= ans) {
		cout << P[1] << " 0" << endl;
		return;
	}
	if (maxv <= ans) {
		cout << ans << " 0" << endl;
		return;
	}
	cout << ans << " " << maxv - ans << endl;
	return;
}
int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}