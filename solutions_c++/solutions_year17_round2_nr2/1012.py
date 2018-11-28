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
    int x,id;
    node(){}
    node(int xx,int id):x(xx),id(id){}
    bool operator < (const node a) const{
        if(x == a.x) return id < a.id;
        return x < a.x;
    }
}a[MAXN];
int b[MAXN];
int c[MAXN];
int d[MAXN];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char str[] = {"ROYGBV"};
char s[MAXN];
bool vis[MAXN];
int n,m;
int ans;

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    scanf("%d",&tt);
    while(tt--){
        scanf("%d",&n);
        priority_queue<node> que;
        for(int i = 0 ; i < 6 ; i++){
            scanf("%d",&a[i].x);
            a[i].id = i;
            if(a[i].x>0)
                que.push(a[i]);
        }
        int last = -1;
        int num = 0;
        bool f = true;
        while(!que.empty()){
            if(n-num==3&&que.size()==3){
                if(s[0]=='R'){
                    if(last==0||last==2){
                        s[num++] = 'B';
                        s[num++] = 'R';
                        s[num++] = 'Y';
                    }
                    else {
                        s[num++] = 'Y';
                        s[num++] = 'R';
                        s[num++] = 'B';
                    }
                    break;
                }
            }
            node p = que.top();
            que.pop();
            if(last==p.id&&que.empty()){
                f = false;
                break;
            }
            if(last==p.id){
                node q = p;
                p = que.top();
                que.pop();
                que.push(q);
            }
            s[num++] = str[p.id];
            last = p.id;
            if(p.x > 1)
                que.push(node(p.x-1,p.id));
        }
        s[num] = '\0';
        if(s[0]==s[num-1])
            f = false;
        printf("Case #%d: ",ca++);
        if(f)
            printf("%s\n",s);
        else printf("IMPOSSIBLE\n");
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
