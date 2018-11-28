#include <bits/stdc++.h>
#define N 509
using namespace std;

int nodes, src, dest;
int dist[N],q[N],work[N];
struct edge{ int to,rev; int f,cap; }; //{to, rev, f, cap}
vector<edge> g[N];
void addEdge(int s,int t,int cap){ //
    edge e1 = {t, g[t].size(), 0, cap};
    edge e2 = {s, g[s].size(), cap, cap}; //set f=0 for bidirectional
    g[s].push_back(e1);
    g[t].push_back(e2);
}
bool bfs(){
    memset(dist,-1,sizeof dist);
    dist[src]=0;
    int qt=0; q[qt++]=src;
    for(int qh=0;qh<qt;qh++){
        int u=q[qh];
        for(int j=0;j<g[u].size();j++){
            edge &e=g[u][j];
            int v=e.to;
            if(dist[v]<0&&e.f<e.cap){
                dist[v]=dist[u]+1;
                q[qt++]=v;
            }
        }
    }
    return dist[dest]>=0;
}
int dfs(int u,int f){
    //printf("%d ",u);
    if(u==dest) return f;
    for(int &i=work[u];i<g[u].size();i++){
        edge &e=g[u][i];
        if(e.cap<=e.f) continue;
        int v=e.to;
        if(dist[v]==dist[u]+1){
            int df=dfs(v,min(f,e.cap-e.f));
            if(df>0){
                e.f+=df; g[v][e.rev].f-=df;
                return df;
            }
        }
    }
    return 0;
}
int dinic(int s,int t){
    src=s; dest=t;
    int ret=0;
    while(bfs()){
        memset(work,0,sizeof work);
        //printf("--> ");
        while(int delta=dfs(src,INT_MAX))
            ret+=delta;
        //printf("\n--> %d\n",ret);
    }
    return ret;
}

void reset(int n){
    for(int i=0;i<4*n+2;i++) g[i].clear();
    memset(dist,0,sizeof dist);
    memset(work,0,sizeof work);
    memset(q,0,sizeof q);
}

char a[N][N],b[N][N];
void solve(int tc){
    printf("Case #%d: ",tc);
    int n,k; scanf("%d%d",&n,&k);
    nodes = n+n+2;
    int sc = 0;
    for(int i=1;i<=n;i++){
        memset(a[i]+1,'.',sizeof(a[0][0])*n);
    }
    while(k--){
        char ch[2]; int r,c;
        scanf("%s%d%d",ch,&r,&c);
        a[r][c]=ch[0];
        if(ch[0]=='o') sc+=2;
        else sc++;
    }

    // for case 'x'
    for(int i=1;i<=n;i++){
        addEdge(0,i,1); addEdge(i+n,n+n+1,1);
        for(int j=1;j<=n;j++){
            b[i][j]=a[i][j];
            // build x
            if(a[i][j]=='.'||a[i][j]=='+'){
                int k;
                for(k=1;k<=n;k++){
                    if(a[i][k]=='x'||a[i][k]=='o') break;
                }
                if(k>n){
                    for(k=1;k<=n;k++){
                        if(a[k][j]=='x'||a[k][j]=='o') break;
                    }
                    if(k>n) addEdge(i,j+n,1);
                }
            }
        }
    }
    int add = dinic(0,n+n+1);
    for(int i=1;i<=n;i++){
        for(edge e: g[i]){
            if(e.to<=n||e.to>n+n) continue;
            if(e.f) b[i][e.to-n]=(b[i][e.to-n]=='.'?'x':'o');
        }
    }
    reset(n);


    // for case '+'
    nodes = 4*n+1;
    for(int i=1;i<n+n;i++){
        addEdge(0,i,1); addEdge(4*n+1-i,n+n,1);
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            //build +
            if(a[i][j]=='.'||a[i][j]=='x'){
                int k;
                for(k=1;k<=n;k++){
                    int l=i+j-k;
                    if(1>l||l>n) continue;
                    if(a[k][l]=='+'||a[k][l]=='o') break;
                }
                if(k>n){
                    for(k=1;k<=n;k++){
                        int l=j-i+k;
                        if(1>l||l>n) continue;
                    //if(i==6&&j==6) printf("[%d %d] -> %c\n",k,l,a[k][l]);
                        if(a[k][l]=='+'||a[k][l]=='o') break;
                    }
                    if(k>n) addEdge(i-j+n,i+j+n+n,1);
                }
            }
        }
    }
    /*for(int i=0;i<nodes;i++){
        for(edge e: g[i]){
            printf("%d->%d: %d/%d\n",i,e.to,e.f,e.cap);
        }
    }*/
    add += dinic(0,n+n);
    for(int i=1;i<n+n;i++){
        for(edge e: g[i]){
            int r=(i+e.to-3*n)/2, c=(e.to-i-n)/2;
            if(c<1||c>n) continue;
            if(e.f) b[r][c]=(b[r][c]=='.'?'+':'o');
        }
    }
    reset(n);
    int cnt=0;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(a[i][j]!=b[i][j]) cnt++;
        }
    }
    printf("%d %d\n",sc+add,cnt);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(a[i][j]!=b[i][j]) printf("%c %d %d\n",b[i][j],i,j);
        }
    }
}

int main()
{
    freopen("D-large.in","r",stdin); freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        solve(tc);
    }
    return 0;
}
