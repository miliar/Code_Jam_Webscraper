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
typedef long long ll;

const int MAX = 1000000;

void solve() {
	string s;
	cin >> s;
	int len = s.size();
	FORD(i, len-2, 0) {
		if (s[i] > s[i+1]) {
			s[i]--;
			FOR(j, i+1, len-1) s[j] = '9';
		}
	}
	if (s[0] != '0') cout << s[0];
	FOR(i, 1, len-1) cout << s[i];
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