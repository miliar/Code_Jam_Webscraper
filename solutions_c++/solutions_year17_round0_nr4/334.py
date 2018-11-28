#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class TMaxBipartiteMatchingFinder {
public:
    TMaxBipartiteMatchingFinder(int n1, int n2)
        : Edges(n1)
        , Matching(n2, -1)
    {
    }

    void AddEdge(int id, int from, int to) {
        Edges[from].push_back(TEdge{from, to, id});
    }

    void Find() {
        vector<bool> used;
        for (int i = 0; i < GetN1(); ++i) {
            used.assign(GetN1(), false);
            TryDfs(i, used);
        }
    }

    int GetN1() {
        return Edges.size();
    }

    int GetN2() {
        return Matching.size();
    }

    vector<int> GetResultEdgeIds() {
        vector<int> result;
        for (int v = 0; v < (int) Edges.size(); ++v) {
            for (const TEdge& e : Edges[v]) {
                if (Matching[e.To] == e.From) {
                    result.push_back(e.Id);
                }
            }
        }
        return result;
    }

private:
    struct TEdge {
        int From;
        int To;
        int Id;
    };

    vector<vector<TEdge>> Edges;
    vector<int> Matching;

    bool TryDfs(int v, vector<bool>& used) {
        if (used[v]) {
            return false;
        }
        used[v] = true;
        for (const TEdge& e : Edges[v]) {
            if (Matching[e.To] == -1 || TryDfs(Matching[e.To], used)) {
                Matching[e.To] = e.From;
                return true;
            }
        }
        return false;
    }
};

class TBaseSolver {
public:
    explicit TBaseSolver(int n)
        : N(n)
        , HasData(n, vector<bool>(n, false))
    {
    }

    void Add(int r, int c) {
        HasData[r][c] = true;
        DoAdd(r, c);
    }

    virtual void Extend() {
    }

    bool Has(int r, int c) {
        return HasData[r][c];
    }

    vector<pair<int, int>> GetExtended() {
        return Extended;
    }

    int GetN() {
        return N;
    }

protected:
    void AddToExtended(int r, int c) {
        Extended.push_back(make_pair(r, c));
        Add(r, c);
    }

private:
    int N;

    vector<vector<bool>> HasData;

    vector<pair<int, int>> Extended;

    virtual void DoAdd(int r, int c) {
    }
};

class TStraightSolver : public TBaseSolver {
public:
    explicit TStraightSolver(int n)
        : TBaseSolver(n)
        , UsedRow(n, false)
        , UsedCol(n, false)
    {
    }

    void Extend() override {
        vector<int> unusedRows;
        vector<int> unusedCols;
        for (int i = 0; i < (int) UsedRow.size(); ++i) {
            if (!UsedRow[i]) {
                unusedRows.push_back(i);
            }
            if (!UsedCol[i]) {
                unusedCols.push_back(i);
            }
        }
        for (int i = 0; i < (int) min(unusedRows.size(), unusedCols.size()); ++i) {
            AddToExtended(unusedRows[i], unusedCols[i]);
        }
    }
private:
    vector<bool> UsedRow;
    vector<bool> UsedCol;

    void DoAdd(int r, int c) override {
        UsedRow[r] = true;
        UsedCol[c] = true;
    }
};

class TDiagonalSolver : public TBaseSolver {
public:
    explicit TDiagonalSolver(int n)
        : TBaseSolver(n)
        , UsedMainDiagonal(2 * n - 1, false)
        , UsedSubDiagonal(2 * n - 1, false)
    {
    }

    void Extend() override {
        // greedy strategy can be also applied
        TMaxBipartiteMatchingFinder finder(2 * GetN() - 1, 2 * GetN() - 1);
        for (int i = 0; i < GetN(); ++i) {
            for (int j = 0; j < GetN(); ++j) {
                const int md = GetMainDiagonalId(i, j);
                const int sd = GetSubDiagonalId(i, j);
                if (UsedMainDiagonal[md] || UsedSubDiagonal[sd]) {
                    continue;
                }
                finder.AddEdge(i * GetN() + j, md, sd);
            }
        }
        finder.Find();
        vector<int> finderEdgeIds = finder.GetResultEdgeIds();
        for (int i : finderEdgeIds) {
            const int r = i / GetN();
            const int c = i % GetN();

            AddToExtended(r, c);
        }
    }
private:
    vector<bool> UsedMainDiagonal;
    vector<bool> UsedSubDiagonal;

    int GetMainDiagonalId(int r, int c) {
        const int d = min(r, c);
        r -= d;
        c -= d;
        if (r == 0) {
            return GetN() + c - 1;
        } else {
            return GetN() - r - 1;
        }
    }

    int GetSubDiagonalId(int r, int c) {
        const int d = min(r, GetN() - 1 - c);
        r -= d;
        c += d;
        if (r == 0) {
            return c;
        } else {
            return r + GetN() - 1;
        }
    }

    void DoAdd(int r, int c) override {
        UsedMainDiagonal[GetMainDiagonalId(r, c)] = true;
        UsedSubDiagonal[GetSubDiagonalId(r, c)] = true;
    }
};

const char DIAGONAL_SIGN = 'x';
const char STRAIGHT_SIGN = '+';
const char BOTH_SIGN = 'o';
const char EMPTY_SIGN = '.';

int n, m;
vector<char> signs;
vector<int> rows;
vector<int> cols;

void Solve() {
    TStraightSolver ss(n);
    TDiagonalSolver ds(n);

    for (int i = 0; i < m; ++i) {
        if (signs[i] == DIAGONAL_SIGN) {
            ss.Add(rows[i], cols[i]);
        } else if (signs[i] == STRAIGHT_SIGN) {
            ds.Add(rows[i], cols[i]);
        } else {
            ss.Add(rows[i], cols[i]);
            ds.Add(rows[i], cols[i]);
        }
    }

    ss.Extend();
    ds.Extend();

    vector<pair<int, int>> straightExtended = ss.GetExtended();
    vector<pair<int, int>> diagonalExtended = ds.GetExtended();

    vector<vector<char>> field(n, vector<char>(n, EMPTY_SIGN));
    for (const auto& se : straightExtended) {
        if (ds.Has(se.first, se.second)) {
            field[se.first][se.second] = BOTH_SIGN;
        } else {
            field[se.first][se.second] = DIAGONAL_SIGN;
        }
    }
    for (const auto& de : diagonalExtended) {
        if (ss.Has(de.first, de.second)) {
            field[de.first][de.second] = BOTH_SIGN;
        } else {
            field[de.first][de.second] = STRAIGHT_SIGN;
        }
    }

    int resultValue = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (ss.Has(i, j)) {
                ++resultValue;
            }
            if (ds.Has(i, j)) {
                ++resultValue;
            }
        }
    }

    vector<char> resultSign;
    vector<int> resultRow;
    vector<int> resultCol;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (field[i][j] != EMPTY_SIGN) {
                resultSign.push_back(field[i][j]);
                resultRow.push_back(i);
                resultCol.push_back(j);
            }
        }
    }

    cout << resultValue << " " << resultSign.size() << endl;
    for (int i = 0; i < (int) resultSign.size(); ++i) {
        cout << resultSign[i] << " " << resultRow[i] + 1 << " " << resultCol[i] + 1 << endl;
    }
}

void Read() {
    cin >> n >> m;
    signs.resize(m);
    rows.resize(m);
    cols.resize(m);
    for (int i = 0; i < m; ++i) {
        cin >> signs[i] >> rows[i] >> cols[i];
        --rows[i];
        --cols[i];
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        Read();
        cout << "Case #" << test << ": ";
        Solve();
    }

    return 0;
}
