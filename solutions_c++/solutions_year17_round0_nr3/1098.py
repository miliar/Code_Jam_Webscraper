#include <cstdio>
#include <string>
#include <iostream>
#include <map>

using namespace std;

typedef long long int64;
#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, k;
		cin >> n >> k;
		map<int64, int64> cnt;
		cnt[n] = 1;
		cout << "Case #" << cN << ": ";
		while (1) {
			int64 ma = cnt.rbegin()->first;
			int64 L = (ma-1) / 2;
			int64 R = ma-1-L;
			if (k <= cnt[ma]) {
				cout << R << " " << L << endl;
				break;
			} else {
				cnt[L] += cnt[ma];
				cnt[R] += cnt[ma];
				k -= cnt[ma];
				cnt.erase(ma);
			}
		}
	}
}
