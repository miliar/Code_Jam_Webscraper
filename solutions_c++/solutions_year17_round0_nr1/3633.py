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
#define MAXN 1005
#define inf 0x3f3f3f3f

struct node{
    int x,y;
    node(){}
    node(int xx,int yy):x(xx),y(yy){}
    bool operator < (const node a) const{
        if(x == a.x) return y < a.y;
        return x < a.x;
    }
};
int a[MAXN];
int b[MAXN];
int c[MAXN];
int d[MAXN];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char s[MAXN];
bool vis[MAXN];
int n,m;
int ans;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    scanf("%d",&tt);
    while(tt--){
        ans = 0;
        scanf("%s %d",s,&n);
        int l = strlen(s);
        for(int i = 0 ; i <= l-n ; i++){
            if(s[i]=='+')continue;
            for(int j = i ; j < i+n ; j++){
                if(s[j]=='-')
                    s[j]='+';
                else s[j] = '-';
            }
            ans++;
        }
        for(int i = l-n ; i < l ; i++)
            if(s[i]=='-')
                ans = -1;
        printf("Case #%d: ",ca++);
        if(ans==-1)
        printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
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

*/
