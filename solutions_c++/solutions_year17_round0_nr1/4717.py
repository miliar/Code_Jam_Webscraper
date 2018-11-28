// author: ash_code

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
	
	string s;
    ull t, k;
    cin >> t;
    REP(tt, t) {
    	cin >> s >> k;
    	ull n=s.length(), ans=0;
    	REP(i, n-k+1) {
    		if(s[i]=='-') {
    			ans++;
    			REP(j, k) {
    				if(s[i+j]=='-') 
    					s[i+j]='+';
    				else 
    					s[i+j]='-';
    			}
    		}
    	}

    	REP(i, n) {
    		if(s[i]=='-') {
    			ans=-1; break;
    		}
    	}

    	if(ans==-1) {
    		cout << "Case #" << tt+1 << ": IMPOSSIBLE\n";
    	}
    	else {
    		cout << "Case #" << tt+1 << ": " << ans << endl;
    	}
    }  
    
    return 0;
}

