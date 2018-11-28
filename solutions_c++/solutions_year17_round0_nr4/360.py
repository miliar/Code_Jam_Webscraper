#include<bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<char> > G;

int V, edge_cnt, source, sink;

vector<int> last_edge, nxt_edge, oppo, capa;

void init() {
    edge_cnt = 0, last_edge.clear(), nxt_edge.clear(), oppo.clear(), capa.clear(), last_edge = vector<int>(V, -1);
}

void add(int u, int v, int capa_) {
    nxt_edge.push_back(last_edge[u]), last_edge[u] = edge_cnt, oppo.push_back(v), capa.push_back(capa_), edge_cnt++;
}

vector<int> dist;

bool bfs() {
    dist.clear(), dist = vector<int>(V, -1);
    queue<int> q;
    q.push(source), dist[source] = 0;
    while(!q.empty()) {
        int now = q.front();
        q.pop();

        for(int i = last_edge[now]; i != -1; i = nxt_edge[i]) {
            int nxt = oppo[i];
            if(capa[i] && dist[nxt] == -1) {
                dist[nxt] = dist[now] + 1;
                q.push(nxt);
            }
        }
    }
    if(dist[sink] == -1) return false;
    else return true;
}

vector<int> last_edge2;

int dfs(int now, int flow) {
    if(now == sink) return flow;

    for(int i = last_edge2[now]; i != -1; i = nxt_edge[i]) {
        last_edge2[now] = i;

        int nxt = oppo[i];
        if(capa[i] && dist[nxt] == dist[now] + 1) {
            if(int tmp = dfs(nxt, min(capa[i], flow))) {
                capa[i] -= tmp;
                capa[i^1] += tmp;
                return tmp;
            }
        }
    }
    return 0;
}

int dinic() {
    int total_flow = 0;
    while(bfs()) {
        last_edge2 = last_edge;
        while(int tmp = dfs(source, 1e9))
            total_flow += tmp;
    }
    return total_flow;
}

vector<vector<char> > A;

void main2(int tc) {
    scanf("%d %d", &N, &M);
    G.clear();
    A.clear();
    A = G = vector<vector<char> >(N, vector<char>(N, '.'));
    int tot = 0;
    for(int i = 0; i < M; i++) {
        char ch;
        int r, c;
        scanf("\n%c %d %d", &ch, &r, &c);
        r--; c--;
        G[r][c] = ch;
        if(ch == '+' || ch == 'x') tot++;
        else tot += 2;
    }

    V = 2*N + 2, source = V - 2, sink = V - 1;
    init();

    for(int i = 0; i < N; i++) {
        bool poss = true;
        for(int j = 0; j < N; j++) {
            if(G[i][j] == 'x' || G[i][j] == 'o') {
                poss = false;
                break;
            }
        }
        if(poss) {
            add(source, i, 1);
            add(i, source, 0);
        }
    }
    for(int i = 0; i < N; i++) {
        bool poss = true;
        for(int j = 0; j < N; j++) {
            if(G[j][i] == 'x' || G[j][i] == 'o') {
                poss = false;
                break;
            }
        }
        if(poss) {
            add(N + i, sink, 1);
            add(sink, N + i, 0);
        }
    }
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            add(i, N + j, 1);
            add(N + j, i, 0);
        }
    }
    tot += dinic();

    for(int i = 0; i < N; i++) {
        for(int j = last_edge[i]; j != -1; j = nxt_edge[j]) {
            int k = oppo[j];
            if(k == source) continue;
            if(!capa[j]) {
                if(G[i][k - N] == '.') A[i][k - N] = 'x';
                else A[i][k - N] = 'o';
            }
        }
    }

    V = 4*N + 2, source = V - 2, sink = V - 1;
    init();

    for(int i = -(N - 1); i <= N - 1; i++) {
        bool poss = true;
        for(int j = 0; j < N; j++) {
            int k = j - i;
            if(k < 0 || N <= k) continue;
            if(G[j][k] == '+' || G[j][k] == 'o') {
                poss = false;
                break;
            }
        }
        if(poss) {
            add(source, i + N, 1);
            add(i + N, source, 0);
        }
    }
    for(int i = 0; i <= 2*(N - 1); i++) {
        bool poss = true;
        for(int j = 0; j < N; j++) {
            int k = i - j;
            if(k < 0 || N <= k) continue;
            if(G[j][k] == '+' || G[j][k] == 'o') {
                poss = false;
                break;
            }
        }
        if(poss) {
            add(2*N + i, sink, 1);
            add(sink, 2*N + i, 0);
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            add(i - j + N, 2*N + i + j, 1);
            add(2*N + i + j, i - j + N, 0);
        }
    }

    tot += dinic();

    for(int i = -(N - 1); i <= (N - 1); i++) {
        for(int j = last_edge[i + N]; j != -1; j = nxt_edge[j]) {
            int k = oppo[j];
            if(k == source) continue;
            k -= 2*N;
            if(!capa[j]) {
                if(G[ (k + i) / 2 ][ (k - i) / 2 ] == '.' && A[ (k + i) / 2 ][ (k - i) / 2 ] == '.') A[ (k + i) / 2 ][ (k - i) / 2 ] = '+';
                else A[ (k + i) / 2 ][ (k - i) / 2 ] = 'o';
            }
        }
    }

    int cnt = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(A[i][j] != '.') cnt++;
        }
    }

    printf("Case #%d: %d %d\n", tc, tot, cnt);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(A[i][j] != '.') {
                printf("%c %d %d\n", A[i][j], i + 1, j + 1);
            }
        }
    }
}

int TC;
int main() {
    freopen("inputD.txt", "r", stdin);
    freopen("outputD.txt", "w", stdout);
    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
