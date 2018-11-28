#include <bits/stdc++.h>
using namespace std;

class matcher{ public:

    static const int MAXN1 = 202;
    static const int MAXN2 = 202;
    static const int MAXM = 40404;

    int n1, n2, edges, last[MAXN1], prev[MAXM], head[MAXM];
    int matching[MAXN2], dist[MAXN1], Q[MAXN1];
    bool used[MAXN1], vis[MAXN1];

    void init(int _n1, int _n2) {
        n1 = _n1;
        n2 = _n2;
        edges = 0;
        fill(last, last + n1, -1);
    }

    void add_edge(int u, int v) {
        head[edges] = v;
        prev[edges] = last[u];
        last[u] = edges++;
    }

    void bfs() {
        fill(dist, dist + n1, -1);
        int sizeQ = 0;
        for (int u = 0; u < n1; ++u) {
            if (!used[u]) {
                Q[sizeQ++] = u;
                dist[u] = 0;
            }
        }
        for (int i = 0; i < sizeQ; i++) {
            int u1 = Q[i];
            for (int e = last[u1]; e >= 0; e = prev[e]) {
                int u2 = matching[head[e]];
                if (u2 >= 0 && dist[u2] < 0) {
                    dist[u2] = dist[u1] + 1;
                    Q[sizeQ++] = u2;
                }
            }
        }
    }

    bool dfs(int u1) {
        vis[u1] = true;
        for (int e = last[u1]; e >= 0; e = prev[e]) {
            int v = head[e];
            int u2 = matching[v];
            if (u2 < 0 || !vis[u2] && dist[u2] == dist[u1] + 1 && dfs(u2)) {
                matching[v] = u1;
                used[u1] = true;
                return true;
            }
        }
        return false;
    }

    int max_matching() {
        fill(used, used + n1, false);
        fill(matching, matching + n2, -1);
        for (int res = 0;;) {
            bfs();
            fill(vis, vis + n1, false);
            int f = 0;
            for (int u = 0; u < n1; ++u)
                if (!used[u] && dfs(u))
                    ++f;
            if (!f)
                return res;
            res += f;
        }
    }

};


void solve(){
    int n,m;
    int tier[101][101] = {};
    bool use_x[101] = {};
    bool use_y[101] = {};
    bool use_sum[202] = {};
    bool use_diff[202] = {};
    bool exist[202][202] = {};
    bool Plus[101][101] = {};
    bool Cross[101][101] = {};
    matcher mat;
    queue<string> answer;
    int score=0, cnt=0;

    cin >> n >> m;
    mat.init(201,201);
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            exist[i+j][i+100-j] = 1;
        }
    }

    for(int i=1; i<=m; i++){
        char c;
        int a, b;
        cin >> c >> a >> b;
        tier[a][b] = 0;
        if(c=='x' || c=='o'){
            Cross[a][b] = 1;
            use_x[a] = 1;
            use_y[b] = 1;
            tier[a][b] ++;
        }
        if(c=='+' || c=='o'){
            Plus[a][b] = 1;
            use_sum[a+b] = 1;
            use_diff[a+100-b] = 1;
            tier[a][b] ++;
        }
    }

    for(int i=1; i<=200; i++){
        for(int j=1; j<=200; j++){
            if(!use_sum[i] && !use_diff[j] && exist[i][j]){
                mat.add_edge(i,j);
            }
        }
    }

    mat.max_matching();
    for(int i=1; i<=200; i++){
        if(mat.matching[i] != -1){
            int a = mat.matching[i];
            int b = i;
            int x = (a+b-100)/2;
            int y = (a-b+100)/2;
            Plus[x][y] = 1;
        }
    }

    int p=1, q=1;
    while(p<=n && q<=n){
        if(use_x[p]){
            p++;
        }
        else if(use_y[q]){
            q++;
        }
        else{
            Cross[p][q]=1;
            use_x[p]=1;
            use_y[q]=1;
        }
    }

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            int new_tier = 0;
            if(Plus[i][j]) new_tier++;
            if(Cross[i][j]) new_tier++;
            if(Plus[i][j] && Cross[i][j]){
                if(new_tier>tier[i][j]){
                    string s = "o " + to_string(i) + " " + to_string(j);
                    answer.push(s);
                    cnt++;
                }
                score+=2;
            }
            else if(Plus[i][j]){
                if(new_tier>tier[i][j]){
                    string s = "+ " + to_string(i) + " " + to_string(j);
                    answer.push(s);
                    cnt++;
                }
                score++;
            }
            else if(Cross[i][j]){
                if(new_tier>tier[i][j]){
                    string s = "x " + to_string(i) + " " + to_string(j);
                    answer.push(s);
                    cnt++;
                }
                score++;
            }
        }
    }
    cout << score << " " << cnt << endl;
    while(!answer.empty()){
        cout << answer.front() << endl;
        answer.pop();
    }
}

int main(){
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
    }
}
