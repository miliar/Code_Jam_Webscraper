#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<int(n);++i)
char a[32][32];
int R, C;
bool ok(int r, int miny, int maxy){
    for(int i=miny;i<=maxy;++i)
        if(a[r][i]!='?')return false;
    return true;
}
void fillx(int x, int y, char ch){
    int minx, maxx, miny, maxy;
    for(miny=y;miny>=0&&a[x][miny-1]=='?';--miny);
    for(maxy=y;maxy<C&&a[x][maxy+1]=='?';++maxy);
    for(minx=x;minx>=0&&ok(minx-1,miny,maxy);--minx);
    for(maxx=x;maxx<R&&ok(maxx+1,miny,maxy);++maxx);
    for(int i=minx;i<=maxx;++i)
        for(int j=miny;j<=maxy;++j)
            a[i][j]=ch;
}
int main(){
    int T;
    scanf("%d",&T);
    REP(cs,T){
        int vis[26];
        memset(vis, 0, sizeof vis);
        scanf("%d%d ",&R,&C);
        REP(i,R)scanf("%s",a[i]);
        REP(i,R)REP(j,C){
            if(a[i][j]!='?' && !vis[a[i][j]-'A']){
                vis[a[i][j]-'A']=1;
                fillx(i,j,a[i][j]);
            }
        }
        REP(i,R)REP(j,C)assert(a[i][j]!='?');
        printf("Case #%d:\n", cs+1);
        REP(i,R)printf("%s\n",a[i]);
    }
}
