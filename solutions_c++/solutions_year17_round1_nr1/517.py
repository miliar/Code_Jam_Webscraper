/// a.cpp

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
        fo << "Case #" << cs << ":\n";
        static char str[555][555];
        int n,m;
        fi>>n>>m;
        for (int i = 1;i <= n;++i)
            fi>>(str[i] + 1);
        int was = 0;
        for (int i = 1;i <= n;++i)
        {
            int cnt = 0;
            for (int j = 1;j <= m;++j)
                cnt |= str[i][j] != '?';
            was |= cnt;
            if (cnt)
            {
                int prev = 0;
                for (int j = 1;j <= m;++j)
                if (str[i][j] != '?')
                {
                    for (int k = prev + 1;k < j;++k)
                        str[i][k] = str[i][j];
                    prev = j;
                }
                for (int k = prev + 1;k <= m;++k)
                    str[i][k] = str[i][prev];
            }
        }
        if (!was)
        {
            for (int i = 1;i <= n;++i)
                for (int j = 1;j <= m;++j)
                    str[i][j] = 'A';
        }
        else
        {
            for (int j = 1;j <= m;++j)
            {
                int prev = 0;
                for (int i = 1;i <= n;++i)
                if (str[i][j] != '?')
                {
                    for (int k = prev + 1;k < i;++k)
                        str[k][j] = str[i][j];
                    prev = i;
                }
                for (int k = prev + 1;k <= n;++k)
                    str[k][j] = str[prev][j];
            }
        }
        for (int i = 1;i <= n;++i,fo << '\n')
            for (int j = 1;j <= m;++j)
                fo << str[i][j];
    }
    cerr << "Time elapsed :" << clock() * 1000.0 / CLOCKS_PER_SEC << " ms" << '\n';
    return 0;
}
