#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

struct Solver {
    vector<int> requirements;
    vector<vector<int>> packages;
    vector<vector<pair<int, int>>> ranges;
    int N;

    Solver() {
        int P;
        cin >> N >> P;
        requirements.resize(N, 0);
        packages.resize(N);
        ranges.resize(N);
        for (int i = 0; i < N; ++i) cin >> requirements[i];
        for (int i = 0; i < N; ++i) {
            int r = requirements[i];
            packages[i].resize(P);
            for (int j = 0; j < P; ++j) {
                int p;
                cin >> p;
                packages[i][j] = p;
                // p = 900, r = 500 => two packages (90%)
                // p = 10, r = 2 => 5 packages only
                // p = 10, r = 1 => 10 packages only
                // p = 100, r = 1 => 91 packages to 111 packages.
                // [ceil(p / 1.1r), floor(p / 0.9r)]
                // ceil(p / 1.1r) = ceil(10p / 11r)
                // floor(p / 0.9r) = floor(10p / 9r)
                int low = max(1, (10 * p + 11 * r - 1) / (11 * r)),
                    high = (10 * p) / (9 * r);
                if (low <= high) ranges[i].emplace_back(low, high);
            }
            sort(ranges[i].begin(), ranges[i].end());
        }
    }

    vector<vector<int>> capacity;
    vector<int> layer_offsets;
    vector<set<int>> adjacency;
    vector<int> visited;

    inline static bool overlap(const pair<int, int>& a, const pair<int, int>& b) {
        return max(a.first, b.first) <= min(a.second, b.second);
    }

    void add_edge(int from, int to) {
        adjacency[from].insert(to);
        adjacency[to].insert(from);
        capacity[from][to] = 1;
    }

    bool dfs(int phase, int v, int t) {
        if (v == t) return true;
        if (visited[v] == phase) return false;
        visited[v] = phase;
        for (int vv : adjacency[v]) {
            if (capacity[v][vv] > 0 && dfs(phase, vv, t)) {
                --capacity[v][vv];
                ++capacity[vv][v];
                return true;
            }
        }
        return false;
    }

    inline int match(int s, int t) {
        visited.resize(adjacency.size(), -1);
        int ans = 0;
        while (dfs(ans, s, t)) {
            ++ans;
        }
        return ans;
    }

    int solve() {
        // We are going to construct a huge graph now.
        // We have the source at 0, sink at 1.
        // Each ingredient is a layer. Each package is a one edge.
        layer_offsets.push_back(1);
        for (int i = 0; i < N; ++i) {
            if (ranges[i].empty()) return 0;
            layer_offsets.push_back(layer_offsets.back() + ranges[i].size() * 2);
        }
        layer_offsets.push_back(layer_offsets.back() + 1);
        int num_vertices = layer_offsets.back();
        capacity.resize(num_vertices, vector<int>(num_vertices, 0));
        adjacency.resize(num_vertices);
        // Let's connect the layers.
        // The source is connected to all first layer.
        for (int v = 0; v < ranges[0].size(); ++v) {
            int v_name = layer_offsets[0] + v * 2;
            add_edge(0, v_name);
        }
        // Add a fake sink.
        ranges.push_back(vector<pair<int, int>>(1, make_pair(1, 10000000)));
        for (int l = 0; l < N; ++l) {
            // Within that layer!
            int offset = layer_offsets[l];
            for (int v = 0; v < ranges[l].size(); ++v) {
                add_edge(offset + v * 2, offset + v * 2 + 1);
                // Find out the next layer.
                int next_offset = layer_offsets[l + 1];
                for (int vv = 0; vv < ranges[l + 1].size(); ++vv) {
                    if (overlap(ranges[l][v], ranges[l + 1][vv])) {
                        add_edge(offset + v * 2 + 1, next_offset + vv * 2);
                    }
                }
            }
        }

        return match(0, num_vertices - 1);
    }
};

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        Solver solver;
        cout << "Case #" << case_index << ": " << solver.solve() << endl;
    }
    return 0;
}
