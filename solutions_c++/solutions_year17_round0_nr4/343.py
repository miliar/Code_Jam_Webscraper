#include <tuple>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <unordered_map>
using namespace std;

ifstream                        f("in.txt");
ofstream                        g("out.txt");
vector<unordered_map<int, int>> F, C;
vector<vector<int>>             G;
vector<string>                  S;
int                             N;

void add_edge(int u, int v, int capacity) {
    G[u].push_back(v); C[u][v] = capacity; F[u][v] = 0;
    G[v].push_back(u); C[v][u] = capacity; F[v][u] = capacity;
}

void create_network() {
    int K = 1 + N + (2*N - 1) + N + (2*N - 1) + 1;
    F.clear(); C.clear(); G.clear(); F.resize(K); C.resize(K); G.resize(K);

    for (int r = 0; r < N; r++)         add_edge(0, 1 + r,     1);
    for (int d = 0; d < 2*N - 1; d++)   add_edge(0, 1 + N + d, 1);
    
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            add_edge(1 + r, 3*N + c, 1);

    vector<vector<bool>> intersect(2*N - 1, vector<bool>(2*N - 1));
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            intersect[r + c][r - c + N - 1] = true;
    
    for (int d1 = 0; d1 < 2*N - 1; d1++)
        for (int d2 = 0; d2 < 2*N - 1; d2++)
            if (intersect[d1][d2]) add_edge(1 + N + d1, 4*N + d2, 1);
    
    for (int c = 0; c < N; c++)         add_edge(3*N + c, K - 1, 1);
    for (int d = 0; d < 2*N - 1; d++)   add_edge(4*N + d, K - 1, 1);
}

void push_flow_no_return(int a, int b, int c, int d, int flow) {
    F[a][b] += flow; F[b][a] += flow;
    F[b][c] += flow; F[c][b] += flow;
    F[c][d] += flow; F[d][c] += flow;
}

void add_model(char m, int r, int c, int &flow) {
    int K = 1 + N + (2*N - 1) + N + (2*N - 1) + 1;
    
    switch (m) {
        case '+':
            push_flow_no_return(0, 1 + N + r + c, 4*N + r - c + N - 1, K - 1, 1);
            flow++;
            break;
            
        case 'x':
            push_flow_no_return(0, 1 + r, 3*N + c, K - 1, 1);
            flow++;
            break;
            
        case 'o':
            push_flow_no_return(0, 1 + N + r + c, 4*N + r - c + N - 1, K - 1, 1);
            push_flow_no_return(0, 1 + r, 3*N + c, K - 1, 1);
            flow += 2;
            break;
    }
}

int max_flow(int startFlow) {
    int src = 0, dst = (int)G.size() - 1, flow = startFlow;

    for (;;) {
        vector<bool>            visited(G.size());
        vector<int>             parent(G.size(), -1);
        queue<pair<int, int>>   Q;
        int                     delta = 0;
        
        Q.push({src, 1}); visited[src] = true;
        while (!Q.empty()) {
            int u = Q.front().first, d = Q.front().second; Q.pop();
            if (u == dst) { delta = d; break; }
            for (auto v : G[u]) if (!visited[v] && C[u][v] > F[u][v]) {
                parent[v] = u; visited[v] = true;
                Q.push({v, min(d, C[u][v] - F[u][v])});
            }
        }
        if (!delta) break;
        
        flow += delta;
        for (int v = dst; parent[v] != -1; v = parent[v]) {
            int u = parent[v]; F[u][v] += delta; F[v][u] -= delta;
        }
    }
    
    return flow;
}

bool is_path_saturated(int a, int b, int c, int d) {
    return F[a][b] == C[a][b] && F[b][c] == C[b][c] && F[c][d] == C[c][d];
}

void print_solution(int flow) {
    vector<tuple<char, int, int>>   ans;
    int                             K = (int)G.size();
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++) {
            bool isP = is_path_saturated(0, 1 + N + r + c, 4*N + r - c + N - 1, K - 1);
            bool isX = is_path_saturated(0, 1 + r,         3*N + c,             K - 1);
            
            if (isP && isX) {
                if (S[r][c] != 'o') ans.push_back(make_tuple('o', r + 1, c + 1));
            }
            else if (isP){
                if (S[r][c] != '+') ans.push_back(make_tuple('+', r + 1, c + 1));
            }
            else if (isX) {
                if (S[r][c] != 'x') ans.push_back(make_tuple('x', r + 1, c + 1));
            }
        }
    
    g << flow << " " << ans.size() << endl;
    for (auto t : ans) g << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
 /*
    for (int i = 0; i < G.size(); i++)
        for (auto j : G[i])
            g << i << "->" << j << " flow=" << F[i][j] << " capacity=" << C[i][j] << endl;
*/
}

int main() {
    int     T, M, r, c; f >> T;
    char    model;
    
    for (int test = 1; test <= T; test++) {
        f >> N >> M;
        create_network();
        
        int startFlow = 0;
        S = vector<string>(N, string(N, '.'));
        while (M--) {
            f >> model >> r >> c; r--; c--;
            S[r][c] = model;
            add_model(model, r, c, startFlow);
        }
        
        int flow = max_flow(startFlow);
        g << "Case #" << test << ": "; print_solution(flow);
    }

    return 0;
}
