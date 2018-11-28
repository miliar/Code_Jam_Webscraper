#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;

char board[64][64];

const pair<int, int> kDirections[] = {
    { 1, 0 },
    { -1, 0 },
    { 0, 1 },
    { 0, -1 }
};

int numbering[64][64];

int memo[64][64][4];

int beam_assignment[64];

struct Solver {
    int R, C;
    int num_beams = 0;
    vector<set<int>> neighbors;
    vector<vector<int>> rev_neighbors;

    Solver() {
        cin >> R >> C;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                cin >> board[r][c];
            }
        }
        memset(numbering, 0xff, sizeof(numbering));
        num_beams = 0;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (board[r][c] == '|' || board[r][c] == '-') {
                    numbering[r][c] = num_beams++;
                }
            }
        }
        memset(memo, 0xff, sizeof(memo));
        neighbors.resize(num_beams * 2);
    }

    int find_beam(int r, int c, int dir) {
        if (memo[r][c][dir] == -1) {
            int nr = r + kDirections[dir].first;
            int nc = c + kDirections[dir].second;
            if (nr < 0 || nr >= R || nc < 0 || nc >= C ||
                board[nr][nc] == '#') {
                memo[r][c][dir] = -2;  // There is nothing.
            } else {
                // Figure out new direction.
                int ndir = dir;
                if (board[nr][nc] == '-' || board[nr][nc] == '|') {
                    // We have found our targets.
                    memo[r][c][dir] = 2 * numbering[nr][nc] + (dir < 2 ? 1 : 0);
                } else {
                    if (board[nr][nc] == '/') {
                        // 0 -> 3, 1 -> 2, 2 -> 1, 3 -> 0
                        ndir = 3 - dir;
                    } else if (board[nr][nc] == '\\') {
                        // 0 -> 2, 1 -> 3, 2 -> 0, 3 -> 1
                        ndir = 2 ^ dir;
                    }
                    memo[r][c][dir] = find_beam(nr, nc, dir);
                }
            }
        }
        return memo[r][c][dir];
    }

    void solve() {
        if (!solveImpl()) {
            cout << "IMPOSSIBLE" << endl;
        }
    }

    inline void add_edge(int from, int to) {
        // cerr << "Adding " << from << " -> " << to << endl;
        neighbors[from].insert(to);
    }

    bool solveImpl() {
        // For all beam and for all empty cells, construct statements.
        // We have num_beams variables.
        // Each is either horiz or vert.
        // We treat horizontal as false, vertical as true.

        // This basically means that we have a graph with 2 * num_beams vertices.
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (board[r][c] == '.') {
                    // Check if we can afford having horizontal beams.
                    int h1 = find_beam(r, c, 2);
                    int h2 = find_beam(r, c, 3);
                    int h_sum = -1;
                    if (h1 == -2 && h2 != -2) h_sum = h2;
                    else if (h1 != -2 && h2 == -2) h_sum = h1;

                    int v1 = find_beam(r, c, 0);
                    int v2 = find_beam(r, c, 1);
                    int v_sum = -1;
                    if (v1 == -2 && v2 != -2) v_sum = v2;
                    else if (v1 != -2 && v2 == -2) v_sum = v1;

                    // Add the clause (h_sum v v_sum)
                    if (h_sum == -1 && v_sum == -1) return false;
                    else if (h_sum == -1) {
                        // Add (v_sum v v_sum)
                        // cerr << "Case 1" << endl;
                        add_edge(v_sum ^ 1, v_sum);
                    } else if (v_sum == -1) {
                        // Add (h_sum v h_sum)
                        // cerr << "Case 2" << endl;
                        add_edge(h_sum ^ 1, h_sum);
                    } else {
                        // Add (h_sum v v_sum)
                        // cerr << "Case 3" << endl;
                        add_edge(h_sum ^ 1, v_sum);
                        // cerr << "Case 4" << endl;
                        add_edge(v_sum ^ 1, h_sum);
                    }
                } else if (board[r][c] == '-' || board[r][c] == '|') {
                    int my_horiz = numbering[r][c] * 2;
                    int h1 = find_beam(r, c, 2);
                    int h2 = find_beam(r, c, 3);
                    if (h1 != -2 || h2 != -2) {
                        // I cannot be horizontal.
                        // cerr << "Case 5" << endl;
                        add_edge(my_horiz, my_horiz ^ 1);
                    }
                    int my_vert = numbering[r][c] * 2 + 1;
                    int v1 = find_beam(r, c, 0);
                    int v2 = find_beam(r, c, 1);
                    if (v1 != -2 || v2 != -2) {
                        // I cannot be vertical.
                        // cerr << "Case 6" << endl;
                        add_edge(my_vert, my_vert ^ 1);
                    }
                }
            }
        }
        // Graph constructed. Now do SCC.
        auto scc = compute_scc();

        // Check if things are okay.
        for (const auto& component : scc) {
            /*
            cerr << "SCC:";
            for (int x : component) {
                cerr << ' ' << x;
            }
            cerr << endl;
            */
            for (int x : component) {
                if (component.find(x ^ 1) != component.end()) return false;
            }
        }

        memset(beam_assignment, 0xff, sizeof(beam_assignment));
        for (auto riter = scc.rbegin(); riter != scc.rend(); ++riter) {
            for (int x : *riter) {
                int beam = x >> 1;
                // Check if beam is already set.
                if (beam_assignment[beam] == -1) {
                    // cerr << "Setting " << beam << " to " << (x & 1) << endl;
                    beam_assignment[beam] = x & 1;
                }
            }
        }

        cout << "POSSIBLE" << endl;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (numbering[r][c] != -1) {
                    board[r][c] = beam_assignment[numbering[r][c]] == 1 ? '|' : '-';
                }
                cout << board[r][c];
            }
            cout << endl;
        }

        return true;
    }

    vector<bool> visited;

    vector<set<int>> compute_scc() {
        visited.assign(2 * num_beams, false);
        vector<int> ss;
        for (int i = 0; i < 2 * num_beams; ++i) {
            dfs1(i, ss);
        }
        // Reverse graph.
        rev_neighbors.resize(2 * num_beams);
        for (int i = 0; i < 2 * num_beams; ++i) {
            for (int j : neighbors[i]) {
                rev_neighbors[j].push_back(i);
                // cerr << "Reversing " << j << " -> " << i << endl;
            }
        }
        visited.assign(2 * num_beams, false);
        vector<set<int>> ret;
        while (!ss.empty()) {
            int v = ss.back();
            ss.pop_back();
            if (!visited[v]) {
                ret.emplace_back();
                visited[v] = true;
                dfs2(v, ret.back());
            }
        }
        return ret;
    }

    void dfs1(int v, vector<int>& ss) {
        if (visited[v]) return;
        visited[v] = true;
        for (int x : neighbors[v]) {
            dfs1(x, ss);
        }
        ss.push_back(v);
    }

    void dfs2(int v, set<int>& ss) {
        ss.insert(v);
        for (int x : rev_neighbors[v]) {
            if (!visited[x]) {
                visited[x] = true;
                dfs2(x, ss);
            }
        }
    }
};

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        Solver solver;
        cout << "Case #" << case_index << ": ";
        solver.solve();
    }
    return 0;
}
