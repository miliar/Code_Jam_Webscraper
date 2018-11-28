#include <cmath>
#include <dirent.h>
#include <cstdio>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <iomanip>

using namespace std;

typedef vector<vector<int> > Matrix;
int const Inf = numeric_limits<int>::max();

vector<int> S;
vector<int> D;
Matrix P;
int K = 0;

int getMin(vector<int> const& vert, vector<int> const& path) {
    int u = 0;
    int minp = Inf;
    
    for (int i = 1; i < vert.size(); ++i) {
        if (vert[i] == 0 && path[i] < minp) {
            minp = path[i];
            u = i;
        }
    }
    
    return u;
}

void Dijkstra(vector<vector<int> > const & g, Matrix const & w, int s, vector<int>& vert, vector<int>& path) {
    path[s] = 0;
    
    int vsize = vert.size() - 1;
    while (vsize) {
        int u = getMin(vert, path);
        vert[u] = 1;
        --vsize;
        
        for (int v : g[u]) {
            path[v] = min(path[v], path[u] + w[u][v]); // relax
        }
    }
}

int recSol(int si, int di, int load, int cur, vector<vector<vector<vector<int> > > > & table) {
    if (di == K) {
        assert(load == 0);
        assert(si == K);
        return 0;
    }
    
    if (si == K) {
        assert(load != 0);
        if (load == 1)
            return P[cur][D[di]];
        else
            return recSol(si, di+1, load-1, D[di], table) + P[cur][D[di]];
    }
    
    if (table[si][di][cur][load] > 0) {
        return table[si][di][cur][load];
    }
    
    int res = 0;
    if (load == 0) {
        res = recSol(si+1, di, load+1, S[si], table) + P[cur][S[si]];
    } else if (load == 1) {
        int res1 = recSol(si, di+1, load-1, D[di], table) + P[cur][D[di]];
        int res2 = recSol(si+1, di, load+1, S[si], table) + P[cur][S[si]];
        
        res = min(res1, res2);
    } else {
        res = recSol(si, di+1, load-1, D[di], table) + P[cur][D[di]];
    }
    
    return table[si][di][cur][load] = res;
}

int main() {
    freopen("manic_input.txt", "r", stdin);
    freopen("manic_output.txt", "w", stdout);
    
    int T; cin >> T;
    
    for (int t = 1; t <= T; ++t) {
        int N; cin >> N;
        int M; cin >> M;
        cin >> K;
        
        vector<int> vert(N+1);
        vector<vector<int> > G(N+1);
        Matrix W(N+1, vector<int>(N+1));
        for (int i = 0; i < M; ++i) {
            int u; cin >> u;
            int v; cin >> v;
            int g; cin >> g;
            
            if (W[u][v] != 0) {
                W[u][v] = min(W[u][v], g);
                W[v][u] = min(W[v][u], g);
            } else {
                G[u].push_back(v);
                G[v].push_back(u);
                
                W[u][v] = g;
                W[v][u] = g;
            }
        }
        
        P.resize(N+1);
        for (auto & p : P) {
            p.resize(N+1);
            for (int& x : p) {
                x = Inf;
            }
        }
        
        for (int node = 1; node <= N; ++node) {
            for (int& v : vert) {
                v = 0;
            }
            
            Dijkstra(G, W, node, vert, P[node]);
        }
        
        S.resize(K);
        D.resize(K);
        for (int i = 0; i < K; ++i) {
            cin >> S[i];
            cin >> D[i];
        }
        
        int res = 0;
        for (int i = 0; i < K; ++i) {
            if (P[1][S[i]] == Inf) {
                res = -1;
                break;
            }
            if (P[1][D[i]] == Inf) {
                res = -1;
                break;
            }
        }
        
        if (res == -1) {
            cout << "Case #" << t << ": " << res << endl;
            continue;
        }
        
        vector< vector < vector < vector<int> > > > table(K, vector<vector<vector<int>>>(K, vector<vector<int>>(N+1, vector<int>(2,-1))));
        
        res = recSol(0, 0, 0, 1, table);
        
        cout << "Case #" << t << ": " << res << endl;
    }
    
    return 0;
}
