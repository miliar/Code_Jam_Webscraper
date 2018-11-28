#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, Num[110][110][4], cnt, K, SCC[20100], ord[20100];
vector<int>E[20100], F[20100];
bool v[20100];
struct AA{
    int x, y, dir;
};
vector<AA>TP;
struct point{
    int x, y;
}w[5000];
char p[110][110];
int dx[3][4]={{1,-1,0,0},{0,0,1,-1},{0,0,-1,1}};
int dy[3][4]={{0,0,1,-1},{1,-1,0,0},{-1,1,0,0}};
int ddir[3][4]={{0,1,2,3},{2,3,0,1},{3,2,1,0}};
bool Pos(int x, int y, int dir){
    if(p[x][y]=='#')return true;
    if(p[x][y]=='|' || p[x][y]=='-')return false;
    TP.push_back({x,y,dir});
    int ck;
    if(p[x][y]=='.')ck = 0;
    else if(p[x][y]=='/')ck = 2;
    else ck = 1;
    return Pos(x+dx[ck][dir], y+dy[ck][dir], ddir[ck][dir]);
}
void Add_Edge(int a, int b){
    E[a].push_back(b);
    F[b].push_back(a);
}
void DFS(int a){
    int i;
    v[a]=true;
    for(i=0;i<E[a].size();i++){
        if(!v[E[a][i]])DFS(E[a][i]);
    }
    ord[++cnt] = a;
}
void DFS2(int a){
    SCC[a] = cnt;
    int i;
    for(i=0;i<F[a].size();i++){
        if(!SCC[F[a][i]])DFS2(F[a][i]);
    }
}
int main(){
    freopen("/Users/joseunghyeon/Downloads/C-small-attempt0 (2).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int i, j, k, l;
    int TT, TC;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++){
            scanf("%s",p[i]+1);
        }
        for(i=0;i<=n+1;i++){
            for(j=0;j<=m+1;j++){
                if(i==0||i==n+1||j==0||j==m+1)p[i][j]='#';
                for(k=0;k<4;k++)Num[i][j][k] = 0;
            }
        }
        cnt = 0;
        vector<int>t2;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                if(p[i][j] == '-' || p[i][j] == '|'){
                    cnt++;
                    w[cnt] = {i,j};
                    TP.clear();
                    if(Pos(i, j+1, 2) && Pos(i, j-1, 3)){
                        for(k=0;k<TP.size();k++){
                            Num[TP[k].x][TP[k].y][TP[k].dir] = cnt*2-1;
                        }
                    }
                    else{
                        t2.push_back(cnt*2-1);
                    }
                    TP.clear();
                    if(Pos(i-1, j, 1) && Pos(i+1, j, 0)){
                        for(k=0;k<TP.size();k++){
                            Num[TP[k].x][TP[k].y][TP[k].dir] = cnt*2;
                        }
                    }
                    else{
                        t2.push_back(cnt*2);
                    }
                }
            }
        }
        K = cnt*2;
        for(i=1;i<=2*K;i++){
            E[i].clear();
            F[i].clear();
        }
        for(i=0;i<t2.size();i++){
            Add_Edge(t2[i],t2[i]+K);
        }
        for(i=1;i<=cnt;i++){
            Add_Edge(i*2-1, i*2+K);
            Add_Edge(i*2, i*2-1+K);
            Add_Edge(i*2-1+K, i*2);
            Add_Edge(i*2+K, i*2-1);
        }
        int chk = 0;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                if(p[i][j]!='#' && p[i][j]!='-' && p[i][j] != '|'){
                    vector<int>ttt;
                    for(k=0;k<4;k++){
                        if(Num[i][j][k]){
                            int ck = 0;
                            for(l=0;l<ttt.size();l++)if(ttt[l]==Num[i][j][k])ck=1;
                            if(ck)continue;
                            ttt.push_back(Num[i][j][k]);
                        }
                    }
                    if(ttt.empty())chk = 1;
                    else if(ttt.size()==2){
                        Add_Edge(ttt[0]+K, ttt[1]);
                        Add_Edge(ttt[1]+K, ttt[0]);
                    }
                    else{
                        Add_Edge(ttt[0]+K, ttt[0]);
                    }
                }
            }
        }
        if(chk){
            printf("IMPOSSIBLE\n");
            continue;
        }
        cnt = 0;
        for(i=1;i<=K*2;i++)v[i]=false,SCC[i]=0;
        for(i=1;i<=K*2;i++){
            if(!v[i])DFS(i);
        }
        cnt = 0;
        for(i=K*2;i>=1;i--){
            if(!SCC[ord[i]]){
                cnt++;
                DFS2(ord[i]);
            }
        }
        for(i=1;i<=K;i++){
            if(SCC[i] == SCC[i+K])chk = 1;
            if(SCC[i] > SCC[i+K]){
                if(i%2==1){
                    p[w[(i+1)/2].x][w[(i+1)/2].y] = '-';
                }
                else{
                    p[w[(i+1)/2].x][w[(i+1)/2].y] = '|';
                }
            }
        }
        if(chk){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("POSSIBLE\n");
            for(i=1;i<=n;i++){
                for(j=1;j<=m;j++){
                    printf("%c",p[i][j]);
                }
                printf("\n");
            }
        }
    }
}
