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
}a[MAXN];
int b[MAXN];
int c[MAXN];
int d[MAXN];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char s[MAXN][MAXN];
bool vis[MAXN];
int n,m;
int ans;
int num;

void dfs(int u,int v){
    char c = s[u][v];
    vis[c] = true;
    int lx = n,rx=0;
    int ly = m,ry = 0;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if(s[i][j] == c){
                lx = min(lx,i);
                ly = min(ly,j);
                rx = max(rx,i);
                ry = max(ry,j);
            }
        }
    }
    for(int i = lx ; i <= rx ; i++){
        for(int j = ly ; j <= ry ; j++){
            s[i][j] = c;
        }
    }
}
bool k(char c){
    int lx = n,rx=0;
    int ly = m,ry = 0;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if(s[i][j] == c){
                lx = min(lx,i);
                ly = min(ly,j);
                rx = max(rx,i);
                ry = max(ry,j);
            }
        }
    }
    for(int i = lx ; i <= rx ; i++){
        for(int j = ly ; j <= ry ; j++){
            if(s[i][j] != c)
                return false;
        }
    }
    return true;
}
bool ok(){
    MT(vis,0);
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < m ; j++){
                if(s[i][j]=='?')return false;
                if(vis[s[i][j]])continue;
                vis[s[i][j]] = true;
                if(!k(s[i][j]))
                    return false;
            }
        }
        return true;
}
bool dfs1(int u){
    if(ok())
        return true;
    node p = a[u];
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if(s[i][j]!= '?')continue;
            if(s[i][j]=='?'){
                p = node(i,j);

                for(int i = 0 ; i < 4 ; i++){
                    int x = p.x+dx[i];
                    int y = p.y+dy[i];
                    if(x<0||x>=n||y<0||y>=m)continue;
                    if(s[x][y]=='?')continue;
                    s[p.x][p.y] = s[x][y];
                    if(dfs1(u+1))
                        return true;
                }

            }
            s[i][j] = '?';
        }
    }

}

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int tt,ca = 1;
    int p,q;
    scanf("%d",&tt);
    while(tt--){
        MT(vis,0);
        scanf("%d %d",&n,&m);
        for(int i = 0 ; i < n ; i++)
            scanf("%s",s[i]);
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < m ; j++){
                if(s[i][j]=='?' || vis[s[i][j]])continue;
                dfs(i,j);
            }
        }
        num = 0;
        MT(vis,0);
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < m ; j++){
                if(s[i][j]=='?')
                    num++;
            }
        }
        if(num>0)
            dfs1(0);

        printf("Case #%d:\n",ca++);
        for(int i = 0 ; i <n ; i++){
            for(int j = 0 ; j < m ; j++)
                printf("%c",s[i][j]);
            printf("\n");
        }
        //printf("%d\n",ans);
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
