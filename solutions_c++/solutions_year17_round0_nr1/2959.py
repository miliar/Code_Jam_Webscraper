#include <bits/stdc++.h>
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

int test, x, n;
string cake;

int main() {
	cin >> test;
	REP(tt, test) {
		cin >> cake >> x;
		n = sz(cake);
		int cnt = 0;

		REP(i, n-x+1) {
			if (cake[i] == '-') {
				cnt++;
				REP(j, x) cake[i+j] = (cake[i+j] == '+' ? '-' : '+');
			}
		}

		bool ok = true;
		REP(i, n) if (cake[i] == '-') ok = false;

		cout << "Case #" << tt + 1 << ": ";

		if (ok) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
