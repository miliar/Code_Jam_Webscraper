#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, EC, w1[110][110], sink;
char p[110][110], q[110][110];
struct Edge{
    int e, f;
}E[101000];
vector<int>G[1000];
void Make_Edge(int a, int b, int c){
    G[a].push_back(EC);
    G[b].push_back(EC+1);
    E[EC++] = {b,c};
    E[EC++] = {a,0};
}
int Level[1000], PV[1000], Q[1000];
bool GetLevel(){
    int i, head = 0, tail = 0;
    for(i=0;i<=sink;i++)Level[i] = -1;
    Level[0] = 0, Q[++tail] = 0;
    while(head < tail){
        int x = Q[++head];
        for(i=0;i<G[x].size();i++){
            Edge tp = E[G[x][i]];
            if(tp.f && Level[tp.e] == -1){
                Level[tp.e] = Level[x] + 1;
                Q[++tail] = tp.e;
            }
        }
    }
    return Level[sink] != -1;
}
int BlockFlow(int a){
    if(a==sink)return 1;
    for(int &i = PV[a];i>=0;i--){
        Edge &tp = E[G[a][i]];
        if(tp.f && Level[tp.e] == Level[a] + 1){
            if(BlockFlow(tp.e)){
                E[G[a][i]].f--;
                E[G[a][i]^1].f++;
                return 1;
            }
        }
    }
    return 0;
}
int Flow(){
    int i, r = 0;
    while(GetLevel()){
        for(i=0;i<=sink;i++)PV[i] = G[i].size()-1;
        while(BlockFlow(0))r++;
    }
    return r;
}
bool Find(int a, int b){
    int i;
    for(i=0;i<G[a].size();i++){
        if(E[G[a][i]].e==b && !E[G[a][i]].f)return true;
    }
    return false;
}
int F[1000];
int main(){
    freopen("/Users/joseunghyeon/Downloads/D-large.in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code2/output.txt","w",stdout);
    int TC, TT, i, j;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%d%d",&n,&m);
        EC = 0;
        char pp[10];
        int s = m;
        for(i=1;i<=n;i++)for(j=1;j<=n;j++)p[i][j]=0;
        for(i=0;i<m;i++){
            int x, y;
            scanf("%s%d%d",pp,&x,&y);
            if(pp[0]=='o')s++;
            p[x][y] = pp[0];
        }
        for(i=1;i<=n*6;i++)F[i] = 1;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(p[i][j]=='x' || p[i][j]=='o')F[i]=F[j+n]=0;
                Make_Edge(i, j+n, 1);
                if(p[i][j]=='+' || p[i][j]=='o')F[n*2+i+j]=F[n*5+i-j]=0;
                Make_Edge(n*2+i+j, n*5+i-j, 1);
            }
        }
        sink = n*6+1;
        for(i=1;i<=n*6;i++){
            int t = (i-1)/n;
            if(t==0 || t==2 || t==3) Make_Edge(0,i,F[i]);
            else Make_Edge(i,sink,F[i]);
        }
        printf("%d",s+Flow());
        int cc = 0;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                int c = 0;
                if(p[i][j]=='o')c=3;
                if(p[i][j]=='x')c=2;
                if(p[i][j]=='+')c=1;
                if(Find(i,j+n))c|=2;
                if(Find(n*2+i+j,n*5+i-j))c|=1;
                q[i][j]=0;
                if(c==1)q[i][j]='+';
                if(c==2)q[i][j]='x';
                if(c==3)q[i][j]='o';
                if(p[i][j]!=q[i][j]){
                    cc++;
                }
            }
        }
        printf(" %d\n",cc);
        for(i=1;i<=n;i++)for(j=1;j<=n;j++)if(p[i][j]!=q[i][j])printf("%c %d %d\n",q[i][j],i,j);
        for(i=0;i<=sink;i++)G[i].clear();
    }
}
