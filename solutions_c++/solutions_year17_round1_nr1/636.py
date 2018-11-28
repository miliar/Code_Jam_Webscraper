#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;


int TC;

int R, C;
string A[100];
void solve() {
	cin >> R >> C;
	rep(i, R) cin >> A[i];
	rep(i, R) {
		char cur = '?';
		rep(j, C) {
			if (A[i][j] == '?')
				A[i][j] = cur;
			else
				cur = A[i][j];
		}

		cur = '?';
		for(int j=C-1; j>=0; j--) {
			if (A[i][j] == '?')
				A[i][j] = cur;
			else
				cur = A[i][j];
		}
	}

	string cur = A[0];
	rep(i, R) {
		if (A[i][0] == '?') {
			A[i] = cur;
		} else {
			cur = A[i];
		}
	}
		
	for(int i=R-1; i>=0; i--) {
		if (A[i][0] == '?') {
			A[i] = cur;
		} else {
			cur = A[i];
		}
	}

	rep(i, R) {
		cout << A[i] << endl;
	}

}
int main() {
	int T; cin >> T;
	for(int TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ":" << endl;
		solve();
	}
}

