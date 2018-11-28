#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define ll long long
#define ull unsigned long long

#define PI (3.1415926535897932)
#define eps 1e-8

void solve() {
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	if(B < O || Y < V || R < G) {
		cout << "IMPOSSIBLE";
		return;
	}
	if (B == O && B != 0) {
		if (Y + V + R + G == 0) {
			REP(k, B) cout << "BO";
		}
		else {
			cout << "IMPOSSIBLE";
		}
		return;
	}
	if (Y == V && Y != 0) {
		if (B + O + R + G == 0) {
			REP(k, Y) cout << "YV";
		}
		else {
			cout << "IMPOSSIBLE";
		}
		return;
	}
	if (R == G && R != 0) {
		if (Y + V + B + O == 0) {
			REP(k, R) cout << "RG";
		}
		else {
			cout << "IMPOSSIBLE";
		}
		return;
	}
	pair<int, pair<char, pair<char, int> > > colCnt[3] = { {R - G, {'R', {'G', G}}} ,{ B - O, {'B', {'O', O}} } ,{Y - V, {'Y', {'V', V} } } };
	int NN = R + B + Y - G - O - V;

	sort(colCnt, colCnt + 3);

	if (colCnt[2].first > NN / 2) {
		cout << "IMPOSSIBLE";
		return;
	}
	int m[3][10000] = {};
	REP(i, colCnt[2].first) {
		m[2][i] = 1;
	}
	int k;
	for (int i = 0; i < colCnt[1].first; i++) {
		m[1][i] = 1;
	}
	for (int i = 0; i < colCnt[0].first; i++) {
		m[0][colCnt[2].first - i - 1] = 1;
	}
	char col[3] = {};

	bool f[3] = { false, false, false };

	for (int i = 0; i < colCnt[2].first; i++) {
		for (int j = 2; j >= 0; j--) {
			if (m[j][i] > 0) {
				cout << colCnt[j].second.first;
				if (f[j] == false) {
					f[j] = true;
					REP(k, colCnt[j].second.second.second)
						cout << colCnt[j].second.second.first << colCnt[j].second.first;
				}
			}
		}
	}
}


int main() {
	int T; cin >> T;
	FOR(i, 1, T + 1) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}