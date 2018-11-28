#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <cassert>
#include "Solver.hpp"
#define repeat(i,n) for (int i = 0; (i) < int(n); ++(i))
#define repeat_from(i,m,n) for (int i = (m); (i) < int(n); ++(i))
#define repeat_reverse(i,n) for (int i = (n)-1; (i) >= 0; --(i))
#define repeat_from_reverse(i,m,n) for (int i = (n)-1; (i) >= int(m); --(i))
#define whole(f,x,...) ([&](decltype((x)) whole) { return (f)(begin(whole), end(whole), ## __VA_ARGS__); })(x)
#define debug(x) #x << " = " << (x) << " "
using ll = long long;
using namespace std;
template <class T> inline void setmax(T & a, T const & b) { a = max(a, b); }
template <class T> inline void setmin(T & a, T const & b) { a = min(a, b); }
template <typename X, typename T> auto vectors(X x, T a) { return vector<T>(x, a); }
template <typename X, typename Y, typename Z, typename... Zs> auto vectors(X x, Y y, Z z, Zs... zs) { auto cont = vectors(y, z, zs...); return vector<decltype(cont)>(x, cont); }

enum dir_t { UP, DOWN, RIGHT, LEFT };
const int dy[] = { -1, 1, 0, 0 };
const int dx[] = { 0, 0, 1, -1 };
dir_t mirror(char c, dir_t d) {
    if (c == '/') {
        switch (d) {
            case UP: return RIGHT;
            case DOWN: return LEFT;
            case RIGHT: return UP;
            case LEFT: return DOWN;
        }
    } else if (c == '\\') {
        switch (d) {
            case UP: return LEFT;
            case DOWN: return RIGHT;
            case RIGHT: return UP;
            case LEFT: return DOWN;
        }
    }
    assert (false);
}

vector<string> solve(int h, int w, vector<string> const & s) {
    // analyze the field
    auto is_on_field = [&](int y, int x) { return 0 <= y and y < h and 0 <= x and x < w; };
    vector<pair<int, int> > shooters;
    repeat (y,h) {
        repeat (x,w) {
            if (s[y][x] == '-' or s[y][x] == '|') {
                shooters.emplace_back(y, x);
            }
        }
    }
    function<bool (int, int, dir_t, vector<pair<int, int> > &)> shoot = [&](int y, int x, dir_t d, vector<pair<int, int> > & acc) {
        int ny = y + dy[d];
        int nx = x + dx[d];
        if (not is_on_field(ny, nx) or s[ny][nx] == '#') { // goal
            return true;
        } else if (s[ny][nx] == '.') {
            acc.emplace_back(ny, nx);
            return shoot(ny, nx, d, acc);
        } else if (s[ny][nx] == '/' or s[ny][nx] == '\\') {
            return shoot(ny, nx, mirror(s[ny][nx], d), acc);
        } else if (s[ny][nx] == '-' or s[ny][nx] == '|') {
            acc.clear();
            return false;
        } else {
            assert (false);
        }
    };
    vector<char> shooter_result(shooters.size(), '\0');
    auto used = vectors(h, w, bool());
    auto vars = vectors(h, w, vector<int>());
    repeat (i, shooters.size()) {
        int y, x; tie(y, x) = shooters[i];
        vector<pair<int, int> > a, b;
        bool is_hr = shoot(y, x, RIGHT, a) and shoot(y, x, LEFT, a);
        bool is_vr = shoot(y, x, UP, b) and shoot(y, x, DOWN, b);
        if (not is_hr and not is_vr) {
            return vector<string>(); // IMPOSSIBLE
        } else if (not is_hr or not is_vr) {
            shooter_result[i] = (is_hr ? '-' : '|');
            if (a.empty()) a.swap(b);
            for (auto it : a) {
                int ay, ax; tie(ay, ax) = it;
                used[ay][ax] = true;
            }
        } else {
            for (auto it : a) {
                int ay, ax; tie(ay, ax) = it;
                vars[ay][ax].push_back(+ (i+1));
            }
            for (auto it : b) {
                int by, bx; tie(by, bx) = it;
                vars[by][bx].push_back(- (i+1));
            }
        }
    }
    // sat
    togasat::Solver solver;
    auto var_at = [&](int y, int x) { return 1 + shooters.size() + y * h + x; };
    vector<pair<int, int> > cnf;
    repeat (y,h) {
        repeat (x,w) if (s[y][x] == '.' and not used[y][x]) {
            vector<int> clause = vars[y][x];
            clause.push_back(- var_at(y, x));
            solver.addClause(clause);
            vector<int> assertion;
            assertion.push_back(var_at(y, x));
            assertion.push_back(var_at(y, x));
            solver.addClause(assertion);
cerr << "add clause";
for (auto var : clause) cerr << " " << var;
cerr << endl;
        }
    }
    togasat::lbool status = solver.solve();
    if (status != 0) return vector<string>(); // IMPOSSIBLE
    repeat (i, shooters.size()) if (not shooter_result[i]) {
        shooter_result[i] = (solver.assigns[i] ? '|' : '-');
    }
    // result
    vector<string> result = s;
    repeat (i, shooters.size()) {
        int y, x; tie(y, x) = shooters[i];
        result[y][x] = shooter_result[i];
    }
    return result;
}

int main() {
    int t; cin >> t;
    repeat (x,t) {
        int h, w; cin >> h >> w;
        vector<string> s(h); repeat (y,h) cin >> s[y];
        vector<string> result = solve(h, w, s);
cerr << "Case #" << x+1 << ": " << (result.empty() ? "IMPOSSIBLE" : "POSSIBLE") << endl;
if (not result.empty()) {
repeat (y,h) cerr << result[y] << endl;
}
        cout << "Case #" << x+1 << ": " << (result.empty() ? "IMPOSSIBLE" : "POSSIBLE") << endl;
        if (not result.empty()) {
            repeat (y,h) cout << result[y] << endl;
        }
    }
    return 0;
}
