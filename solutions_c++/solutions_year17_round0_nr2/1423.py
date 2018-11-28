#include <bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); ++i)
#define fi first
#define se second

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;

    string s;
	FOR(t,T) {
	    cin >> s;
	    int conf = -1;
	    FOR(i, s.length()-1) {
	        if(s[i] > s[i+1]) {
                conf = i;
                break;
	        }
	    }
	    if(conf != -1) {
	        int k = conf;
            while(k>=0 && s[k] == s[conf]) {
                k--;
            }
            k++;
            s[k] = (s[k]-1);
            REP(i, k+1, s.length()-1) {
                s[i] = '9';
            }
            if(s[0] == '0') {
                FOR(i, s.length()) {
                    if(s[i] != '0') {
                        s = s.substr(i);
                        break;
                    }
                }
            }
	    }
		cout << "Case #" << t+1 << ": ";
        cout << s;
		cout << endl;
	}
	return 0;
}
