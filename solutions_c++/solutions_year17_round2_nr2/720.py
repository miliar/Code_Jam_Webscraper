#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef long long ll;

const int MAX = 1000 + 10;

char a[MAX];
char cs[] = "ROYGBV";
pii vals[6];

void solve() {
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	vals[0] = pii(R, cs[0]);
	vals[1] = pii(O, cs[1]);
	vals[2] = pii(Y, cs[2]);
	vals[3] = pii(G, cs[3]);
	vals[4] = pii(B, cs[4]);
	vals[5] = pii(V, cs[5]);
	sort(vals, vals+6);
	reverse(vals, vals+6);
	REP(i, N) a[i] = '-';
	int idx = 0;
	int idx2 = 0;
	char cur = 'R';
	bool possible = false;
	REP(_i, N) {
		while (vals[idx2].first == 0) idx2++;
		vals[idx2].first--;
		char c = vals[idx2].second;
		bool found = false;
		REP(__i, N) {
			int prev = idx == 0 ? N-1 : idx-1;
			int next = idx == N-1 ? 0 : idx+1;
			if (a[idx] == '-' && a[prev] != c && a[next] != c) {
				found = true;
				break;
			}
			idx++;
			if (idx >= N) idx = 1;
		}
		if (!found) {
			cout << "IMPOSSIBLE";
			return;
		}
		a[idx] = c;
	}
	REP(i, N) cout << a[i];
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