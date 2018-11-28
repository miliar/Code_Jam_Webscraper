#include <bits/stdc++.h>

using namespace std;

// RDLU
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int pair_slash[] = {3, 2, 1, 0};
int pair_rslash[] = {1, 0, 3, 2};

vector<int> DEFAULT(1, -1);

//
// 2SAT Solver
//
// Usage:
//
// Add edges with AddEdge(u, xu, v, xv)
// where xu == 1 if u and xu == 0 if not u.
// (edges are of type u -> v), and call Solve().
//
// The answer is in TwoSAT::Sol. If there is
// no solution, no_sol will be set to true.
// 
// Also, keep in mind the 0-indexing of literals!
//

struct TwoSAT {

    vector<vector<int>> G, G_T;
    vector<int> Viz;
    vector<bool> Sol, True;
    vector<int> Stack;
    bool no_sol;
    int n;

    TwoSAT(int n) : n(n), G(2 * n), G_T(2 * n), Viz(2 * n), 
        Sol(n, 0), True(2 * n, 0) {

        Stack.reserve(2 * n);
    }

    void AddEdge(int a, bool pa, int b, bool pb) {
        G[2 * a + pa].push_back(2 * b + pb);
        G_T[2 * b + pb].push_back(2 * a + pa);
    }

    void dfs_forward(int node) {
        Viz[node] = true;

        for(auto vec : G[node]) {
            if(!Viz[vec])
                dfs_forward(vec);
        }

        Stack.push_back(node);
    }

    void dfs_backward(int node) {

        // Set node's truth value to false      
        if(True[node])
            no_sol = true;
        Viz[node] = true;
        True[node ^ 1] = true;

        Sol[node / 2] = (node & 1 ^ 1);
        
        // Whatever implies false is false
        for(auto vec : G_T[node]) {
            if(!Viz[vec])
                dfs_backward(vec);
        }
    }

    void Solve() {
        fill(Viz.begin(), Viz.end(), 0);
        for(int i = 0; i < 2 * n; ++i) {
            if(!Viz[i])
                dfs_forward(i);
        }

        no_sol = false;
        fill(Viz.begin(), Viz.end(), 0);
        for(int i = 2 * n - 1; i >= 0; --i) {
            if(!Viz[Stack[i]] && !Viz[Stack[i] ^ 1])
                dfs_backward(Stack[i]);
        }
    }
};


vector<int> append(vector<int> a, vector<int> b) {
    if (a == DEFAULT || b == DEFAULT) 
        return DEFAULT;
    vector<int> ret;
    for (auto x : a) ret.push_back(x);
    for (auto x : b) ret.push_back(x);
    return ret;
}

struct Solver {
    vector<string> Mat;
    string OK;
    int n, m;
    vector<vector<int>> A, B;
    vector<vector<int>> Need;
    string LaserChosen;

    int cell2ind(int i, int j) {
        return i * m + j;
    }
    char cell_at(int ind) {
        return Mat[ind / m][ind % m];
    }

    vector<int> GetLasers() {
        vector<int> ret;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (Mat[i][j] == '-' || Mat[i][j] == '|')
                    ret.push_back(cell2ind(i, j));
        return ret;
    }

    vector<int> SimulateLaser(int i, int j, int dir) {
        vector<int> ret;
        while (true) {
            i += dx[dir]; j += dy[dir];
            if (i < 0 || j < 0 || i >= n || j >= m || Mat[i][j] == '#')
                break;
            if (Mat[i][j] == '-' || Mat[i][j] == '|') 
                return DEFAULT;

            ret.push_back(cell2ind(i, j));
            if (Mat[i][j] == '/') dir = pair_slash[dir];
            if (Mat[i][j] == '\\') dir = pair_rslash[dir];
        }
        return ret;
    }

    void Paint(vector<int> V) {
        if (V == DEFAULT) return;

        cerr << endl;
        vector<string> ret(n, string(m, '.'));
        for (auto p : V)
            ret[p / m][p % m] = '#';
        for (auto s : ret)
            cerr << s << endl;
        cerr << endl;
    }

    void Impossible() {
        cout << "IMPOSSIBLE" << endl;
    }

    void ChooseA(int laser) {
        cerr << laser << " chosen horizontally\n";
        LaserChosen[laser] = 'T';
        Mat[laser / m][laser % m] = '-';
        for (auto x : A[laser])
            OK[x] = 'T';
    }
    void ChooseB(int laser) {
        cerr << laser << " chosen vertically\n";
        LaserChosen[laser] = 'T';
        Mat[laser / m][laser % m] = '|';
        for (auto x : B[laser])
            OK[x] = 'T';
    }
    void Choose(int what) {
        if (what >= 0) return ChooseA(what);
        return ChooseB(-what - 1);
    }

    vector<int> Prune(vector<int> old) {
        vector<int> ret;
        for (auto what : old) {
            int l = what;
            if (what < 0) l = -l - 1;
            if (LaserChosen[l] == 'F') ret.push_back(what);
        }
        return ret;
    }

    void Solve() {
        cerr << "---------\n";
        cin >> n >> m;
        Mat = vector<string>(n);
        for (auto &s : Mat)
            cin >> s;
        A.resize(n * m); B.resize(n * m);
        Need.resize(n * m);

        OK = LaserChosen = string(n * m, 'F');
        for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            if (Mat[i][j] == '#' || Mat[i][j] == '-' || Mat[i][j] == '|')
                OK[cell2ind(i, j)] = 'T';
            if (Mat[i][j] != '-' && Mat[i][j] != '|')
                LaserChosen[cell2ind(i, j)] = 'T';
        }

        cerr << "Getting lasers...\n";
        auto lasers = GetLasers();
        for (auto laser : lasers) {
            A[laser] = append(SimulateLaser(laser / m, laser % m, 0),
                SimulateLaser(laser / m, laser % m, 2));
            B[laser] = append(SimulateLaser(laser / m, laser % m, 1),
                SimulateLaser(laser / m, laser % m, 3));


            cerr << "laser: " << laser << endl;
            cerr << "A:\n";
            Paint(A[laser]);
            cerr << "B:\n";
            Paint(B[laser]);


            if (A[laser] == DEFAULT && B[laser] == DEFAULT)
                return Impossible();
            else if (A[laser] == DEFAULT) ChooseB(laser);
            else if (B[laser] == DEFAULT) ChooseA(laser);
            else {
                // Propagate
                for (auto x : A[laser]) Need[x].push_back(laser);
                for (auto x : B[laser]) Need[x].push_back(-laser - 1);
            }
        }

        cerr << "Building constraints...\n";
        for (int i = 0; i < n * m; ++i) {
            if (OK[i] == 'T') continue;
            Need[i] = Prune(Need[i]);
            assert(Need[i].size() <= 2);
            if (Need[i].empty()) {
                cerr << "Bad at: " << i << endl;
                return Impossible();
            }
            if (Need[i].size() == 1) Need[i].push_back(Need[i].back());
        }
    

        cerr << "Solving 2sat...\n";
        TwoSAT sat(n * m);
        for (int i = 0; i < n * m; ++i) {
            if (OK[i] == 'T') continue;

            int a = Need[i][0], b = Need[i][1];
            bool ba = false, bb = false;
            if (a < 0) ba = true, a = -a - 1;
            if (b < 0) bb = true, b = -b - 1;

            sat.AddEdge(a, not ba, b, bb);
            sat.AddEdge(b, not bb, a, ba);
        }

        sat.Solve();
        if (sat.no_sol) return Impossible();
        
        for (int i = 0; i < n * m; ++i) {
            if (LaserChosen[i] == 'T') continue;

            if (sat.Sol[i]) ChooseB(i);
            else ChooseA(i);
        }

        cout << "POSSIBLE\n";
        for (auto x : Mat) 
            cout << x << endl;
    }
};

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        Solver().Solve();
        cerr << "Done case #" << tt << endl;
    }

    return 0;
}