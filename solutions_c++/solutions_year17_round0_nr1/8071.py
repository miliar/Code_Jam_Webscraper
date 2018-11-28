#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;

const int MAX = 1000000;

bool a[1000];

int calc(int K, int len) {
	int res = 0;
	REP(i, len) {
		if (i + K > len) break;
		if (!a[i]) {
			REP(j, K) a[i+j] = !a[i+j];
			res++;
		}
	}
	// REP(i, len) cout << a[i] ? '+' : '-'; cout << endl;
	REP(i, len) {
		if (!a[i]) return MAX;
	}
	return res;
}

void solve() {
	string S;
	int K;
	cin >> S >> K;
	int len = S.size();
	REP(i, len) a[i] = S[i] == '+';
	int c1 = calc(K, len);
	REP(i, len) a[len-i-1] = S[i] == '+';
	c1 = min(calc(K, len), c1);
	if (c1 == MAX) {
		cout << "IMPOSSIBLE";
		return;
	}
	cout << c1;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
}