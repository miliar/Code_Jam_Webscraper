#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <stack>
#include <bitset>


using namespace std;

#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     FIT(it,v)         for (typeof((v).begin())it=(v).begin(); it!=(v).end(); ++it)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     GSORT(x)          sort(ALL(x), greater<typeof(*((x).begin()))>())
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              550000
#define     MOD               1000000007
#define     deb(x)            cout << #x << " : " << x << endl
#define     Dbug              cout<<"";
typedef unsigned long long ll;
typedef pair<int, int> pii;

ll n;
string st;
ll dp[19][10][3], pw[20];
bool vis[19][10][3];
int mxl;
vector<int> digits;
int len(ll num)
{
    int l = 0;
    while(num) l++, num/=10;
    return l;
}
ll rec(int p, int r, bool big)
{
    if(p == mxl)
    {
        return 0;
    }
    if(vis[p][r][big])
    {
        return dp[p][r][big];
    }
    vis[p][r][big] = 1;
    ll ret = 0;
    For(j, r, 10)
    {
        if(big == 0) //==
        {
            if(j > digits[p]) break;
        }
        int tb = big;
        if(j < digits[p]) tb = 1;
        ll num = rec(p+1, j, tb);
        int l = len(num);
        num = (j * pw[l]) + num;
        ret = max(ret, num);
    }
    return dp[p][r][big] = ret;
}
int main()
{
    freopen("/Users/yoonesrezaei/Documents/Projects/Contests/Contests/a.in", "r", stdin);
    freopen("/Users/yoonesrezaei/Documents/Projects/Contests/Contests/a.out", "wr", stdout);
    int tc, cas = 1;
    cin>>tc;
    pw[0] = 1;
    For(i, 1, 20) pw[i] = pw[i - 1] * 10;
    while (tc--)
    {
        cin>>n;
        digits.clear();
        ll tmp = n;
        while(tmp)
        {
            digits.push_back(tmp%10);
            tmp /= 10;
        }
        reverse(ALL(digits));
        mxl = len(n);
        Set(vis, 0);
        ll ans = rec(0, 1, 0);
        ans = max(ans, rec(1, 1, 1));
        PF("Case #%d: ", cas ++);
        cout<<ans<<endl;
    }
    return 0;
}
