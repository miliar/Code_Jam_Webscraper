#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, K, CS, CT, w[1050][12][12];
int D[50][50], chk[50][50];
int G[1025][1025];
char p[40][40];
struct point{
    int x, y;
}Q[5010], Path[1025][1025];
void Make(int x, int y){
    int i;
    for(i=y;p[x][i]!='#';i--)chk[x][i]=1;
    for(i=y;p[x][i]!='#';i++)chk[x][i]=1;
    for(i=x;p[i][y]!='#';i--)chk[i][y]=1;
    for(i=x;p[i][y]!='#';i++)chk[i][y]=1;
}
int Get(int x, int y){
    int r = 1e9;
    int i;
    for(i=y;p[x][i]!='#';i--)r=min(r,D[x][i]);
    for(i=y;p[x][i]!='#';i++)r=min(r,D[x][i]);
    for(i=x;p[i][y]!='#';i--)r=min(r,D[i][y]);
    for(i=x;p[i][y]!='#';i++)r=min(r,D[i][y]);
    return r;
}
int head, tail;
void Ins(int x, int y, int d){
    if(p[x][y]=='#')return;
    if(D[x][y]<=d)return;
    D[x][y]=d;
    Q[++tail] = {x,y};
}
void BFS(int x, int y){
    head = 0, tail = 0;
    int i, j;
    for(i=1;i<=n;i++)for(j=1;j<=m;j++)D[i][j]=1e9;
    Ins(x,y,0);
    while(head < tail){
        point t = Q[++head];
        if(chk[t.x][t.y])continue;
        Ins(t.x+1,t.y,D[t.x][t.y]+1);
        Ins(t.x,t.y+1,D[t.x][t.y]+1);
        Ins(t.x-1,t.y,D[t.x][t.y]+1);
        Ins(t.x,t.y-1,D[t.x][t.y]+1);
    }
}
int main(){
    freopen("/Users/joseunghyeon/Downloads/D-small-attempt0 (1).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int i, j, k, l;
    int TT, TC;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%d%d%d",&m,&n,&K);
        for(i=1;i<=n;i++){
            scanf("%s",p[i]+1);
        }
        for(i=0;i<=n+1;i++){
            for(j=0;j<=m+1;j++){
                if(i==0||j==0||i==n+1||j==m+1)p[i][j]='#';
            }
        }
        vector<point> S, T;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                if(p[i][j]=='S')S.push_back({i,j});
                if(p[i][j]=='T')T.push_back({i,j});
            }
        }
        CS = S.size(), CT = T.size();
        for(i=0;i<(1<<CT);i++){
            for(j=1;j<=n;j++)for(k=1;k<=m;k++)chk[j][k] = 0;
            for(k=0;k<CT;k++){
                if((1<<k)&i)continue;
                Make(T[k].x,T[k].y);
            }
            for(j=0;j<CS;j++){
                BFS(S[j].x,S[j].y);
                for(k=0;k<CT;k++){
                    w[i][j][k] = Get(T[k].x,T[k].y);
                }
            }
        }
        for(i=0;i<(1<<CS);i++)for(j=0;j<(1<<CT);j++)G[i][j] = 0;
        G[0][0] = 1;
        int MM = -1, xx = 0, yy = 0;
        for(i=0;i<(1<<CS);i++){
            for(j=0;j<(1<<CT);j++){
                if(!G[i][j])continue;
                int c = CS;
                for(k=0;k<CS;k++){
                    if((1<<k)&i)continue;
                    c--;
                    for(l=0;l<CT;l++){
                        if((1<<l)&j)continue;
                        if(w[j][k][l]<=K){
                            G[i|(1<<k)][j|(1<<l)] = 1;
                            Path[i|(1<<k)][j|(1<<l)] = {k,l};
                        }
                    }
                }
                if(c>MM)MM=c, xx = i, yy = j;
            }
        }
        printf("%d\n",MM);
        vector<point>Res;
        while(xx){
            point t = Path[xx][yy];
            Res.push_back({t.x+1,t.y+1});
            xx -= (1<<t.x);
            yy -= (1<<t.y);
        }
        for(i=Res.size()-1;i>=0;i--)printf("%d %d\n",Res[i].x,Res[i].y);
    }
}
