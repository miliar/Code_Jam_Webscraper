#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<string> ret_t;
typedef vector<vector<int> > vvi;

class Tarjan {
public:
    /* call with:
    Tarjan T(g);
    T.tarjan();
    */
    int n;
    vector<vector<int> > g;
    int nscc;
    vector<vector<int> > scc; // scc id -> vector of node ids
    vector<int> inscc; // node id -> scc id
    vector<int> sccpos; // node id -> id within scc
    vector<int> sccsize; // scc id -> size
    // each scc has edges only to lower scc's (i.e. reverse topological sort)
    Tarjan(vector<vector<int> > _g):n(_g.size()), g(_g), nscc(0) {
        inscc = vector<int>(n);
        sccpos = vector<int>(n);
    }
    void doTarjan(int v, int & index, stack<int> & S, vector<bool> & onStack, vector<int> & vIndex, vector<int> & vLowlink, int from) {
        vIndex[v] = vLowlink[v] = index++;
        S.push(v);
        onStack[v] = true;
        for (int i = 0; i < g[v].size(); ++i) {
            int w = g[v][i];
            //if (w == from) continue; // for undirected graphs //???
            if (vIndex[w] == -1) {
                doTarjan(w, index, S, onStack, vIndex, vLowlink, v);
                vLowlink[v] = min(vLowlink[v], vLowlink[w]);
            }
            else if (onStack[w]) {
                vLowlink[v] = min(vLowlink[v], vIndex[w]);
            }
        }
        if (vLowlink[v] == vIndex[v]) {
            int pos = 0;
            int w = S.top();
            S.pop();
            onStack[w] = false;
            //if (w!=v) cout<<"SCC:\t"<<w<<endl;
            scc.push_back(vector<int>(1, w));
            inscc[w] = nscc;
            sccpos[w] = pos++;
            while (w != v) {
                w = S.top();
                S.pop();
                onStack[w] = false;
                //cout<<'\t'<<w<<endl;
                scc[nscc].push_back(w);
                inscc[w] = nscc;
                sccpos[w] = pos++;
            }
            sccsize.push_back(pos);
            nscc++;
        }
    }
    void tarjan() {
        int index = 0;
        stack<int> S;
        vector<bool> onStack(n, false);
        vector<int> vIndex(n, -1);
        vector<int> vLowlink(n, -1);
        for (int v = 0; v < n; ++v) {
            if (vIndex[v] == -1) {
                doTarjan(v, index, S, onStack, vIndex, vLowlink, -1);
            }
        }
    }
};

class Solver {
public:
    int h, w;
    vector<string> a;
    vvi ind, fn, fs, fe, fw;
    void trace(int x, int y, int dir, int src) {
        while (true) {
            // move x,y
            switch (dir) {
            case 0: --x; break;
            case 1: ++x; break;
            case 2: ++y; break;
            case 3: --y; break;
            }
            // stop?
            if (x < 0 || y < 0 || x >= h || y >= w)
                break;
            if (a[x][y] == '#')
                break;
            if (a[x][y] == '/') {
                // change dir at mirror
                switch (dir) {
                case 0: dir = 2; break;
                case 1: dir = 3; break;
                case 2: dir = 0; break;
                case 3: dir = 1; break;
                }
            }
            else if (a[x][y] == '\\') {
                // change dir at mirror
                switch (dir) {
                case 0: dir = 3; break;
                case 1: dir = 2; break;
                case 2: dir = 1; break;
                case 3: dir = 0; break;
                }
            }
            else {
                // record (on '.' or beam shooter)
                switch (dir) {
                case 0: fs[x][y] = src; break;
                case 1: fn[x][y] = src; break;
                case 2: fw[x][y] = src; break;
                case 3: fe[x][y] = src; break;
                }
            }
        }
    }
    ret_t solve(vector<string> _a) {
        a = _a;
        ret_t ret(a);
        ret_t fail(0);
        h = a.size();
        w = a[0].size();
        ind = vvi(h, vector<int>(w, -1));
        fn = vvi(h, vector<int>(w, -1));
        fs = vvi(h, vector<int>(w, -1));
        fe = vvi(h, vector<int>(w, -1));
        fw = vvi(h, vector<int>(w, -1));
        int num_beams = 0;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (a[i][j] == '-' || a[i][j] == '|') {
                    int cur = num_beams++;
                    ind[i][j] = cur;
                    for (int dir = 0; dir < 4; ++dir)
                        trace(i, j, dir, (cur << 2) + dir);
                }
            }
        }
        /*cerr << "from E:" << endl;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                cerr << fe[i][j] << '\t';
            }
            cerr << endl;
            }*/

        vvi g(2 * num_beams, vector<int>(0));
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (ind[i][j] >= 0) {
                    if (fn[i][j] >= 0) {
                        int v = (fn[i][j] >> 1);
                        int w = (v ^ 1);
                        //cerr << "forbid: " << v << " -> " << w << endl;
                        g[v].push_back(w);
                    }
                    if (fs[i][j] >= 0) {
                        int v = (fs[i][j] >> 1);
                        int w = (v ^ 1);
                        //cerr << "forbid: " << v << " -> " << w << endl;
                        g[v].push_back(w);
                    }
                     if (fe[i][j] >= 0) {
                        int v = (fe[i][j] >> 1);
                        int w = (v ^ 1);
                        //cerr << "forbid: " << v << " -> " << w << endl;
                        g[v].push_back(w);
                    }
                     if (fw[i][j] >= 0) {
                        int v = (fw[i][j] >> 1);
                        int w = (v ^ 1);
                        //cerr << "forbid: " << v << " -> " << w << endl;
                        g[v].push_back(w);
                    }
                }
                else if (a[i][j] == '.') {
                    int ns = fn[i][j];
                    if (ns < 0) ns = fs[i][j];
                    int ew = fe[i][j];
                    if (ew < 0) ew = fw[i][j];
                    if (ns < 0 && ew < 0) {
                        return fail;
                    }
                    else if (ns < 0) {
                        int w = (ew >> 1); // v = ((ew >> 2) << 1);
                        int v = w ^ 1;
                        //cerr << "reqr 1: " << v << " -> " << w << endl;
                        g[v].push_back(w);
                    }
                    else if (ew < 0) {
                        //int v = ((ns >> 2) << 1);
                        //int w = v | 1;
                        int w = (ns >> 1);
                        int v = w ^ 1;
                        //cerr << "reqr 2: " << v << " -> " << w << endl;
                        g[v].push_back(w);
                    }
                    else {
                        int v = (ns >> 1);
                        int w = (ew >> 1);
                        //cerr << "either: " << (v ^ 1) << " -> " << w << endl;
                        g[v ^ 1].push_back(w);
                        //cerr << "    or: " << (w ^ 1) << " -> " << v << endl;
                        g[w ^ 1].push_back(v);
                    }
                }
            }
        }

        Tarjan T(g);
        T.tarjan();
        for (int i = 0; i < num_beams; ++i) {
            if (T.inscc[(i << 1)] == T.inscc[(i << 1) | 1])
                return fail;
        }
        for (int i = 0; i < num_beams; ++i) {
            //cerr << i << ":\t" << T.inscc[(i << 1)] << '\t' << T.inscc[(i << 1) | 1] << endl;
        }
        string ans(num_beams, '?');
        for (int i = 0; i < T.nscc; ++i) {
            vector<int> scc = T.scc[i];
            for (int j = 0; j < scc.size(); ++j) {
                int v = scc[j];
                int k = (v >> 1);
                if (ans[k] == '?') {
                    if (v & 1)
                        ans[k] = '-';
                    else
                        ans[k] = '|';
                }
            }
        }
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (ind[i][j] >= 0) {
                    ret[i][j] = ans[ind[i][j]];
                }
            }
        }

        return ret;
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr //<< "Case "
            << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int h, w;
        {
            stringstream A(s);
            A >> h >> w;
        }
        vector<string> a(h, "");
        for (int i = 0; i < h; ++i) {
            getline(cin, a[i]);
        }
        ret_t ret = solver.solve(a);

        // *** give output ***
        cout << "Case #" << no << ": ";
        if (ret.size()) {
            cout << "POSSIBLE" << endl;
            for (int i = 0; i < ret.size(); ++i)
                cout << ret[i] << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
        //cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
