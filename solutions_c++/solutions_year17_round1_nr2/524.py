/// b.cpp

# include <stdio.h>
# include <bits/stdc++.h>
using namespace std;
const pair < int , int > DD[] = {{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};
# define fi cin
# define fo cout
# define x first
# define y second
# define ll long long
# define IOS ios_base :: sync_with_stdio(0);cin.tie(0)
# define p(v) cerr << #v << " = " << v << '\n'
# define p2(v) cerr << #v << " = " << (complex < __typeof(v.x) > (v.x,v.y)) << '\n'
# define vi vector < int >
# define vl vector < ll >
# define pll pair < ll , ll >
# define pii pair < int , int >
# define mp make_pair
# define db long double
# define fail puts("-1")
# define yes puts("YES")
# define no puts("NO")
# define PP puts("Possible")
# define II puts("Impossible")
# define vii vector < pii >
# define vll vector < ll >
# define pb push_back
# define pdd pair < db , db >
# define CF
template < class T > T smin(T &a,T b) {if (a > b) a = b;return a;}
template < class T > T smax(T &a,T b) {if (a < b) a = b;return a;}
int main(void)
{
    #ifdef CF
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    #endif // CF
    srand(time(0));
    fo << fixed << setprecision(7);
    cerr << fixed << setprecision(7);
    int t;
    fi>>t;
    for (int cs = 1;cs <= t;++cs)
    {
        fo << "Case #" << cs << ": ";
        static int s[1 << 20];
        int n,m;
        fi>>n>>m;
        for (int i = 1;i <= n;++i)
            fi>>s[i];
        static pii v[1 << 10][1 << 10];
        vi ss;
        for (int i = 1;i <= n;++i)
            for (int j = 1;j <= m;++j)
                {
                    int cnt;
                    fi>>cnt;
                    int L = (10 * cnt + 11 * s[i] - 1) / (11 * s[i]);
                    int R = (10 * cnt) / (9 * s[i]);
                    v[i][j] = mp(L,R);
                    ss.pb(L);ss.pb(R);
                }
        sort(ss.begin(),ss.end());
        ss.resize(unique(ss.begin(),ss.end()) - ss.begin());
        for (int i = 1;i <= n;++i)
            for (int j = 1;j <= m;++j)
            {
                v[i][j].x = lower_bound(ss.begin(),ss.end(),v[i][j].x) - ss.begin() + 1;
                v[i][j].y = lower_bound(ss.begin(),ss.end(),v[i][j].y) - ss.begin() + 1;
            }
        static int was[1 << 10][1 << 10];
        for (int i = 1;i <= n;++i)
            for (int j = 1;j <= m;++j)
                was[i][j] = 0;
        int sz = ss.size();
        int ans = 0;
        for (int tt = 1;tt <= sz;++tt)
        {
            static int bst[1 << 20];
            for (int i = 1;i <= n;++i)
                bst[i] = 0;
            for (int i = 1;i <= n;++i)
                for (int j = 1;j <= m;++j)
                    if (!was[i][j] && v[i][j].y >= tt && v[i][j].x <= tt)
                        if (!bst[i] || v[i][bst[i]].y > v[i][j].y)
                            bst[i] = j;
            int ok = 1;
            for (int i = 1;i <= n;++i)
                ok &= bst[i] != 0;
            if (ok)
            {
                ++ans;
                for (int i = 1;i <= n;++i)
                    was[i][bst[i]] = 1;
                --tt;
            }
        }
        fo << ans << '\n';
    }
    cerr << "Time elapsed :" << clock() * 1000.0 / CLOCKS_PER_SEC << " ms" << '\n';
    return 0;
}
