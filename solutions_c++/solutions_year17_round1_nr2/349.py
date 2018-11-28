#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <queue>
#include <map>
#include <cmath>

using namespace std;


const int MAXN = 5555555,MAXE = MAXN*10,INF = 0x3f3f3f3f;
int head[MAXN],ed[MAXE],nxt[MAXE],cap[MAXE],q;
int n;
void clr(){
    memset(head, 0, sizeof(head));
    q = 2;
}
void ade(int f,int t,int c){
    ed[q] = t;
    cap[q] = c;
    nxt[q] = head[f];
    head[f] = q++;
}
void nfade(int f,int t,int c){
    ade(f,t,c);
    ade(t,f,0);
}
bool vis[MAXN];
int dis[MAXN];
bool dinic_bfs(int start,int end){
    memset(vis, 0, sizeof(vis));
    queue<int> que;
    que.push(start);
    dis[start] = 0;
    vis[start] = true;
    while(!que.empty()){
        int u = que.front();
        que.pop();
        for(int i = head[u];i;i = nxt[i]){
            int v = ed[i];
            if (!vis[v] && cap[i]) {
                dis[v] = dis[u] + 1;
                vis[v] = true;
                que.push(v);
            }
        }
    }
    return vis[end];
}
int cur[MAXN];
int dinic_dfs(int u,int a,int start,int end){
    if (u == end || a == 0) {
        return a;
    }
    int flow = 0,f;
    for(int &i = cur[u];i;i = nxt[i]){
        int v =  ed[i];
        if(dis[u] + 1 == dis[v] &&
           (f = dinic_dfs(v, min(a,cap[i]), start, end)) > 0){
            flow += f;
            a -= f;
            cap[i] -= f;
            cap[i^1] += f;
            if (a == 0) {
                break;
            }
        }
    }
    return flow;
}
int dinic(int start,int end){
    int ret = 0;
    while (dinic_bfs(start, end)) {
        for(int i = 1; i <= n; i++){
            cur[i] = head[i];
        }
        ret += dinic_dfs(start, INF, start, end);
    }
    return ret;
}

int N,P;
int sig[55],qty[55][55];
int ss,tt;
int tot;
map<int,pair<int,int> > vertid[55];
inline int normalpt(int r,int c){
    return P*(r-1)+c+2;
}
void buildgph(){
    clr();
    ss = 1,tt = 2;
    tot = N*P+2;
    for(int i = 1;i <= N; i++){
        vertid[i].clear();
    }
    
    for(int i = 1;i <= N; i++){
        for(int j = 1;j <= P; j++){
            int r = (int)(floor((double)qty[i][j]/0.9/(double)sig[i])+0.5);
            int l = (int)(ceil((double)qty[i][j]/1.1/(double)sig[i])+0.5);
            if(l > 0 && l <= r){
                for(int k = l;k <= r; k++){
                    if(!vertid[i].count(k)){
                        vertid[i][k] = make_pair(tot+1,tot+2);
                        tot += 2;
                    }
                    nfade(vertid[i][k].first,normalpt(i,j),1);
                    nfade(normalpt(i,j),vertid[i][k].second,1);
                }
            }
        }
        if(i == 1){
            //from source
            for(int j = 1;j <= P; j++){
                nfade(ss,normalpt(i, j),1);
            }
        }
        if(i > 1){
            //interconnections
            for(map<int,pair<int,int> > :: iterator it = vertid[i].begin(); it != vertid[i].end(); it++){
                if(vertid[i-1].count(it->first)){
                    nfade(vertid[i-1][it->first].second, it->second.first,INF);
                }
            }
        }
        if(i == N){
            //to sink
            for(map<int,pair<int,int> > ::iterator it = vertid[i].begin(); it != vertid[i].end(); it++){
                nfade(it->second.second,tt,INF);
            }
        }
    }
    n = tot;
}

void solve(){
    buildgph();
    int res = dinic(ss,tt);
    printf("%d\n",res);
}

int main(int argc, char *argv[]){
    
    int caseCnt;
    scanf(" %d",&caseCnt);
    for(int d = 1;d <= caseCnt ;d++){
        printf("Case #%d: ",d);
        scanf(" %d %d",&N,&P);
        for(int i = 1;i <= N; i++){
            scanf(" %d",&sig[i]);
        }
        for(int i = 1;i <= N; i++){
            for(int j = 1;j <= P; j++){
                scanf(" %d",&qty[i][j]);
            }
        }
        solve();
    }
    
    
    return 0;
}
