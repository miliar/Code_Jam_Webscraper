#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int DX[] = {-1, 0, 1, 0};
int DY[] = {0, 1, 0, -1};
vector <int> selected;
bool solution_found;
string solution;

void bt(vector <vector<pair<int, int> > > &needed, vector<string> &G, int idx) {
    if (solution_found) {
        return;
    }
    if (idx == needed.size()) {
        solution_found = true;
        solution = "POSSIBLE";
        int n = 0;
        for (int i = 0; i < G.size(); i++) {
            solution += "\n";
            for (int j = 0; j < G[i].size(); j++) {
                if (G[i][j] == '-' || G[i][j] == '|') {
                    if (selected[n] == 0) {
                        solution += '-';
                    } else {
                        solution += '|';
                    }
                    n++;
                } else {
                    solution += G[i][j];
                }
            }
        }
        return;
    }
    for (int i = 0; i < needed[idx].size(); i++) {
        int s = needed[idx][i].first;
        int d = needed[idx][i].second;
        if (selected[s] == d) {
            bt(needed, G, idx + 1);
            continue;
        }
        if (selected[s] != -1) {
            continue;
        }
        selected[s] = d;
        bt(needed, G, idx + 1);
        selected[s] = -1;
    }
}

pair<vector <int>, vector<int> > trace(vector <string> &G,
        vector<vector<int> > &f, pair<int, int> p) {
    vector <int> hor;
    vector <int> ver;
    int x = p.first;
    int y = p.second;
    bool xh, xv;
    xh = false;
    xv = false;
    int d = 0;
    while (true) {
        x += DX[d];
        y += DY[d];
        if (x < 0 || y < 0 || x >= G.size() || y >= G[0].size()) {
            break;
        }
        if (G[x][y] == '#') {
            break;
        }
        if (G[x][y] == '-' || G[x][y] == '|') {
            xv = true;
            break;
        }
        if (G[x][y] == '\\') {
            d = 3 - d;
        }
        if (G[x][y] == '/') {
            if (d < 2) {
                d = 1 - d;
            } else {
                d = 5 - d;
            }
        }
        if (f[x][y] >= 0) {
            ver.push_back(f[x][y]);
        }
    }
    d = 2; x = p.first; y = p.second;
    while (true) {
        x += DX[d];
        y += DY[d];
        if (x < 0 || y < 0 || x >= G.size() || y >= G[0].size()) {
            break;
        }
        if (G[x][y] == '#') {
            break;
        }
        if (G[x][y] == '-' || G[x][y] == '|') {
            xv = true;
            break;
        }
        if (G[x][y] == '\\') {
            d = 3 - d;
        }
        if (G[x][y] == '/') {
            if (d < 2) {
                d = 1 - d;
            } else {
                d = 5 - d;
            }
        }
        if (f[x][y] >= 0) {
            ver.push_back(f[x][y]);
        }
    }
    d = 1;
    x = p.first; y = p.second;
    while (true) {
        x += DX[d];
        y += DY[d];
        if (x < 0 || y < 0 || x >= G.size() || y >= G[0].size()) {
            break;
        }
        if (G[x][y] == '#') {
            break;
        }
        if (G[x][y] == '-' || G[x][y] == '|') {
            xh = true;
            break;
        }
        if (G[x][y] == '\\') {
            d = 3 - d;
        }
        if (G[x][y] == '/') {
            if (d < 2) {
                d = 1 - d;
            } else {
                d = 5 - d;
            }
        }
        if (f[x][y] >= 0) {
            hor.push_back(f[x][y]);
        }
    }
    d = 3;
    x = p.first; y = p.second;
    while (true) {
        x += DX[d];
        y += DY[d];
        if (x < 0 || y < 0 || x >= G.size() || y >= G[0].size()) {
            break;
        }
        if (G[x][y] == '#') {
            break;
        }
        if (G[x][y] == '-' || G[x][y] == '|') {
            xh = true;
            break;
        }
        if (G[x][y] == '\\') {
            d = 3 - d;
        }
        if (G[x][y] == '/') {
            if (d < 2) {
                d = 1 - d;
            } else {
                d = 5 - d;
            }
        }
        if (f[x][y] >= 0) {
            hor.push_back(f[x][y]);
        }
    }
    if (xh) {
        hor = vector<int>(1, -1);
    }
    if (xv) {
        ver = vector<int>(1, -1);
    }
    sort(hor.begin(), hor.end());
    hor.erase(unique(hor.begin(), hor.end()), hor.end());
    sort(ver.begin(), ver.end());
    ver.erase(unique(ver.begin(), ver.end()), ver.end());
    return make_pair(hor, ver);
}

string doit() {
    string IMPOSSIBLE = "IMPOSSIBLE\n";
    int R, C;
    cin >> R >> C;
    vector <string> G;
    vector <vector <int> > f(R, vector<int>(C, -1));
    vector <pair <int, int> > m;
    int n = 0;
    // cerr << R << " " << C << endl;
    for (int i = 0; i < R; i++) {
        string x;
        cin >> x;
        G.push_back(x);
        for (int j = 0; j < C; j++) {
            if (G[i][j] == '-' || G[i][j] == '|') {
                m.push_back(make_pair(i, j));
            }
            if (G[i][j] == '.') {
                f[i][j] = n++;
            }
        }
        // cerr << G[i] << endl;
    }
    vector <vector<pair<int, int> > > needed(n, vector<pair<int, int> >());
    selected = vector<int>(n, -1);
    for (int i = 0; i < m.size(); i++) {
        // cerr << i << endl;
        pair<vector <int>, vector<int> > cells = trace(G, f, m[i]);
        bool x0, x1;
        x0 = false;
        x1 = false;
        if (cells.first.size() == 1 && cells.first[0] == -1) {
            x0 = true;
        }
        if (cells.second.size() == 1 && cells.second[0] == -1) {
            x1 = true;
        }
        if (x0 && x1) {
            return IMPOSSIBLE;
        }
        if (x0) {
            selected[i] = 1;
        }
        if (x1) {
            selected[i] = 0;
        }
        if (!x0) {
            for (int j = 0; j < cells.first.size(); j++) {
                needed[cells.first[j]].push_back(make_pair(i, 0));
            }
        }
        if (!x1) {
            for (int j = 0; j < cells.second.size(); j++) {
                needed[cells.second[j]].push_back(make_pair(i, 1));
            }
        }
    }
    /*
    for (int i = 0; i < n; i++) {
        cout << i << ": ";
        for (int j = 0; j < needed[i].size(); j++) {
            cout << needed[i][j].first << "." << needed[i][j].second << " ";
        }
        cout << endl;
    }
    cerr << "DONE" << endl;
    */
    solution_found = false;
    bt(needed, G, 0);
    if (solution_found) {
        return solution;
    }
    return IMPOSSIBLE;
}

int main(int argc, char *argv[]) {
    int C;
    cin >> C;
    for (int i = 1; i <= C; i++) {
        string res = doit();
        cout << "Case #" << i << ": " << res << endl;;
    }
    return 0;
}
