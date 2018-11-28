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
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    char c;
    scanf("%d",&tt);
    while(tt--){
        scanf("%d %d",&n,&m);
        scanf("%d.%d",&p,&q);
        p = p*10000+q;
        int sum = 0;
        gets(s);
        priority_queue<int, vector<int>, greater<int> > que;
        for(int i = 0 ; i < n ; i++){
            scanf("%d.%d",&q,&a[i]);
            if(q==1)
                a[i] += 10000;
            que.push(a[i]);
        }
        while(p){
            int x = que.top();que.pop();
            int y = que.top();
            if(y-x < p){
                p -= y-x+1;
                x = y+1;
                que.push(x);
            }
            else{
                x += p;
                que.push(x);
                break;
            }
        }
        double ans = 1.0;
        while(!que.empty()){
            int x = que.top();
            que.pop();
            ans *= 0.0001*x;
        }
        printf("Case #%d: ",ca++);
        printf("%f\n",ans);
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


3
3 3
1.0000
0.4000 0.4000 1.0000
*/
