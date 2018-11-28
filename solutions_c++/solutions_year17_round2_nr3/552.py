#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>

using namespace std;
typedef long long ll;
typedef double db;
const int N = 105;
const db inf = 1e15;
const ll INF = 0xfffffffffffffff;
int d[N][N];
ll min_d[N][N];
db t[N];
int e[N],s[N];
queue<int> Q;
vector<int> to[N];
bool in[N];
int n;
void dfs(int k,int y,int v,db min_t) {
    if(min_t<t[k]) {
        t[k] = min_t;
        if(!in[k]) Q.push(k),in[k]=true;
    }
    for(int i=0; i<n; i++) {
        if(d[k][i]>0&&y>=d[k][i]) {
            dfs(i, y-d[k][i], v, min_t + (db)d[k][i]/(db)v);
        }
    }
}

db spfa(int st,int ed) {
    for(int i=0; i<n; i++) t[i] = inf,in[i] =false;;
    t[st] = 0,in[st]=true;
    Q.push(st);
    while(!Q.empty()) {
        int now = Q.front();
        Q.pop();
        in[now]=false;
        for(int i=0;i<to[now].size();i++) {
            int nxt = to[now][i];
//            if(now==0&&nxt==3) printf("%d  %d ==\n",now,nxt);
            db tmp = t[now] + (db)min_d[now][nxt]/(db)s[now];
            if(tmp < t[nxt]){
                t[nxt] = tmp;
                if(!in[nxt]) Q.push(nxt),in[nxt]=true;
            }
        }
//        dfs(now, e[now], s[now], t[now]);
    }
    return t[ed];
}

int main() {
#ifdef PKWV
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
#endif // PKWV
    int T;
    scanf("%d",&T);
    for(int ca=1; ca<=T; ca++) {
        int q;
        scanf("%d%d",&n,&q);
        for(int i=0; i<n; i++) scanf("%d%d",&e[i],&s[i]);
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) scanf("%d",&d[i][j]),min_d[i][j]=d[i][j];
        }
        for(int k=0;k<n;k++) {
            for(int i=0;i<n;i++) {
                for(int j=0;j<n;j++) {
                    if(min_d[i][k]>0&&min_d[k][j]>0) {
                        if(min_d[i][j]==-1) min_d[i][j]=INF;
                        min_d[i][j] = min(min_d[i][j], min_d[i][k]+min_d[k][j]);
                    }
                }
            }
        }
        for(int i=0;i<n;i++) {
            to[i].clear();
            for(int j=0;j<n;j++) {
                if(min_d[i][j]<=e[i] && min_d[i][j]>0) to[i].push_back(j);
            }
        }
        printf("Case #%d: ",ca);
        for(int j=0; j<q; j++) {
            int st,ed;
            scanf("%d%d",&st,&ed);
            db res = spfa(st-1,ed-1);
            printf(" %f",res);
        }
        printf("\n");
    }
    return 0;
}
