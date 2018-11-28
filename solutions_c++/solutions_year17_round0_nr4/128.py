#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iomanip>
#include <map>
#include <cmath>
#include <deque>
using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef pair<ll,ll> l4;
const int maxn = 30010;
const double eps = 1e-8;
const int inf = 1e9;
const int des = 24000;
const int layer1 = 20000;
const int layer2 = 21000;
const int layer3 = 22000;
const int layer4 = 23000;
struct edge{
    int from,to,cap,flow;
    edge(){}
    edge(int from,int to,int cap,int flow):from(from),to(to),cap(cap),flow(flow){}
};

struct Dinic{
    int n,m,s,t;
    vector<edge> edges;
    vector<int > G[maxn];
    bool vis[maxn];
    int cur[maxn];
    int d[maxn];
    
    void addedge(int from,int to,int cap){
        edges.push_back(edge(from,to,cap,0));
        edges.push_back(edge(to,from,0,0));
        m=edges.size();
        G[from].push_back(m-2);
        G[to].push_back(m-1);
    }
    
    bool bfs(){
        memset(vis,0,sizeof(vis));
        queue <int> Q;
        Q.push(s);
        d[s]=0;
        vis[s]=1;
        while(!Q.empty()){
            int x=Q.front();
            Q.pop();
            for(int i=0;i<G[x].size();i++){
                edge &e=edges[G[x][i]];
                if(!vis[e.to]&&e.cap>e.flow){
                    vis[e.to]=1;
                    d[e.to]=d[x]+1;
                    Q.push(e.to);
                }
            }
        }
        return vis[t];
    }
    int dfs(int x,int a){
        if(x==t||a==0) return a;
        int flow=0;
        int f;
        for(int &i=cur[x];i<G[x].size();i++){
            edge &e=edges[G[x][i]];
            if((d[e.to]==d[x]+1)&&(f=dfs(e.to,min(e.cap-e.flow,a)))>0){
                e.flow+=f;
                edges[G[x][i]^1].flow-=f;
                flow+=f;
                a-=f;
                if(a==0) break;
            }
        }
        return flow;
    }
    
    int maxflow(int a,int b){
        s=a;t=b;
        int flow=0;
        while(bfs()){
            memset(cur,0,sizeof(cur));
            flow+=dfs(s,inf);
        }
        return flow;
    }
};

int T;
int n,m;
char ch;
int r,c;
int pt[200][200];
int ptafter[200][200];
int row[200];
int col[200];
int dia1[300];
int dia2[300];
int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        Dinic FL;
        memset(pt, 0, sizeof(pt));
        memset(ptafter, 0, sizeof(ptafter));
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        memset(dia1, 0, sizeof(dia1));
        memset(dia2, 0, sizeof(dia2));
        cin >> n >> m;
        int ans = 0;
        for (int i = 0; i < m; i++) {
            cin >> ch >> r >> c;
            if (ch == 'o') {
                ans += 2;
                row[r] = 1;
                col[c] = 1;
                dia1[r+c] = 1;
                dia2[r-c+100] = 1;
                pt[r][c] = 3;
            } else if (ch == '+') {
                dia1[r+c] = 1;
                dia2[r-c+100] = 1;
                ans++;
                pt[r][c] = 1;
            } else {
                row[r] = 1;
                col[c] = 1;
                ans++;
                pt[r][c] = 2;
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                FL.addedge(layer1+i, (i-1)*100+j, 1);
                FL.addedge((i-1)*100+j, layer2+j, 1);
                FL.addedge(layer3+i+j, (i-1)*100+j+10000, 1);
                FL.addedge((i-1)*100+j+10000, layer4+i-j, 1);
            }
        }
        for (int i = 1; i <= n; i++) {
            if (!row[i]) {
                FL.addedge(0, layer1+i, 1);
            }
            if (!col[i]) {
                FL.addedge(layer2+i, des, 1);
            }
        }
        for (int i = 2; i <= 2*n; i++) {
            if (!dia1[i]) {
                FL.addedge(0, layer3+i, 1);
            }
        }
        for (int i = 1-n; i <= n-1; i++) {
            if (!dia2[i+100]) {
                FL.addedge(layer4+i, des, 1);
            }
        }
        cout << FL.maxflow(0, des)+ans << " " ;
        memcpy(ptafter, pt, sizeof(pt));
        for (auto e : FL.edges) {
            if (e.from <= 10000) {
                if (e.flow) {
                    e.from--;
                    int r = e.from/100+1;
                    int c = e.from%100+1;
                    ptafter[r][c] |= 2;
                }
            } else if (e.flow <= 20000) {
                if (e.flow) {
                    e.from -= 10001;
                    int r = e.from/100+1;
                    int c = e.from%100+1;
                    ptafter[r][c] |= 1;
                }
            }
        }
        int z = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (ptafter[i][j] != pt[i][j]) {
                    z++;
                }
            }
        }
        printf("%d\n",z);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (ptafter[i][j] != pt[i][j]) {
                    if (ptafter[i][j] == 1) {
                        printf("+ ");
                    } else if (ptafter[i][j] == 2) {
                        printf("x ");
                    } else {
                        printf("o ");
                    }
                    printf("%d %d\n",i,j);
                }
            }
        }
    }
    return 0;
}
