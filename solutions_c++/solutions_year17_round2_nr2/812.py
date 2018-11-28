#include <iostream>
#include <vector>

using namespace std;


vector<char> clr;
vector<char> res;

int n, r, o, y, g, b, v;

void cerrVector(vector<char> &v) {
    cerr << "\n > ";
    for (int i = 0; i < v.size(); ++i)
        cerr << v[i];
    cerr << "\n";
}

char getNxt(char cur, int &r, int &y, int &b) {
    int m;
    if (cur == 'R')
        m = max(y, b);
    else if (cur == 'Y')
        m = max(r, b);
    else if (cur == 'B')
        m = max(y, r);
    else
        m = max(r, max(y, b));

    if (m == 0)
        return 0;

    if (m == r && cur != 'R') {
        --r;
        return 'R';
    }
    else if (m == y && cur != 'Y') {
        --y;
        return 'Y';
    }
    else if (m == b && cur != 'B') {
        --b;
        return 'B';
    }
    else {
        cerr << "ERROR\n";
        return 0;
    }
}

bool solve() {
    // cin >> n >> r >> o >> y >> g >> b >> v;
    // r y b
    // cerr << n << r << y << b << "\n";
    char cur = 0;
    for (int i = 0; i < n; ++i) {
        cur = getNxt(cur, r, y, b);
        if (cur)
            res.push_back(cur);
        else {
            cout << "IMPOSSIBLE\n";
            return false;
        }
    }
    // cout << res.size();
    if (res[0] == res[n - 1]) {
        if (n == 1) {
            cout << "IMPOSSIBLE\n";
            return false;
        }
        // cerr << "fix gogo\n";
        // ye boi more 'fixes'
        cur = res[n - 1];
        int i;
        for (i = 1; i + 1 < n && (res[i] == cur || res[i + 1] == cur); ++i) {
        }
        if (i == n - 1) {
            cout << "IMPOSSIBLE\n";
            return false;
        }

        clr.clear();
        for (int j = 0; j <= i; ++j)
            clr.push_back(res[j]);
        clr.push_back(cur);
        for (int j = i + 1; j + 1 < n; ++j)
            clr.push_back(res[j]);

        swap(res, clr);
        return true;

        // bad code :C
    }
    // for (int i = 0; i < n; ++i)
    //     cout << res[i];
    // cout << "\n";
    return true;
}

void solve2() {
    res.clear();
    cin >> n >> r >> o >> y >> g >> b >> v;
    if (o == b && o + b == n) {
        for (int i = 0; i * 2 < n; ++i)
            cout << "OB";
        cout << "\n";
        return;
    }
    if (g == r && g + r == n) {
        for (int i = 0; i * 2 < n; ++i)
            cout << "GR";
        cout << "\n";
        return;
    }
    if (v == y && v + y == n) {
        for (int i = 0; i * 2 < n; ++i)
            cout << "VY";
        cout << "\n";
        return;
    }

    // cerr << "here " << o << g << v << "\n";

    if ((b <= o && o) || (r <= g && g) || (y <= v && v)){
        cout << "IMPOSSIBLE\n";
        return;
    }

    n -= o; b -= o;
    n -= g; r -= g;
    n -= v; y -= v;
    n = b + r + y;
    if (!solve())
        return;

    // cerrVector(res);

    int i, j;

    clr.clear();
    for (i = 0; i < res.size() && res[i] != 'B'; ++i) {
    } // 'code style' in shitcode oh ye
    for (j = 0; j < i; ++j)
        clr.push_back(res[j]);
    for (j = 0; j < o; ++j) {
        clr.push_back('B');
        clr.push_back('O');
    }
    for (j = i; j < res.size(); ++j)
        clr.push_back(res[j]);
    swap(res, clr);

    clr.clear();
    for (i = 0; i < res.size() && res[i] != 'R'; ++i) {
    } // 'code style' in shitcode oh ye
    for (j = 0; j < i; ++j)
        clr.push_back(res[j]);
    for (j = 0; j < g; ++j) {
        clr.push_back('R');
        clr.push_back('G');
    }
    for (j = i; j < res.size(); ++j)
        clr.push_back(res[j]);
    swap(res, clr);

    clr.clear();
    for (i = 0; i < res.size() && res[i] != 'Y'; ++i) {
    } // 'code style' in shitcode oh ye
    for (j = 0; j < i; ++j)
        clr.push_back(res[j]);
    for (j = 0; j < v; ++j) {
        clr.push_back('Y');
        clr.push_back('V');
    }
    for (j = i; j < res.size(); ++j)
        clr.push_back(res[j]);
    swap(res, clr);

    for (int i = 0; i < res.size(); ++i)
        cout << res[i];
    cout << "\n";

}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve2();
    }
    return 0;
}