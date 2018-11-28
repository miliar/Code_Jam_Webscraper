/*
 * Author:  vawait
 * Created Time:  六  4/15 09:12:51 2017
 * File Name: a.cpp
 */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
using namespace std;
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define sqr(x) ((x) * (x))
#define mp make_pair
#define pb push_back
#define db pop_back
typedef long long lint;
int n , m , lef[200] , rig[200], up[200], down[200];
int vis[100];
char a[100][100];

void init()
{
    scanf("%d%d",&n,&m);
    rep(i,1,n) scanf("%s",a[i]+1);
    //rep(i,1,n) printf("%s\n",a[i]+1);
    rep(i,0,26) {
        lef[i] = up[i] = 100;
        rig[i] = down[i] = 0;
    }
    clr( vis , 0 );
    int k;
    rep(i,1,n)
        rep(j,1,m) if (a[i][j] != '?' ){
            k = a[i][j] - 'A';
            lef[k] = min( j , lef[k] );
            rig[k] = max( j , rig[k] );
            up[k] = min( i , up[k] );
            down[k] = max( i , down[k] );
        }
    rep(k,0,26) {
        rep(j,lef[k],rig[k])
            rep(i,down[k],up[k]) a[i][j] = 'A' + k;
    }
}

bool ok(int k, int y1,int y2,int x1,int x2) {
    //printf("%c %d %d %d %d\n",k+'A',x1,x2,y1,y2);
    rep(i,x1,x2)
        rep(j,y1,y2) if ( a[i][j] != '?' ) return false;
    rep(i,x1,x2)
        rep(j,y1,y2) a[i][j] = 'A' + k;
    return true;
}

void work()
{
    int k = 'C';
    rep(i,1,n)
        rep(j,1,m) if ( a[i][j] != '?' && !vis[a[i][j]-'A'] ) {
            k = a[i][j] - 'A';
            vis[k] = 1;
            while ( lef[k] > 1 && ok( k, lef[k] - 1 , lef[k] - 1 , up[k], down[k] ) ) lef[k] --;
            while ( rig[k] < m && ok( k, rig[k] + 1 , rig[k] + 1 , up[k], down[k] ) ) rig[k] ++;
        }
    clr( vis ,0 );
    rep(i,1,n)
        rep(j,1,m) if ( a[i][j] != '?' && !vis[a[i][j]-'A'] ) {
            k = a[i][j] - 'A';
            vis[k] = 1;
            while ( up[k] > 1 && ok( k, lef[k] , rig[k] , up[k] - 1, up[k] - 1 ) ) up[k] --;
            while ( down[k] < n && ok( k, lef[k] , rig[k] , down[k] + 1, down[k] + 1 ) ) down[k] ++;
        }
    rep(i,1,n) {
        rep(j,1,m) printf("%c",a[i][j]);
        puts("");
    }
}

int main()
{
    int t;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin >> t;
    rep(i,1,t) {
        printf("Case #%d:\n",i);
        init();
        work();
    }
    return 0;
}
