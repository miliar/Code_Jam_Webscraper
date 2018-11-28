#include <bits/stdc++.h>

using namespace std;

struct Horse {
    int e, s;
    bool operator<(const Horse& other) const {
        return e < other.e || (e == other.e && s < other.s);
    }
};

struct State {
    int v;
    double t;
    Horse h;
    bool operator<(const State& other) const {
        return t > other.t || (t == other.t && h.s < other.h.s);
    }
};

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    cout << fixed << setprecision(8);
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        int n, q;
        cin >> n >> q;
        vector<int> e(n), s(n);
        for (int i = 0; i < n; ++i) {
            cin >> e[i] >> s[i];
        }
        vector<vector<int>> d(n, vector<int>(n));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                cin >> d[i][j];
        vector<vector<double>> time(n, vector<double>(n, -1));
        for (int i = 0; i < q; ++i) {
            int u, v;
            cin >> u >> v;
            --u; --v;
            priority_queue<State> bfs;
            bfs.push({ u, 0, {e[u], s[u]} });
            vector<set<Horse>> visit(n);
            while (!bfs.empty()) {
                State st = bfs.top();
                bfs.pop();
                if (time[u][st.v] == -1)
                    time[u][st.v] = st.t;
                if (st.v == v) break;
                auto it = visit[st.v].find(st.h);
                if (it != visit[st.v].end() && it->s >= st.h.s) continue;
                if (st.v != v && visit[st.v].empty())
                    bfs.push({ st.v, st.t, {e[st.v], s[st.v]} });
                visit[st.v].insert(st.h);
                for (int i = 0; i < n; ++i) {
                    if (d[st.v][i] > 0 && d[st.v][i] <= st.h.e)
                        bfs.push({ i, st.t + (double)d[st.v][i] / st.h.s, { st.h.e - d[st.v][i], st.h.s } });
                }
            }
            cout << time[u][v] << " ";
        }
        cout << endl;
    }
}