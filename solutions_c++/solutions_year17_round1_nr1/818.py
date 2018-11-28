#include <bits/stdc++.h>
#define base 1000000007LL
#define ll long long
#define X first
#define Y second
#define pb push_back
#define Scan(a) scanf("%I64d", &a)
#define CLR(a) memset(a,0,sizeof(a))
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)

using namespace std;

typedef pair<int, int> II;
typedef vector<II> vi;

int t, n, m;
char ch[30][30];

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    FOR(o,1,t) {
        cin >> n >> m;
        FOR(i,1,n)
            FOR(j,1,m) cin >> ch[i][j];
        FOR(i,1,n)
            FOR(j,1,m)
                if (ch[i][j] != '?') {
                    FOR(k,j+1,m)
                        if (ch[i][k] != '?') break;
                        else ch[i][k] = ch[i][j];
                    FORE(k,j-1,1)
                        if (ch[i][k] != '?') break;
                        else ch[i][k] = ch[i][j];
                }
        FOR(i,1,n)
            if (ch[i][1] != '?') {
                FOR(k,i+1,n)
                    if (ch[k][1] != '?') break;
                    else FOR(j,1,m) ch[k][j] = ch[i][j];
                FORE(k,i-1,1)
                    if (ch[k][1] != '?') break;
                    else FOR(j,1,m) ch[k][j] = ch[i][j];
            }
        cout << "Case #" << o << ":\n";
        FOR(i,1,n) {
            FOR(j,1,m) cout << ch[i][j];
            cout << endl;
        }
    }
    return 0;
}
