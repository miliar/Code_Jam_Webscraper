
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

string solve(string s) {
    int n = SIZE(s);
    int maxPref = 0;
    
    while (maxPref < n-1 && s[maxPref] <= s[maxPref+1]) {
        maxPref++;
    }
    
    if (maxPref == n-1) {
        return s;
    }
    
    int start = maxPref;
    while (start > 0 && s[start-1] == s[start]) {
        start--;
    }
    
    s[start]--;
    FOR(i,start+1,n-1) {
        s[i] = '9';
    }
    
    int pref = 0;
    while (s[pref] == '0') {
        pref++;
    }
    
    s = s.substr(pref);
    return s;
}

/*************************************************************************/

int main() {
    ios_base::sync_with_stdio(0);
    
    int t;
    cin >> t;
    
    FOR(i,1,t) {
        string s;
        cin >> s;
        
        cout << "Case #" << i << ": " << solve(s) << '\n';
    }

    return 0;
}

/*************************************************************************/

