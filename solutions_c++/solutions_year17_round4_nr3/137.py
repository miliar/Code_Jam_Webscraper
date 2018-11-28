#include "bits/stdc++.h"
using namespace std;

const int N = 500;

// up, left, down, right
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

int n, m;
char a[N][N];

/*
    2-SAT Template
    Given an implication graph, this checks if a solution exists.

    addXor(), addAnd(), addOr() can be used to appropriately add clauses.
    forceTrue() forces some variable to be true.
    forceFalse() forces some variable to be false.

    You can also add additional implications yourself.
    init() initializes 2-SAT arrays.
    solve() checks if in the final implication graph, a valid solution exists.
    mark[u] stores the boolean value of the node (u). You can use mark[] to
    recover the final solution as well.

    Notes on Indexing Nodes :
    u = 2k, !u = 2k + 1
    Nodes are 0-indexed. [0, NUM_VERTICES)
*/

int NUM_VERTICES, id;
int arr[N * 2];
vector < int > adj[N * 2];
bool mark[N * 2];

inline bool dfs(int node) {
    if (mark[node ^ 1]) {
        return false;
    }
    if (mark[node]) {
        return true;
    }
    mark[node] = true;
    arr[id++] = node;
    for (int i = 0; i < (int) adj[node].size(); i++) {
        if (!dfs(adj[node][i])) {
            return false;
        }
    }
    return true;
}

inline void init() {
    for (int i = 0; i < NUM_VERTICES; i++) {
        adj[i].clear();
    }
    memset(mark, 0, sizeof(mark));
}

// Adds the clause (u or v) to the set of clauses
inline void addOr(int u, int v) {
    adj[u ^ 1].push_back(v);
    adj[v ^ 1].push_back(u);
}

// Adds the clause (u == v) to the set of clauses
inline void addEquivalent(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);
    adj[u ^ 1].push_back(v ^ 1);
    adj[v ^ 1].push_back(u ^ 1);
}

// Adds the clause (u xor v) to the set of clauses
inline void addXor(int u, int v) {
    addOr(u, v);
    addOr(u ^ 1, v ^ 1);
}

// Forces variable (u) to be true
inline void forceTrue(int u) {
    adj[u ^ 1].push_back(u);
}

// Forces variable (u) to be false
inline void forceFalse(int u) {
    adj[u].push_back(u ^ 1);
}

// Adds the clause (u and v) to the set of clauses
inline void addAnd(int u, int v) {
    forceTrue(u);
    forceTrue(v);
}

// Returns true if a solution exists.
inline bool solve() {
    for (int i = 0; i < NUM_VERTICES; i++) {
        sort(adj[i].begin(), adj[i].end());
        adj[i].resize(unique(adj[i].begin(), adj[i].end()) - adj[i].begin());
    }
    for (int i = 0; i < NUM_VERTICES; i += 2) {
        if ((!mark[i]) && (!mark[i + 1])) {
            id = 0;
            if(!dfs(i)) {
                while (id > 0) {
                    mark[arr[--id]] = false;
                }
                if(!dfs(i + 1)) {
                    return false;
                }
            }
        }
    }
    return true;
}

// End of 2-SAT Template.

int number[N][N];
bool made_false[N][N];

inline bool rekt(int x, int y) {
    return !(x >= 1 && x <= n && y >= 1 && y <= m);
}

int main() {
    freopen ("inp.in", "r", stdin);
    freopen ("C.out", "w", stdout);
    int tc; cin >> tc;
    for (int qq = 1; qq <= tc; qq++) {
        cout << "Case #" << qq << ": ";
        cin >> n >> m;
        int beams = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> a[i][j];
                beams += ((a[i][j] == '|') || (a[i][j] == '-'));
                if ((a[i][j] == '|') || (a[i][j] == '-')) {
                    number[i][j] = beams - 1;
                } else if (a[i][j] == '#') {
                    number[i][j] = -2;
                } else {
                    number[i][j] = -1;
                }
            }
        }
        NUM_VERTICES = 4 * beams;
        init();
        // 4x -> beam vertical
        // 4x + 1 -> ! beam vertical
        // 4x + 2 -> beam horizontal
        // 4x + 3 -> ! beam horizontal
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if ((a[i][j] == '|') || (a[i][j] == '-')) {
                    addXor(4 * number[i][j], 4 * number[i][j] + 2); // both cant be on at same time
                    int dir = 0;
                    int cx = i, cy = j;
                    // going up
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            forceFalse(4 * number[cx][cy]);
                            break;
                        }
                    }
                    dir = 2;
                    cx = i, cy = j;
                    // going down
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            forceFalse(4 * number[cx][cy]);
                            break;
                        }
                    }
                    // going left
                    dir = 1;
                    cx = i, cy = j;
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            forceFalse(4 * number[cx][cy] + 2);
                            break;
                        }
                    }
                    // going right
                    dir = 3;
                    cx = i, cy = j;
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            forceFalse(4 * number[cx][cy] + 2);
                            break;
                        }
                    }
                }
            }
        }
        bool rektttt = false;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (a[i][j] == '.') {
                    int dir = 0;
                    int cx = i, cy = j;
                    // going up
                    vector < int > vert_ids;
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            vert_ids.push_back(4 * number[cx][cy]);
                            break;
                        }
                    }
                    dir = 2;
                    cx = i, cy = j;
                    // going down
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            vert_ids.push_back(4 * number[cx][cy]);
                            break;
                        }
                    }
                    // going left
                    dir = 1;
                    cx = i, cy = j;
                    vector < int > hor_ids;
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            hor_ids.push_back(4 * number[cx][cy] + 2);
                            break;
                        }
                    }
                    // going right
                    dir = 3;
                    cx = i, cy = j;
                    while (cx >= 1 && cx <= n && cy >= 1 && cy <= m) {
                        cx += dx[dir];
                        cy += dy[dir];
                        if (rekt(cx, cy)) {
                            break;
                        }
                        if (a[cx][cy] == '.') {
                            continue;
                        }
                        if (a[cx][cy] == '#') {
                            break;
                        }
                        if (number[cx][cy] >= 0) {
                            hor_ids.push_back(4 * number[cx][cy] + 2);
                            break;
                        }
                    }
                    if (vert_ids.size() && hor_ids.size()) {
                        if (vert_ids.size() > 1 && hor_ids.size() > 1) {
                            rektttt = true;
                        }
                        addOr(vert_ids[0], hor_ids[0]);
                    } else if (!vert_ids.size() && !hor_ids.size()) {
                        rektttt = true;
                    } else if (vert_ids.size()) {
                        forceTrue(vert_ids[0]);
                    } else {
                        forceTrue(hor_ids[0]);
                    }
                }
            }
        }
        if (rektttt) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        bool ans = solve();
        if (ans) {
            cout << "POSSIBLE\n";
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    int x = number[i][j];
                    if (x < 0) {
                        cout << a[i][j];
                    } else {
                        if (mark[4 * x] == 1) {
                            cout << "|";
                        } else {
                            cout << "-";
                        }
                    }
                }
                cout << "\n";
            }
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
}