#include <bits/stdc++.h>


#define f(i, a, b) for(int i = a; i <= b; i++)
#define fd(i, a, b) for(int i = a; i >= b; i--)
#define fin ""
#define fou ""
#define mp make_pair
#define fi first
#define se second
#define pb push_back

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int m, n, t, lastr;
char a[30][30], b[30][30];
vector<pair<char, int> > v;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.ou", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> m >> n;
        f(i, 1, m)
        {
            int ok = 0;
            f(j, 1, n)
            {
                cin >> a[i][j];
                if (a[i][j] != '?') ok = 1;
            }
            if (ok) lastr = i;
        }
        int last = 0;
        f(i, 1, m)
        {
            v.clear();
            f(j, 1, n)
                if (a[i][j] != '?') v.pb(mp(a[i][j], j));
            v.pb(mp('?', n + 1));
            if (v.size() == 1) continue;
            f(ii, last + 1, i)
                f(jj, 0, v.size() - 2)
                    f(k, v[jj].se, v[jj + 1].se - 1)
                        b[ii][k] = v[jj].fi;
            f(ii, last + 1, i)
                f(j, 0, v[0].se - 1)
                    b[ii][j] = v[0].fi;
            if (lastr == i)
            {
                f(ii, i + 1, m)
                    f(jj, 0, v.size() - 2)
                        f(k, v[jj].se, v[jj + 1].se - 1)
                            b[ii][k] = v[jj].fi;
                f(ii, i + 1, m)
                    f(j, 0, v[0].se - 1)
                        b[ii][j] = v[0].fi;
            }
            last = i;
        }
        cout << "Case #" << tt << ": " << endl;
        f(i, 1, m)
        {
            f(j, 1, n)
                cout << b[i][j];
            cout << endl;
        }
    }
    return 0;
}
