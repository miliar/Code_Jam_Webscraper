#include <bits/stdc++.h>

using namespace std;


const int kInf = 1e9;

template<typename T>
struct MaxFlowMinCost {
    vector<vector<int>> G;
    int src, dest;

    vector<int> Parent, InQ;
    vector<T> Dist;
    vector<vector<T>> F, C, K;



    void initMat(vector<vector<T>> &M, int n) {
        M.clear();
        M.resize(n, vector<T>(n, 0));
    }
    MaxFlowMinCost& Initialize(int n, int m = 0) {
        G.clear();
        G.resize(n);
        Parent.resize(n);
        Dist.resize(n);
        InQ.resize(n);

        initMat(F, n);
        initMat(C, n);
        initMat(K, n);

        return *this;
    }

    void _addEdge(int from, int to, T cap, T cost) {
        C[from][to] = cap;
        K[from][to] = cost;
        G[from].push_back(to);
    }
    MaxFlowMinCost& AddEdge(int from, int to, T cap, T cost) {
        _addEdge(from, to, cap, cost);
        _addEdge(to, from, 0, -cost);
        return *this;
    }

    MaxFlowMinCost& SetSourceSink(int src, int dest) {
        this->src = src; this->dest = dest;
        return *this;
    }

    bool Bellman() {
        static queue<int> Q;

        fill(Dist.begin(), Dist.end(), numeric_limits<T>::max());
        fill(Parent.begin(), Parent.end(), -1);
        fill(InQ.begin(), InQ.end(), 0);

        Dist[src] = 0;
        Q.push(src);

        while(!Q.empty()) {
            int node = Q.front();
            Q.pop();
            InQ[node] = 0;

            if(Parent[node] != -1 && InQ[Parent[node]])
                continue;

            for(auto vec : G[node]) {
                if(F[node][vec] < C[node][vec] && Dist[vec] > Dist[node] + K[node][vec]) {
                    Dist[vec] = Dist[node] + K[node][vec];
                    Parent[vec] = node;
                    if(!InQ[vec]) {
                        Q.push(vec);
                        InQ[vec] = 1;
                    }
                }
            }
        }

        return Parent[dest] != -1;
    }
    pair<T, T> Compute() {
        T flow = 0, cost = 0;

        while(Bellman()) {
            T m = numeric_limits<T>::max();
            for(int node = dest; node != src; node = Parent[node]) {
                m = min(m, C[Parent[node]][node] - F[Parent[node]][node]);
            }
            for(int node = dest; node != src; node = Parent[node]) {
                F[Parent[node]][node] += m;
                F[node][Parent[node]] -= m;
                cost += K[Parent[node]][node] * m;
            }
            flow += m;
        }

        return {flow, cost};
    }
};


MaxFlowMinCost<int> mfmc;

void Solve() {
    int n, c, m; cin >> n >> c >> m;

    vector<vector<int>> Tickets(c, vector<int>(n, 0));
    for (int i = 0; i < m; ++i) {
        int pos, cust; cin >> pos >> cust;
        Tickets[cust - 1][pos - 1]++;
    }

    if (c != 2) {
        cerr << "Skipped case\n";
        return;
    }

    int src = 2 * n;
    int dest = 2 * n + 1;
    // Build flow network

    cerr << "Building...\n";
    mfmc.Initialize(3 * n, 10000000);
    mfmc.SetSourceSink(src, dest);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) {
                if (i == 0) continue;
                mfmc.AddEdge(i, n + j, kInf, 1);
            } else {
                mfmc.AddEdge(i, n + j, kInf, 0);
            }
        }
    }

    for (int p = 0; p < n; ++p) {
        mfmc.AddEdge(src, p, Tickets[0][p], 0);
        mfmc.AddEdge(p + n, dest, Tickets[1][p], 0);
    }

    auto p = mfmc.Compute();
    cout << m - p.first << " " << p.second << endl;
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        Solve();
        cerr << "Done case #" << tt << endl;
    }
    return 0;
}