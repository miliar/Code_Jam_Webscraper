#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR2(i, s, n) for (int i = (s); i <= (n); ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

typedef long long ll;
typedef vector<int> vi;

struct City
{
    int E, S;
};

struct Node
{
    double d;
    int n;
    Node() {}
    Node(double _d, int _n) : d(_d), n(_n) {}

    bool operator < (const Node &o) const {
        return d > o.d;
    }
};

int N, Q;
City cities[110];
int dist[110][110];
double dist2[110][110];
double go1(int from, int to)
{
    double dy[110];
    dy[0] = 0;
    FOR(i, 1, N) {
        dy[i] = -1;
        double sum_dist = 0;
        for(int j = i-1; j >= 0; --j) {
            sum_dist += dist[j][j+1];
            if (sum_dist > cities[j].E) continue;
            double test = dy[j] + sum_dist / (double)cities[j].S;
            if (dy[i] < 0 || dy[i] > test) dy[i] = test;
        }
    }
    return dy[to];
}

void run_from(int s)
{
    double visited[110] = {0, };
    REP(i, N) visited[i] = -1;

    priority_queue<Node> pq;
    pq.push(Node(0, s));

    while(!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (visited[node.n] >= 0) continue;
        visited[node.n] = node.d;
        REP(j, N) {
            if (dist[node.n][j] > 0) {
                double hour = double(dist[node.n][j]) + node.d;
                if (hour > cities[s].E) continue;
                pq.push(Node(hour, j));
            }
        }
    }

    REP(i, N) {
        dist2[s][i] = (visited[i] > 0) ? visited[i] / cities[s].S : -1;
    }
    dist2[s][s] = -1;
}

double go2(int from, int to)
{
    double visited[110] = {0, };
    REP(i, N) visited[i] = -1;

    priority_queue<Node> pq;
    pq.push(Node(0, from));

    while(!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (visited[node.n] >= 0) continue;
        visited[node.n] = node.d;
        if (node.n == to) {
            return node.d;
        }
        REP(j, N) {
            if (dist2[node.n][j] > 0) {
                double hour = double(dist2[node.n][j]) + node.d;
                pq.push(Node(hour, j));
            }
        }
    }
    return -1;
}

void solve()
{
    cin >> N >> Q;

    REP(i, N) {
        cin >> cities[i].E >> cities[i].S;
    }
    REP(i, N) {
        REP(j, N) {
            cin >> dist[i][j];
        }
    }

    REP(i, N)
        run_from(i);

    REP(i, Q) {
        int q0, q1;
        cin >> q0 >> q1;
        cout << setprecision(8) << go2(q0-1, q1-1) << " ";
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}