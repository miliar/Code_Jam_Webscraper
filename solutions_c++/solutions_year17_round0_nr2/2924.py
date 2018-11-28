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

typedef long long LL;

int test;
string num;

void printResult(int tt) {
	LL ans = atoll(num.c_str());
	cout << "Case #" << tt << ": " << ans << endl;
}

bool ok(string x) {
	int last = '0';
	REP(i, sz(x)) {
		if (x[i] < last) return false;
		last = x[i];
	}
	return true;
}

int main() {
	cin >> test;
	REP(tt, test) {
		cin >> num;
		int n = sz(num);
		//cout << "input: " << num << endl;

		if (n == 1) {
			printResult(tt + 1);
			continue;
		}

		int ind = n - 2;
		while (ind >= 0 && !ok(num)) {
			//cout << "whiling" << endl;
			while (ind >= 0 && num[ind] == '0') ind--;
			//dbg(ind);
			num[ind]--;
			for (int i = ind + 1; i < n; i++) num[i] = '9';
		}
		//dbg(num);
		assert(ok(num));
		printResult(tt + 1);
	}
	return 0;
}
