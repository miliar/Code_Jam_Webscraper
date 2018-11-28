#include <bits/stdc++.h>


using namespace std;
const int N = 66;
const double eps = 0.01;
struct Edge {
    int v, w, next;
}e[1000000];
int need[N];
int n , p;
int have[N][N];
int l[N][N], r[N][N];
int head[N * N * 10], tot, level[N * N * 10], cur[N * N * 10];
int source, sink, M;
void _add (int u , int v , int w) {
    e[tot].v = v;
    e[tot].w = w;
    e[tot].next = head[u];
    head[u] = tot ++;
}
void add (int u , int v , int w) {
    // cout << u << " " << v << endl;
    _add(u, v , w);
    _add(v , u , 0);
}
bool bfs(){
    queue<int> q;
    memset(level,-1,sizeof(level));
    level[source] = 0;
    q.push(source);
    while(! q.empty()){
        int u = q.front();q.pop();
        for(int i = head[u];i != -1;i = e[i].next){
            int v = e[i].v;
            if(e[i].w && level[v] == -1){
                level[v] = level[u] + 1;
                q.push(v);
            }
        }
    }
    return level[sink] != -1;
}
int dfs(int u,int flow){
    if(u == sink) return flow;
    int tmp = flow;
    for(int &i = cur[u];i != -1;i = e[i].next){
        int v = e[i].v;
        if(e[i].w && level[v] == level[u] + 1){
            int add = dfs(v,min(e[i].w,tmp));
            tmp -= add;
            e[i].w -= add;
            e[i ^ 1].w += add;
            if(! tmp) break;
        }
    }
    return flow - tmp;
}
int dinic(){
    int maxFlow = 0;
    while(bfs()){
        for(int i = 0;i < M ;i ++)
            cur[i] = head[i];
        maxFlow += dfs(source,int(1e9));
    }
    return maxFlow;
}




int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t --) {
        tot = 0;memset (head , -1, sizeof (head));
        printf("Case #%d: ", ++ cas);
        scanf("%d %d", &n, &p);
        for(int i = 0 ; i < n ; i ++)
            scanf("%d" , &need[i]);
        for(int i = 0 ; i < n ; i ++) {
            for(int j = 0 ; j < p ; j ++) {
                scanf("%d" , &have[i][j]);
                int m = have[i][j] / need[i];
                l[i][j] = -1;
                r[i][j] = -1;

                for(int k = m + 10 ; ; k --) {
                    int gao = k * need[i];
                    if(have[i][j] + 0.0 >= (gao * 0.9 - eps) && have[i][j] + 0.0 <= (gao * 1.1 + eps)) {
                        l[i][j] = k;
                    }
                    if(have[i][j] > gao * 1.1 + 1) {
                        break;
                    }
                }
                for(int k = m - 10 ; ; k ++) {
                    int gao = k * need[i];
                    if(have[i][j] + 0.0 >= (gao * 0.9 - eps) && (have[i][j] + 0.0 <= gao * 1.1 + eps)) {
                        r[i][j] = k;
                    }
                    if(have[i][j] < gao * 0.9 - 1) {
                        break;
                    }
                }
                // cout << i << " " << j << " " << l[i][j] << " " << r[i][j] << endl;
            }
        }
        source = 0;sink = n * p * 2 + 1;
        M = n * p * 2 + 2;
        for(int i = 0 ;i < p; i ++) {
                if(l[0][i] == -1 || r[0][i] == -1) continue;
            add(source, i * 2 + 1, 1);
        }
        for(int i = 0 ; i < n ; i ++) {
            for(int j = 0 ; j < p ; j ++) {
                add((i * p + j) * 2 + 1, (i * p + j) * 2 + 2, 1);
            }
        }
        for(int i = 0 ; i < n - 1 ; i ++) {
            for(int j = 0 ; j < p ; j ++) {
                int A = (i * p + j) * 2 + 2;
                for (int k = 0 ; k < p ; k ++) {
                    int B = ((i + 1) * p + k) * 2 + 1;
                    if(l[i + 1][k] == -1 || r[i + 1][k] == -1) continue;
                    if(max(l[i][j], l[i + 1][k]) <= min(r[i][j], r[i + 1][k])) {
                        add(A, B, 1);
                    }
                }
            }
        }
        for(int i = 0 ; i < p ; i ++) {
                if(l[n - 1][i] == -1 || r[n - 1][i] == -1) continue;
            int A = ((n - 1) * p + i) * 2 + 2;
            add(A, sink, 1);
        }
        printf("%d\n", dinic());
    }


    return 0;
}