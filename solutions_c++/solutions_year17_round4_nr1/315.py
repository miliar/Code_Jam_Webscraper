//#include <bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;


//4-side
//int xx[] = {0,0,-1,1};
//int yy[] = {-1,1,0,0};
//6-side hexagonal
//int xx[] = {2,-2,1,1,-1,-1};
//int yy[] = {0,0,1,-1,1,-1};

#define popc(a) (__builtin_popcount(a))
//ll bigmod(ll a,ll b,ll m){if(b == 0) return 1%m;ll x = bigmod(a,b/2,m);x = (x * x) % m;if(b % 2 == 1) x = (x * a) % m;return x;}
//ll BigMod(ll B,ll P,ll M){ ll R=1%M; while(P>0) {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

#define MX 100005
#define inf 100000000

const ll mod = 1000000007ll;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.in.out", "w", stdout);
    int te, ti, n, p, x;
    scanf("%d", &ti);
    for(te = 1; te <= ti; te++)
    {
        scanf("%d %d", &n, &p);
        int ans = 0, one = 0, two = 0, three = 0;
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &x);
            if(x%p == 0) ans++;
            else if(x%p == 1) one++;
            else if(x%p == 2) two++;
            else if(x%p == 3) three++;
        }
        if(p == 2)
        {
            ans += (one+1)/2;
        }else if(p == 3){
            int tem = min(one,two);
            ans += tem;
            one -= tem;
            two -= tem;
            ans += (one+2)/3+(two+2)/3;
        }else {
            ans += two/2;
            two %= 2;
            int tem = min(one,three);
            ans += tem;
            one -= tem;
            three -= tem;
            if((one+three)>=2 && two)
            {
                ans++;
                if(one) one -= 2;
                else three -= 2;
            }else if(one+three == 0 && two)
                ans++;
            ans += (one+3)/4+(three+3)/4;
        }
        printf("Case #%d: %d\n", te, ans);
    }
    return 0;
}


