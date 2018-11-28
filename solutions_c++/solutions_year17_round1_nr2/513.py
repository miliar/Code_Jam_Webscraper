#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int N = 60;
ll L[N],R[N];
void solve() {
	int n,p;
	cin >> n >> p;
	int ans = 0;
	multiset<int> S[N];
	for (int i=0;i<n;i++) {
		int x;
		cin >> x;
		L[i] = 9*x;
		R[i] = 11*x;
	}
	for (int i=0;i<n;i++) {
		for (int j=0;j<p;j++) {
			int x;
			cin >> x;
			S[i].insert(10*x);
		}
	}
	for (int k=1;k<(1e7);k++) {
		bool ok = true;
		//cout << k << "!" << endl;
		for (int i=0;i<n;i++) {
			int x = *S[i].begin();
			if (L[i]*k > x) {
				//cout << k << " " << L[i] << " " << x << endl;
				ok = false;
				S[i].erase(x);
				k--;
				if (S[i].size() == 0) {
					cout << ans << endl;
					return;
				}
			}
			else if (x > R[i]*k) {
				ok = false;
				//cout << k << " " << R[i] << " " << x << endl;
			}
			if (!ok) break;
		}
		if (ok) {
			ans++;
			for (int i=0;i<n;i++) {
				S[i].erase(S[i].begin());
				if (S[i].size() == 0) {
					cout << ans << endl;
					return;
				}
				k--;
			}
		}
	}
	cout << ans << endl;
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