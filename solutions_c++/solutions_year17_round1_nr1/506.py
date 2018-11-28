#include <bits/stdc++.h>
#define ll long long
using namespace std;
void solve() {
	int r,c;
	cin >> r >> c;
	string s[30];
	for (int i=0;i<r;i++) cin >> s[i];
	for (int i=0;i<r;i++) {
		for (int j=0;j<c;j++) {
			if (s[i][j] == '?') {
				if (j>0) s[i][j] = s[i][j-1];
			}
		}
	}
	for (int i=r-1;i>=0;i--) {
		for (int j=c-1;j>=0;j--) {
			if (s[i][j] == '?') {
				if (j<c-1) s[i][j] = s[i][j+1];
			}
		}
	}
	for (int i=0;i<r;i++) {
		for (int j=0;j<c;j++) {
			if (s[i][j] == '?') {
				if (i>0) s[i][j] = s[i-1][j];
			}
		}
	}
	for (int i=r-1;i>=0;i--) {
		for (int j=c-1;j>=0;j--) {
			if (s[i][j] == '?') {
				if (i<r-1) s[i][j] = s[i+1][j];
			}
		}
	}
	cout << endl;
	for (int i=0;i<r;i++) {
		cout << s[i] << endl;
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