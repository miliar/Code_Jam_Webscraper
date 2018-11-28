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

int t, n, p, b[55][55], a[55], d[55], g[55], c[55];
II f[2000010], e[55];

void init()
{
    FOR(i,1,2000000) {
        int lef = i * 90 / 100;
        if ((i*90) % 100) lef++;
        int rig = i * 110 / 100;
        f[i] = II(lef, rig);
    }
}

bool check()
{
    FOR(i,1,n)
        if (f[d[i]].X > 1000000) return false;
    return true;
}

bool check2()
{
    FOR(i,1,n)
        if (!(b[i][g[i]] >= e[i].X && b[i][g[i]] <= e[i].Y)) return false;
    return true;
}

bool check3()
{
    FOR(i,1,n)
        if (g[i] > p) return false;
    return true;
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    init();
    cin >> t;
    FOR(o,1,t) {
        cin >> n >> p;
        FOR(i,1,n) cin >> a[i];
        FOR(i,1,n) {
            FOR(j,1,p) cin >> b[i][j];
            sort(b[i]+1, b[i]+p+1);
        }
        /*FOR(i,1,n) {
            FOR(j,1,p) cout << b[i][j] << " ";
            cout << endl;
        }*/
        FOR(i,1,n) g[i] = 1;
        FOR(i,1,n) c[i] = 0;
        FOR(i,1,n) d[i] = 0;
        int res = 0;
        while (true) {
            FOR(i,1,n) c[i]++;
            FOR(i,1,n) d[i] += a[i];
            if (!check()) break;
            FOR(i,1,n) e[i] = f[d[i]];
            FOR(i,1,n)
                while (g[i] <= p && b[i][g[i]] < e[i].X) g[i]++;
            if (!check3()) break;
            while (check2()) {
                //cout << c[1];
                //FOR(i,1,n) cout << " " << e[i].X << " " << e[i].Y;
                //cout << endl;
                res++;
                FOR(i,1,n) g[i]++;
                if (!check3()) break;
            }
            if (!check3()) break;
        }

        cout << "Case #" << o << ": " << res << endl;
    }
    return 0;
}
