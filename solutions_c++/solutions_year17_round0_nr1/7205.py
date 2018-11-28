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

int n, k, dp[1001][2001], inf = 1<<20;
string s;

int solve()
{
    int ans = 0;
    Rep(i, n)
    {
        
        if(s[i] == '-')
        {
            ans ++;
            if(i + k > n)
            {
            
                return -2;
                
            }
            else
            {
                For(j, i, i + k) if(s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    
    Rep(i, n) if(s[i] == '-') return -2;
    
    return ans;
}


int main()
{
    freopen("/Users/yoonesrezaei/Documents/Projects/Contests/Contests/a.in", "r", stdin);
    freopen("/Users/yoonesrezaei/Documents/Projects/Contests/Contests/a.out", "wr", stdout);

    int tc , cas = 1;
    cin>>tc;
    while (tc--)
    {
        cin>>s>>k;
        n = s.size();
        Set(dp, -1);
        int ans = solve();
        
        if(ans == -2) PF("Case #%d: IMPOSSIBLE\n", cas++);
        else PF("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
