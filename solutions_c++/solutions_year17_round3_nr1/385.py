/*    brioso     */
//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define SZ size()
#define BG begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define MT(a,x) memset(a,x,sizeof(a))
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
typedef long long ll ;
typedef pair<int, int> PII;
typedef pair<double,double> PDD;
const double PI = acos(-1.0);
const double eps =1e-8;
const int mod = 1000000007;
#define MAXN 1005000
#define inf 0x3f3f3f3f

struct node{
    ll x,y;
    node(){}
    node(ll xx,ll yy):x(xx),y(yy){}
    bool operator < (const node a) const{
        if(x*y == a.x*a.y) return y < a.y;
        return x*y < a.x*a.y;
    }
}a[MAXN];
int b[MAXN];
int c[MAXN];
int d[MAXN];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char s[MAXN];
bool vis[MAXN];
int n,m;
ll ans;

bool cmp(node a,node b){
    if(a.x==b.x)
        return a.y<b.y;
    return a.x < b.x;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    scanf("%d",&tt);
    while(tt--){
        scanf("%d %d",&n,&m);
        for(int i = 0 ; i <n ; i++){
            scanf("%I64d %I64d",&a[i].x,&a[i].y);
        }
        ans = 0;
        sort(a,a+n,cmp);
        for(int i = m-1 ; i < n ; i++){
            ll res = a[i].x*a[i].x + 2*a[i].x*a[i].y;
            priority_queue<node> que;
            for(int j = 0 ; j < i ; j++)
                que.push(a[j]);
            for(int j = 0 ; j < m-1 ; j++){
                node p = que.top();
                que.pop();
                res += 2*p.x*p.y;
            }
            ans = max(ans,res);
        }
        printf("Case #%d: ",ca++);
        printf("%.9f\n",ans*PI);
    }
    return 0;
}


/*

unsigned   int   0～4294967295
int   2147483648～2147483647
unsigned long 0～4294967295
long   2147483648～2147483647
long long的最大值：9223372036854775807
long long的最小值：-9223372036854775808
unsigned long long的最大值：18446744073709551615

__int64的最大值：9223372036854775807
__int64的最小值：-9223372036854775808
unsigned __int64的最大值：18446744073709551615

10
7 4
3173 317458
3731 377723
3110 322158
3806 383053
3356 370379
19273 85
13514 10


*/
