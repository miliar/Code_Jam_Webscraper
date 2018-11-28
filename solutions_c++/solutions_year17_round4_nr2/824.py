#include <bits/stdc++.h>
using namespace std;

class PerfectMatchingMinCost {
private:
    typedef vector<int> VI;
    typedef vector<VI> VII;
    const int INF = 1e9;

    int N;
    VII cost, adj;
    VI d, fx, fy, mx, my, arg, trace;

    queue<int> q;

    int getCost(int x, int y) {
        return cost[x][y] - fx[x] - fy[y];
    }

    void initBFS(int start) {
        for (int i = 0; i < N; i++)
            trace[i] = -1;
        while (!q.empty()) q.pop();
        q.push(start);
        for (int i = 0; i < N; i++)
            d[i] = getCost(start, i), arg[i] = start;
    }

    int findPath() {
        while (!q.empty()) {
            int x = q.front(); q.pop();
            for (int i = 0; i < adj[x].size(); i++) {
                int y = adj[x][i];
                if (trace[y] == -1) {
                    int w = getCost(x, y);
                    if (w == 0) {
                        trace[y] = x;
                        if (my[y] == -1) 
                            return y;
                        q.push(my[y]);
                    }
                    if (d[y] > w) {
                        d[y] = w;
                        arg[y] = x;
                    }
                }
            }
        }
        return -1;
    }

    int update(int start) {
        int delta = INF;
        for (int y = 0; y < N; y++)
            if (trace[y] == -1)
                delta = min(delta, d[y]);   
        fx[start] += delta;
        for (int y = 0; y < N; y++)
            if (trace[y] != -1) {
                int x = my[y];
                fx[x] += delta;
                fy[y] -= delta;
            } 
            else d[y] -= delta;
        for (int y = 0; y < N; y++)
            if (trace[y] == -1 && d[y] == 0) {
                trace[y] = arg[y];
                if (my[y] == -1) 
                    return y;
                q.push(my[y]);
            }
        return -1;
    }

    void enlarge(int finish) {
        for (int y = finish; y != -1; ) {
            int x = trace[y];
            int yy = mx[x];
            mx[x] = y;
            my[y] = x;
            y = yy;
        }
    }

public:
    PerfectMatchingMinCost(int n = 0) {
        N = n;
        cost = VII(n, VI(n, INF));
        adj = VII(n);

        trace = VI(n);
        arg = VI(n);
        fx = VI(n);
        fy = VI(n);
        d = VI(n);
        mx = VI(n, -1);
        my = VI(n, -1);
    }

    void AddEdge(int x, int y, int c) {
        if (cost[x][y] == INF) adj[x].push_back(y);
        if (cost[x][y] > c) cost[x][y] = c;
    }

    int GetMinCost() {
        for (int x = 0; x < N; x++) {
            initBFS(x);
            int finish = -1;
            do {                
                finish = findPath();
                if (finish != -1) break;
                finish = update(x);
            } while (finish == -1);
            enlarge(finish);
        }
        int ret = 0;
        for (int x = 0; x < N; x++) 
            ret += cost[x][mx[x]];
        return ret;
    }
};


int T;
int N, M, C;
pair<int, int> tic[1010];

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        cin >> N >> C >> M;
        for (int i = 0; i < M; ++i) {
            cin >> tic[i].first >> tic[i].second;
        }
        
        if (C == 2) {
            vector<int> pos[2];
            for (int i = 0; i < M; ++i) {
                pos[tic[i].second - 1].push_back(tic[i].first);
            }
            while (pos[0].size() < 2 * M) {
                pos[0].push_back(0);
            }
            while (pos[1].size() < 2 * M) {
                pos[1].push_back(0);
            }

            PerfectMatchingMinCost match(2 * M);

            for (int i = 0; i < 2 * M; ++i) {
                for (int j = 0; j < 2 * M; ++j) {
                    if (pos[0][i] == 0 && pos[1][j] == 0) {
                        match.AddEdge(i, j, 0);
                    } else if (pos[0][i] != pos[1][j]) {
                        match.AddEdge(i, j, 10000);
                    } else if (pos[0][i] == pos[1][j] && max(pos[0][i], pos[1][j]) > 1) {
                        match.AddEdge(i, j, 10001);
                    }
                }
            }

            int cost = match.GetMinCost();
            int nride = cost / 10000;
            int promo = cost % 10000;

            cout << "Case #" << tid + 1 << ": " << nride << " " << promo << endl;

        } else {
            cout << "DM kho vl" << endl;
        }
    }

    return 0;
}