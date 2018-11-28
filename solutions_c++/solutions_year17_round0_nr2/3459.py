#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,k,n) for(int i=k;i<(int)(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define INF 1<<30
#define mp make_pair
#define fi first
#define se second

using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int main() {
	int T;
	cin >> T;

	rep(t, T) {
		string s;
		cin >> s;

		for(int i = s.size()-1; i >= 1; i--) {
			if(s[i-1] <= s[i]) continue;
			else {
				s[i-1]--;

				REP(j, i, s.size()) {
					s[j] = '9';
				}
			}
		}


		cout << "Case #" << t + 1 << ": ";

		if(s[0] == '0') {
			REP(i, 1, s.size()) cout << s[i];
			cout << endl;
		} else cout << s << endl;
	}

	return 0;
}
