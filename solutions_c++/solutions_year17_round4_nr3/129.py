#include <bits/stdc++.h>
using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
    assert(scanf("%d", &CASES) == 1);
}

int dprintf(const char *err, ...) {
    if (debug) {
        va_list pvar;
        va_start(pvar, err);
        return vfprintf(stderr, err, pvar);
    }
    return 0;
}


int R, C;
char grid[200][200];

pii trace(int r, int c, int dr, int dc, bool &end_horz) {
    r += dr; c += dc;
    if (r < 0 || c < 0 || r >= R || c >= C || grid[r][c] == '-' || grid[r][c] == '|' || grid[r][c] == '#') {
        end_horz = (dr == 0);
        return pii(r, c);
    }
    if (grid[r][c] == '/') {
        swap(dr, dc);
        dr = -dr; dc = -dc;
    } else if (grid[r][c] == '\\') {
        swap(dr, dc);
    }
    return trace(r, c, dr, dc, end_horz);
}

bool beam(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C && (grid[r][c] == '-' || grid[r][c] == '|');
}

int assign[100][100];

bool simplify(vector<vector<int>> &F) {
    queue<int> units;
    for (auto &C: F) {
        if (C.size() == 1)
            units.push(C.front());
    }
    while (!units.empty()) {
        int L = units.front(); units.pop();
        int r = (abs(L)-1)/C, c = (abs(L)-1)%C;
        assign[r][c] = L > 0;
        for (int i = F.size()-1; i >= 0; --i) {
            int psize = F[i].size();
            for (int j = F[i].size()-1; j >= 0; --j) {
                if (F[i][j] == L) {
                    F.erase(F.begin() + i);
                    break;
                } else if (F[i][j] == -L) {
                    F[i].erase(F[i].begin() + j);
                }
            }
            if (F[i].size() == 0) return false;
            if (F[i].size() == 1 && psize > 1) {
                units.push(F[i].front());
            }
        }
    }
    return true;
}

int satisfy(vector<vector<int>> F) {
    if (!simplify(F))
        return -1;
    if (F.empty()) return 1;
    int L = F.front().front();
    F.push_back(vi(1, L));
    int r = satisfy(F);
    if (r == -1) {
        F.back().front() = -L;
        r = satisfy(F);
    }
    return r == 1;
}

bool doit() {
    vector<vector<int>> clauses;
    bool dummy;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (grid[i][j] == '-' || grid[i][j] == '|') {
                bool vert_ok = true, horz_ok = true;
                pii A = trace(i, j, -1, 0, dummy), B = trace(i, j, 1, 0, dummy);
                vert_ok = !beam(A.first, A.second) && !beam(B.first, B.second);
                A = trace(i, j, 0, 1, dummy), B = trace(i, j, 0, -1, dummy);
                horz_ok = !beam(A.first, A.second) && !beam(B.first, B.second);
                if (!vert_ok && !horz_ok) return false;
                if (!vert_ok) {
                    clauses.push_back(vi(1, i*C + j + 1));
                }
                if (!horz_ok) {
                    clauses.push_back(vi(1, -(i*C + j + 1)));
                }
            } else if (grid[i][j] == '.') {
                vector<int> Cl;
                bool Ah, Bh;
                pii A = trace(i, j, -1, 0, Ah), B = trace(i, j, 1, 0, Bh);
                if (beam(A.first, A.second) && beam(B.first, B.second))
                    return false;
                if (beam(B.first, B.second)) {
                    A = B;
                    Ah = Bh;
                }
                if (beam(A.first, A.second)) {
                    Cl.push_back(A.first*C + A.second + 1);
                    if (!Ah) Cl.back() = -Cl.back();
                }

                A = trace(i, j, 0, -1, Ah), B = trace(i, j, 0, 1, Bh);
                if (beam(A.first, A.second) && beam(B.first, B.second))
                    return false;
                if (beam(B.first, B.second)) {
                    A = B;
                    Ah = Bh;
                }
                if (beam(A.first, A.second)) {
                    Cl.push_back(A.first*C + A.second + 1);
                    if (!Ah) Cl.back() = -Cl.back();
                }

                if (Cl.empty()) return false;

                clauses.push_back(Cl);
            }
        }
    }

    return satisfy(clauses) == 1;
}

void solve(int P) {
    scanf("%d%d", &R, &C);
    for (int i = 0; i < R; ++i)
        scanf("%s", grid[i]);

    printf("Case #%d: ", P);
    if (!doit()) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("POSSIBLE\n");
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (beam(i, j))
                    grid[i][j] = assign[i][j] > 0 ? '-' : '|';
            }
            printf("%s\n", grid[i]);
        }
    }
}

int main(void) {
    init();
    for (int i = 1; i <= CASES; ++i) solve(i);
    return 0;
}
