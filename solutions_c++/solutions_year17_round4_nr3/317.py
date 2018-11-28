#include <bits/stdc++.h>
using namespace std;

#define TRACE(x)
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(a, b) TRACE(for (auto it=a; it!=b;) cout << *(it++) << " "; cout << endl)
#define WATCHC(V) TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})

#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<char> vc;
typedef vector<vc> vvc;

struct two_sat {
    int N;
    vector<vector<int>> impl;
 
    two_sat(int _N) {
        N = _N;
        impl.resize(2 * N);
    }
 
    void add_impl(int var1, bool neg1, int var2, bool neg2) {
        impl[2 * var1 + neg1].push_back(2 * var2 + neg2);
        impl[2 * var2 + !neg2].push_back(2 * var1 + !neg1);
    }
 
    void add_clause(int var1, bool neg1, int var2, bool neg2) {
        add_impl(var1, !neg1, var2, neg2);
    }
 
    void add_clause(int var1, bool neg1) {
        add_clause(var1, neg1, var1, neg1);
    }
 
    int V, L, C;
    stack<int> view;
 
    int dfs(int loc) {
        visit[loc] = V;
        label[loc] = L++;
 
        int low = label[loc];
        view.push(loc);
        in_view[loc] = true;
 
        for (int nbr : impl[loc]) {
            if(!visit[nbr]) low = min(low, dfs(nbr));
            else if(in_view[nbr]) low = min(low, label[nbr]);
        }
 
        if(low == label[loc]) {
            while (true) {
                int mem = view.top();
                comp[mem] = C;
                in_view[mem] = false;
                view.pop();
                if(mem == loc) break;
            }
            C++;
        }
 
        return low;
    }
 
    vector<int> visit, label, comp, in_view;
 
    void reset(vector<int> &v) {
        v.resize(2 * N);
        fill(v.begin(), v.end(), 0);
    }
 
    bool consistent() {
        V = 0, L = 0, C = 0;
        reset(visit), reset(label), reset(comp), reset(in_view);
 
        for (int i = 0; i < 2 * N; i++) {
            if(!visit[i]) {
                V++;
                dfs(i);
            }
        }
 
        for (int i = 0; i < N; i++)
            if(comp[2 * i] == comp[2 * i + 1]) {
                return false;
            }
 
        return true;
    }
};

const array<int, 3> INIT = { -1, -1, -1 };
bool laser(char c) { return (c == '-') || (c == '|'); }

/* 
 * Figure out where we end up if we enter pos (r, c) from direction dir.
 * Directions are
 *   0
 * 1   2
 *   3
 */
array<int, 3> trace(vvc &grid, vector<array<int, 3>> &memo, 
                    const int R, const int C, int r, int c, int dir) {
    TRACE(cout << "Following laser entering " << r << " " << c << " from " << dir << endl;)

    array<int, 3> &res = memo[(r * C + c) * 4 + dir];
    if (res != INIT) {
        TRACE(cout << "Found precomputed result: " << res[0] << " " << res[1] << " " << res[2] << endl;)
        return res;
    }

    if (laser(grid[r][c]) || grid[r][c] == '#') {
        // we hit a laser or a wall
        res = { r, c, dir };
        TRACE(cout << "Hit a laser or wall: " << res[0] << " " << res[1] << " " << res[2] << endl;)
        return res;
    }

    int nr, nc, ndir;

    if (grid[r][c] == '\\') {
        if (dir == 0) { nr = r; nc = c + 1; ndir = 1; }
        if (dir == 1) { nr = r + 1; nc = c; ndir = 0; }
        if (dir == 2) { nr = r - 1; nc = c; ndir = 3; }
        if (dir == 3) { nr = r; nc = c - 1; ndir = 2; }
    } else if (grid[r][c] == '/') {
        if (dir == 0) { nr = r; nc = c - 1; ndir = 2; }
        if (dir == 1) { nr = r - 1; nc = c; ndir = 3; }
        if (dir == 2) { nr = r + 1; nc = c; ndir = 0; }
        if (dir == 3) { nr = r; nc = c + 1; ndir = 1; }
    } else {
        if (dir == 0) { nr = r + 1; nc = c; }
        if (dir == 1) { nr = r; nc = c + 1; }
        if (dir == 2) { nr = r; nc = c - 1; }
        if (dir == 3) { nr = r - 1; nc = c; }
        ndir = dir;
    }

    return res = trace(grid, memo, R, C, nr, nc, ndir);
}

void solve() {
    int R, C;
    cin >> R >> C;
    R += 2, C += 2;

    vvc grid(R, vc(C));

    int L = 0;
    vvi nums(R, vi(C, -1)); // Number the lasers for convenience

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            // Pad the outside with walls for convenience
            if (r == 0 || c == 0 || r == R - 1 || c == C - 1) {
                grid[r][c] = '#';
            }
            else {
                cin >> grid[r][c];
            }

            if (laser(grid[r][c]))
                nums[r][c] = L++;
        }
    }

    TRACE(cout << "Took in input" << endl; )
    for (vc & v : grid) {
        WATCHC(v);
    }

    // memoize the traces, everything goes to a valid coordinate since we padded with walls
    vector<array<int, 3>> memo(R * C * 4, INIT);

    // ok let's do this
    two_sat sys(L);

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (grid[r][c] == '#') continue;

            array<int, 3> up = trace(grid, memo, R, C, r - 1, c, 3);
            array<int, 3> down = trace(grid, memo, R, C, r + 1, c, 0);

            int up_laser = nums[up[0]][up[1]];
            int down_laser = nums[down[0]][down[1]];

            array<int, 3> right = trace(grid, memo, R, C, r, c + 1, 1);
            array<int, 3> left = trace(grid, memo, R, C, r, c - 1, 2);

            int right_laser = nums[right[0]][right[1]];
            int left_laser = nums[left[0]][left[1]];

            // disallow orientations that kill lasers
            if (grid[r][c] == '|' || grid[r][c] == '-') {
                if (up_laser != -1 || down_laser != -1)
                    sys.add_clause(nums[r][c], true);
                if (right_laser != -1 || left_laser != -1)
                    sys.add_clause(nums[r][c], false);
            }

            // add a clause for each empty spot
            if (grid[r][c] == '.') {
                int opt1 = -1; bool orient1;
                if (left_laser == -1 && right_laser != -1) {
                    opt1 = right_laser;
                    orient1 = (right[2] == 1) || (right[2] == 2);
                }
                if (left_laser != -1 && right_laser == -1) {
                    opt1 = left_laser;
                    orient1 = (left[2] == 1) || (left[2] == 2);
                }

                int opt2 = -1; bool orient2;
                if (up_laser == -1 && down_laser != -1) {
                    opt2 = down_laser;
                    orient2 = (down[2] == 1) || (down[2] == 2);
                }
                if (up_laser != -1 && down_laser == -1) {
                    opt2 = up_laser;
                    orient2 = (up[2] == 1) || (up[2] == 2);

                }

                TRACE(
                        cout << "Options for empty spot " << r << " " << c << ": ("
                             << opt1 << ", " << orient1 << ") and (" << opt2 << ", " << orient2 << ")" << endl;
                     )

                if (opt1 == -1 && opt2 == -1) {
                    TRACE(cout << "No options for this spot." << endl;)
                    cout << "IMPOSSIBLE" << endl;
                    return;
                } 

                if (opt2 == -1) { opt2 = opt1; orient2 = orient1; }
                if (opt1 == -1) { opt1 = opt2; orient1 = orient2; }
                TRACE(cout << "Adding clause " << opt1 << " " << orient1 << " " << opt2 << " " << orient2 << endl;)
                sys.add_clause(opt1, orient1, opt2, orient2);
            }
        }
    }

    if (!sys.consistent()) {
        TRACE(cout << "Could not find a solution to the 2-sat system" << endl;)
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    cout << "POSSIBLE" << endl;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (r == 0 || c == 0 || r == R - 1 || c == C - 1) continue;

            if (grid[r][c] == '-' || grid[r][c] == '|') {
                int inx = nums[r][c];
                if (sys.comp[2 * inx] < sys.comp[2 * inx + 1])
                    cout << '|';
                else cout << '-';
            } else {
                cout << grid[r][c];
            }
        }
        if (r != 0 && r != R-1) cout << endl;
    }

    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cout << fixed << setprecision(15);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}

