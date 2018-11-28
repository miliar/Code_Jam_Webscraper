// author: ash.code

#include <bits/stdc++.h>

#define ull unsigned long long
#define FOR(i, a, b) for(ull i = a; i <= b; i++)
#define ROF(i, a, b) for(ull i = a; i >= b; i--)
#define REP(i, n) for(ull i = 0; i < n; i++)
#define FILL(X, A) memset(X, A, sizeof(X))
#define fast ios_base::sync_with_stdio(false)
#define MOD 1000000007
typedef long long ll;

using namespace std;

int main() {
    // #ifndef ONLINE_JUDGE
    // 	freopen("ip.txt", "r", stdin);
    // 	freopen("op.txt", "w", stdout);
    // #endif
	
	fast;
    ull t;
    string s;
    cin >> t;
    REP(tt, t) {
        cin >> s;
        ull n=s.length();
        
        ROF(i, n-1, 1) {
            if(s[i] < s[i-1]) {
                FOR(j, i, n-1) {
                    if(s[j]=='9') break;
                    s[j]='9';
                }
                s[i-1]-=1;
            }
        }
        ull i=0;
        while(s[i]=='0' && i<n) {
            i++;
        }
        s = s.substr(i);

    	cout << "Case #" << tt+1 << ": " << s << endl;
    }
    
    return 0;
}

