#include <bits/stdc++.h>
#define ll long long
using namespace std;
int n,p;
int A[4];
void solve() {
	cin >> n >> p;
	for (int i=0;i<4;i++) A[i] = 0;
	for (int i=0;i<n;i++) {
		int x;
		cin >> x;
		A[x%p]++;
	}
	if (p == 2) {
		cout << A[0] + (A[1]+1)/2 << endl;
		return;
	}
	if (p == 3) {
		int ans = A[0];
		int x = min(A[1],A[2]);
		cout << ans + x + (A[1]+A[2]-x*2+2)/3 << endl;
	}
	if (p == 4) {
		int ans = A[0];
		ans += min(A[1],A[3]);
		if (A[1] > A[3]) A[1] -= A[3];
		else A[1] = A[3] - A[1];
		int maxv = 0;
		for (int i=0;i<=min(A[2],A[1]/2);i++) {
			int a = A[1] - 2*i;
			int b = A[2] - i;
			int temp = i;
			temp += b/2;
			b %= 2;
			temp += (b*2 + a + 3) / 4;
			maxv = max(maxv,temp);
		}
		cout << ans + maxv << endl;
	}
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