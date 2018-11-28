#include <iostream>
#include <vector>
#include <queue>
#include <cstdio>

using namespace std;

typedef long long LL;

struct Horse {
    LL e;
    LL s;
};

vector<double> solve() {
    int N, Q;
    cin >> N >> Q;

    vector<Horse> horses(N);
    for (int i = 0; i < N; ++i) {
        cin >> horses[i].e >> horses[i].s;
    }
    vector<vector<LL>> dist(N, vector<LL>(N));
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            cin >> dist[i][j];
        }
    }

    for(int k = 0; k < N; ++k) {
        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                if (dist[i][k] == -1 || dist[k][j] == -1) continue;
                const LL d = dist[i][k] + dist[k][j];
                if (dist[i][j] == -1 || dist[i][j] > d) dist[i][j] = d;
            }
        }
    }
    /*
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            cout << dist[i][j] << ' ';
        }
        cout << endl;
    }
    */

    vector<double> ans;
    for(int qq = 0; qq < Q; ++qq) {
        int U, V;
        cin >> U >> V;
        --U; --V;

        vector<double> memo(N, 1.0 / 0.0);
        priority_queue<pair<double, int>> q;
        q.push(make_pair(0, U));
        while(!q.empty()) {
            const double t = -q.top().first;
            const int pos = q.top().second;
            q.pop();
            if (t > memo[pos]) continue;
            if (pos == V) {
                ans.push_back(t);
                break;
            }
            for (int i = 0; i < N; ++i) {
                if (dist[pos][i] == -1) continue;
                if (dist[pos][i] > horses[pos].e) continue;
                const double nt = t + (double) dist[pos][i] / horses[pos].s;
                if (memo[i] <= nt) continue;
                memo[i] = nt;
                q.push(make_pair(-nt, i));
            }
        }
    }
    return ans;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        const vector<double> ans = solve();
        printf("Case #%d:", i);
        for (const double d : ans) {
            printf(" %.10f", d);
        }
        puts("");
    }
}
