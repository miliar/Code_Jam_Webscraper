
#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define SIZE(c) (int) (c).size()
#define FORE(i,c) FOR(i,0,SIZE(c)-1)
#define FORDE(i,c) FORD(i,SIZE(c)-1,0)

#define pb push_back
#define mp make_pair
#define st first
#define nd second


using namespace std;

typedef long long ll;
typedef pair <int,int> pii;
typedef pair <ll,ll> pll;

typedef vector <int> VI;
typedef vector <bool> VB;
typedef vector <pii> VP;
typedef vector <ll> VL;
typedef vector <pll> VPL;

typedef vector <VI> VVI;
typedef vector <VL> VVL;
typedef vector <VB> VVB;
typedef vector <VP> VVP;

const int MOD = 1000000007;
const int INF = 1000000001;
const ll LINF = 1000000000000000001LL;

/*************************************************************************/

int solve(string &s, int k) {
    int n = SIZE(s), ans = 0;
    FOR(i,0,n-k) if (s[i] == '-') {
        ans++;
    
        FOR(j,i,i+k-1) {
            s[j] = '+' + '-' - s[j];
        }
    }
    
    for (char c : s) if (c != '+') {
        return -1;
    }
    
    return ans;
}

/*************************************************************************/

int main() {
    ios_base::sync_with_stdio(0);
    
    int t;
    cin >> t;
    
    FOR(i,1,t) {
        string s;
        int k;
        
        cin >> s >> k;
        
        int ans = solve(s, k);
        cout << "Case #" << i << ": ";
        
        if (ans == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        };
        
        cout << '\n';
    }

    return 0;
}

/*************************************************************************/

