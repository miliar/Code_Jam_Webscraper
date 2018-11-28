#include <bits/stdc++.h>
#define base 1000000007LL
#define ll long long
#define X first
#define Y second
#define pb push_back
#define MAXN 21010
#define Scan(a) scanf("%I64d", &a)
#define CLR(a) memset(a,0,sizeof(a))
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)

using namespace std;

typedef pair<int, int> II;
typedef vector<II> vi;

int t, k, n;
string s;

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    FOR(o,1,t) {
        cout << "Case #" << o << ": ";
        cin >> s >> k;
        n = s.length();
        s = " " + s;
        int res = 0;
        FOR(i,1,n-k+1)
            if (s[i] == '-') {
                res++;
                FOR(j,i,i+k-1)
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
            }
        FOR(i,1,n)
            if (s[i] == '-') {
                res = -1;
                break;
            }
        if (res == -1) cout << "IMPOSSIBLE\n";
        else cout << res << endl;
    }
    return 0;
}
