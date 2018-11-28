#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <string>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define SIZE (200000+10)
#define Ri(a) scanf("%d", &a)
#define Rl(a) scanf("%I64d", &a)
#define Rf(a) scanf("%lf", &a)
#define Rs(a) scanf("%s", a)
#define Pi(a) printf("%d\n", (a))
#define Pf(a) printf("%lf\n", (a))
#define Pl(a) printf("%I64d\n", (a))
#define Ps(a) printf("%s\n", (a))
#define xx first
#define yy second
#define CLR(a, b) memset(a, (b), sizeof(a))
#define INT_MAX 2147483647
#define LL_MAX 9223372036854775807
#define ll __int64
#define lson l, mid, rt<<1
#define rson mid+1, r, rt<<1|1
#define PI acos(-1.0)
const long long MOD = 1000000007;
using namespace std;
ll n,k;
ll minans,maxans;
void solve(ll good,ll bad,ll good_good,ll good_bad,ll bad_bad,ll num,ll pre)
{
//    cout<<"-------"<<good_good<<"-----"<<good_bad<<"-----"<<bad_bad<<endl;
    if(num >= k)
    {
        k -= pre;
        if(k <= good_good)
        {
            minans = good,maxans = good;
            return ;
        }
        k -= good_good;
        if(k <= good_bad)
        {
            minans = bad,maxans = good;
            return ;
        }
        minans = bad,maxans = bad;
        return ;
    }
    good--;
    if(good%2)
    {
        solve(good/2+1,good/2,0,good_good*2+good_bad,bad_bad*2+good_bad,num + 2*(num-pre),num);
    }
    else
    {
        solve(good/2,(good/2-1) >= 0 ? (good/2-1) : 0,good_good*2+good_bad,bad_bad*2+good_bad,0,num + 2*(num-pre),num);
    }
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    Ri(t);
    for(int cas = 1; cas <= t; cas++)
    {
        Rl(n),Rl(k);
  //      n = 1000,k = cas;
   //     cout<<n<<' '<<k<<endl;
        n--;
        if(n%2)
            solve(n/2+1,n/2,0,1,0,1,0);
        else
            solve(n/2,(n/2-1) >= 0 ? (n/2-1) : 0,1,0,0,1,0);
        printf("Case #%d: ",cas);

        cout<<maxans<<' '<<minans<<endl;
    }
    return 0;
}
