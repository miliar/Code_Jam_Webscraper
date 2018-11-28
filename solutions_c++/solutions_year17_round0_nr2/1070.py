#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		string s;
		cin >> s;
		int n = s.size();
		REP(i, n) {
			string t = s;
			FOR(j, i, n-1) t[j] = t[i];
			if (s < t) {
				--s[i];
				FOR(j, i+1, n-1) s[j] = '9';
				break;
			}
		}
		if (s[0] == '0') s.erase(s.begin());
		cout << "Case #" << cN << ": " << s << endl;
	}
}
