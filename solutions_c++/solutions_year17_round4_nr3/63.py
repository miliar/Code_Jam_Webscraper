#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

static const int dx[4] = {-1, 0, 1, 0};
static const int dy[4] = {0, -1, 0, 1};
// UP, LEFT, DOWN, RIGHT

// hits /, so RIGHT, DOWN, LEFT, UP
static const int hit0[4] = {3, 2, 1, 0};

// hits \, so LEFT, UP, RIGHT, DOWN
static const int hit1[4] = {1, 0, 3, 2};

void dfs1(int node, const vector< vector<int> > &edges, vector<bool> &used, vector<int>& order) {
    if (used[node])
        return;
    used[node] = true;
    for (auto &x : edges[node])
        dfs1(x, edges, used, order);
    order.push_back(node);
}

vector<int> solve2SAT(vector< vector<int> > edges) {
    int N = edges.size() / 2;

    vector< vector<int> > reverse_edges(2 * N);
    for (int i = 0; i < 2 * N; ++i)
        for (auto &x : edges[i])
            reverse_edges[x].push_back(i);

    vector<bool> used(2 * N, false);
    vector<int> order;
    for (int i = 0; i < 2 * N; ++i)
        dfs1(i, edges, used, order);
    reverse(order.begin(), order.end());

    fill(used.begin(), used.end(), false);
    vector<int> value(N, 2);
    for (auto &x : order) {
        vector<int> component;
        dfs1(x, reverse_edges, used, component);
        int component_value = 2;
        for (auto &v : component)
            if (value[v / 2] != 2)
                component_value = (value[v / 2] ^ (v % 2));
        if (component_value == 2)
            component_value = 0;
        for (auto &v : component) {
            if (value[v / 2] != 2 && (value[v / 2] ^ (v % 2)) != component_value)
                return vector<int>();
            value[v / 2] = component_value ^ (v % 2);
        }
    }
    return value;
}

string test_case() {
    int R, C; cin >> R >> C;
    vector<string> map(R);
    for (int i = 0; i < R; ++i)
        cin >> map[i];

    vector< pair<int, int> > laser;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (map[i][j] == '-' || map[i][j] == '|')
                laser.emplace_back(i, j);

    int index = 0;
    vector< vector<int> > side[2];
    side[0] = side[1] = vector< vector<int> > (R, vector<int>(C, -1));
    vector< vector<int> > edges(laser.size() * 2);
    auto extend = [&](int x, int y, int dir, int node) {
        do {
            x += dx[dir];
            y += dy[dir];
            if (x < 0 || x >= R || y < 0 || y >= C)
                break;
            side[dir % 2][x][y] = node;
            if (map[x][y] == '/')
                dir = hit0[dir];
            else if (map[x][y] == '\\')
                dir = hit1[dir];
            else if (map[x][y] == '|' || map[x][y] == '-')
                edges[node].push_back(node ^ 1);
            else if (map[x][y] == '#')
                break;
        } while (true);
    };

    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (map[i][j] == '-' || map[i][j] == '|') { // laser, yey
                // first true, horizontal
                // Right
                extend(i, j, 3, index * 2);
                // Left
                extend(i, j, 1, index * 2);

                // vertical, false
                // UP
                extend(i, j, 0, index * 2 + 1);
                // down
                extend(i, j, 2, index * 2 + 1);
                ++index;
            }

    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) {
            if (map[i][j] != '.')
                continue;
            if (side[0][i][j] == -1 && side[1][i][j] == -1)
                return "IMPOSSIBLE\n";
            if (side[0][i][j] == -1) { // ain't hit up and down, pretty clear answer
                int node = side[1][i][j];
                edges[node ^ 1].push_back(node);
                continue;
            }
            if (side[1][i][j] == -1) {
                int node = side[0][i][j];
                edges[node ^ 1].push_back(node);
                continue;
            }
            int node1 = side[0][i][j];
            int node2 = side[1][i][j];
            edges[node1 ^ 1].push_back(node2);
            edges[node2 ^ 1].push_back(node1);
        }

    auto how = solve2SAT(edges);
    if (how.empty()) {
        return "IMPOSSIBLE\n";
    }
    string answer = "POSSIBLE\n";
    for (int i = 0; i < int(laser.size()); ++i)
        if (how[i])
            map[laser[i].first][laser[i].second] = '-';
        else
            map[laser[i].first][laser[i].second] = '|';
    for (auto &row : map) {
        answer += row;
        answer += "\n";
    }
    return answer;
}

int main() {
    int T; cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << test_case();
    }
}
