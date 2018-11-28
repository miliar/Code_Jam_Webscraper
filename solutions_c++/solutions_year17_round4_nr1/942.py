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
# define vll vector < pll >
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
    static int dp1[111][111][5];
    memset(dp1,-1,sizeof(dp1));
    function < int(int,int,int) > f1 = [&](int x,int y,int z)
    {
        if (dp1[x][y][z] != -1)
            return dp1[x][y][z];
        int &ans = dp1[x][y][z];
        ans = 0;
        if (!x && !y)
            return ans;
        if (x >= 1)
            smax(ans,f1(x - 1,y,(z + 1) % 3));
        if (y >= 1)
            smax(ans,f1(x,y - 1,(z + 2) % 3));
        ans += !z;
        return ans;
    };
    static int dp2[111][111][111][5];
    memset(dp2,-1,sizeof(dp2));
    function < int(int,int,int,int) > f2 = [&](int x,int y,int z,int t)
    {
        if (dp2[x][y][z][t] != -1)
            return dp2[x][y][z][t];
        int &ans = dp2[x][y][z][t];
        ans = 0;
        if (!x && !y && !z)
            return ans;
        if (x >= 1)
            smax(ans,f2(x - 1,y,z,(t + 1) % 4));
        if (y >= 1)
            smax(ans,f2(x,y - 1,z,(t + 2) % 4));
        if (z >= 1)
            smax(ans,f2(x,y,z - 1,(t + 3) % 4));
        ans += !t;
        return ans;
    };
    for (int cs = 1;cs <= t;++cs)
    {
        fo << "Case #" << cs << ": ";
        int n,k;
        fi>>n>>k;
        static int cnt[55];
        memset(cnt,0,sizeof(cnt));
        while (n --)
        {
            int v;
            fi>>v;
            ++cnt[v % k];
        }
        if (k == 2)
            fo << (cnt[0] + ((cnt[1] + 1) / 2)) << '\n';
        else
        if (k == 3)
            fo << (cnt[0] + f1(cnt[1],cnt[2],0)) << '\n';
        else
            fo << (cnt[0] + f2(cnt[1],cnt[2],cnt[3],0)) << '\n';
    }
    cerr << "Time elapsed :" << clock() * 1000.0 / CLOCKS_PER_SEC << " ms" << '\n';
    return 0;
}
