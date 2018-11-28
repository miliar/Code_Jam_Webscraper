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
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif // CF
    srand(time(0));
    fo << fixed << setprecision(7);
    cerr << fixed << setprecision(7);
    int t;
    fi>>t;
    for (int cs = 1;cs <= t;++cs)
    {
        fo << "Case #" << cs << ": ";
        string str;
        int k;
        fi>>str>>k;
        int ans = 0;
        int n = str.length();
        for (int i = 0;i <= n - k;++i)
        if (str[i] == '-')
        {
            ++ans;
            for (int j = i;j < i + k;++j)
                if (str[j] == '-')
                    str[j] = '+';
                else
                    str[j] = '-';
        }
        for (auto it : str)
            if (it == '-')
                ans = -1;
        if (ans != -1)
            fo << ans << '\n';
        else
            fo << "IMPOSSIBLE\n";
    }
    cerr << "Time elapsed :" << clock() * 1000.0 / CLOCKS_PER_SEC << " ms" << '\n';
    return 0;
}
