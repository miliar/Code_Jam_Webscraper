//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <bitset>
#include <string>
#include <time.h>
using namespace std;
long double esp=1e-11;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define cle(a) while(!a.empty())a.pop()
#define mem(p,c) memset(p,c,sizeof(p))
#define mp(A, B) make_pair(A, B)
#define pb push_back
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
typedef long long int LL;
const long double PI = acos((long double)-1);
const LL INF=0x3f3f3f3fll;
const int MOD =1000000007ll;
const int maxn=500100;
char s[100];
priority_queue<LL>q;
map<LL,LL>p;
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        LL n,k;
        scanf("%lld%lld",&n,&k);
        cle(q);
        p.clear();
        pair<LL,LL>ans{0,0};
        p[n]=1;
        q.push(n);
        while(k>0&&!q.empty())
        {
            n=q.top();
            q.pop();
            LL s=p[n];  //printf("q%lld %lld\n",n,s);
            if(s>=k)
            {
                ans={n/2,(n-1)/2};
                break;
            }
            k-=s;
            p.erase(n);
            if(p.find(n/2)==p.end())
                q.push(n/2);
            p[n/2]+=s;
            if(p.find((n-1)/2)==p.end())
                q.push((n-1)/2);
            p[(n-1)/2]+=s;
        }
        printf("Case #%d: %lld %lld\n",gg,ans.fi,ans.se);
    }
    return 0;
}
