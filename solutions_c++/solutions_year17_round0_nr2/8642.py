#include "bits/stdc++.h"

#define debug(x) cout<<#x<<": "<<x<<endl
#define rep(i,n) for (int i=0;i<(n);i++)
#define FOR(i,a,b) for (int i=(a);i<=(b);i++)
#define all(a) (a).begin(),(a).end()
using namespace std;
typedef vector<int> VI;
typedef vector<vector<int>> VVI;
typedef long long ll;

void solve() {
#ifdef _WIN32
	istream &cin = ifstream("input.txt");
#endif
	int n;
	cin >> n;
	FOR(caseNo, 1, n) {
		cout << "CASE #" << caseNo << ": ";
		string s;
		cin >> s;
		
		if (s.size() == 1) {
			cout << s << endl;
			continue;
		}

		char target = 'a';
		rep(i, s.size() - 1) {
			if (s[i] > s[i + 1]) {
				target = s[i];
				break;
			}
			
		}
		if (target == 'a') {
			cout << s << endl;
			continue;
		}
		auto lower = s.find_first_of(target), upper = s.find_last_of(target);
		s[lower]--;
		FOR(j, lower + 1, s.size() - 1) {
			s[j] = '9';
		}
		if (s[0] == '0') s.erase(s.begin());
		cout << s << endl;
	}
}




int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);


	solve();
#ifdef _WIN32
	system("PAUSE");
#endif
	return 0;
}