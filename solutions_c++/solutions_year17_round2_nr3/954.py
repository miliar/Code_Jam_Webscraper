#include <bits/stdc++.h>
using namespace std;

#define lli double
#define MAX 101
#define INF 1e12

vector<int> path[MAX];
double E[MAX], S[MAX];
double dp[MAX];
double pref_dist[MAX];
double dist[MAX][MAX];
double timp[MAX][MAX];

int a[MAX], b[MAX];
int N;

void floyd_warshall() {
    for(int k = 0; k < N; k++)
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
}

    struct Node {
        int n;
        int parent;
        lli dist;
        Node(int n, int p, lli dist) : n(n), dist(dist), parent(p) {}
        bool operator < (Node const& other) const {
            return dist > other.dist;
        }
    };

    double dijkstra(int s, int t) {
        bool met[MAX];
        for (int i = 0; i < MAX; i++) met[i] = false;

        priority_queue<Node> q;
        q.push(Node(s, s, 0));

        while (q.size()) {
            Node p = q.top();
            q.pop();

            if (!met[p.n]) {
                met[p.n] = true;

                // cout << p.dist << "\n";

                if (p.n == t)
                    return p.dist;

                for (int i = 0; i < path[p.n].size(); i++) {
                    int cur = path[p.n][i];
                    // cout << p.n << " " << cur << "\n";
                    q.push(Node(cur, p.n, p.dist + timp[p.n][cur]));
                }
            }
        }

        return INF;
    }

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++){

        for (int i = 0; i < MAX; i++) {
            path[i].clear();
            for (int k = 0; k < MAX; k++)
                if (i != k)
                    dist[i][k] = INF;
        }

        cin >> N;
        int Q; cin >> Q;
        for (int i = 0; i < N; i++) {
            cin >> E[i] >> S[i];
        }
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < N; k++) {
                cin >> dist[i][k];
                if (dist[i][k] == -1)
                    dist[i][k] = INF;
            }
        }

        floyd_warshall();

        for (int i = 0; i < N; i++) {
            // see to which cities he can go.
            for (int k = 0; k < N; k++) {
                // cout << dist[i][k] << " ";
                if (dist[i][k] <= E[i]) {
                    // cout << i << " " << k << "\n";
                    timp[i][k] = dist[i][k] / S[i];
                    path[i].push_back(k);
                }
            }
        }

        cout << "Case #" << t << ": ";
        for (int i = 0; i < Q; i++) {
            cin >> a[i] >> b[i];
            cout << fixed << setprecision(9) << dijkstra(a[i] - 1, b[i] - 1) << " ";
        }
        cout << "\n";
    }

    return 0;
}