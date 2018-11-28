#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
#define x first
#define y second
constexpr int maxn = 1005;
int c[maxn][maxn], f[maxn][maxn], e[maxn], h[maxn];
void push(int u, int v) {
    int x = min(c[u][v] - f[u][v], e[u]);
    if(x) {
        f[u][v] += x;
        f[v][u] -= x;
        e[u] -= x;
        e[v] += x;
    }
}
void relabel(int u, int n) {
    h[u] = 2 * n;
    for(int i = 0; i < n; i++)
        if(c[u][i] > f[u][i])
            h[u] = min(h[u], h[i] + 1);
}
void discharge(int u, int n) {
    while(e[u]) {
        for(int i = 0; i < n && e[u]; i++)
            if(h[u] == h[i] + 1)
                push(u, i);
        if(e[u])
            relabel(u, n);
    }
}
int max_flow(int s, int t, int n) {
    for(int i = 0; i < n; i++)
        fill_n(f[i], n, 0);
    for(int i = 0; i < n; i++) {
        f[s][i] = e[i] = c[s][i];
        f[i][s] = -f[s][i];
    }
    fill_n(h, n, 0);
    h[s] = n;
    list<int> q;
    for(int i = 0; i < n; i++)
        if(i != s && i != t)
            q.push_back(i);
    for(auto i = q.begin(); i != q.end(); ++i) {
        int oh = h[*i];
        discharge(*i, n);
        int nh = h[*i];
        if(oh != nh)
            q.splice(q.begin(), q, i);
    }
    return accumulate(f[s], f[s] + n, 0);
}

int is[1005][1005];
vector<int> arr[1005];
int main(){
    int t,C=0, inf=10000;
    scanf("%d",&t);
    while(t--){
        memset(c,0,sizeof(c));
        int n,k,m;
        scanf("%d%d%d",&n,&k,&m);
        for(int i=0;i<k;i++) arr[i].clear();
        int top=0;
        for(int i=0;i<m;i++){
            int x,y;
            scanf("%d%d",&x,&y);
            y--;
            arr[y].push_back(x);
        }
        int NN = arr[0].size() + arr[1].size() + 2;
        int N = arr[0].size();
        int M = arr[1].size();
        for(int i=0;i<N;i++) c[NN-2][i]=inf;
        for(int i=0;i<M;i++) c[i+N][NN-1]=inf;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(arr[0][i]!=arr[1][j]){
                    c[i][j+N] = inf;
                }
                /*else if (arr[0][i]!=1){
                    c[i][j+N] = inf - 1;
                }*/
            }
        }
        int sum = max_flow(NN - 2, NN - 1, NN);
        int pre = sum / inf;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(arr[0][i]!=arr[1][j]){
                    c[i][j+N] = inf;
                }
                else if (arr[0][i]!=1){
                    c[i][j+N] = inf ;
                }
            }
        }
        sum = max_flow(NN - 2, NN - 1, NN);
        int ans = sum / inf;
        int cnt = ans - pre;
        printf("Case #%d: %d %d\n",++C,N + M - ans,cnt);
    }
}
