#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

struct field {
    bool x = false;
    bool p = false;

    bool operator!=(field other)
    {
        return x != other.x || p != other.p;
    }
};

ostream& operator<<(ostream& out, field f)
{
    if (f.x && f.p) out << 'o';
    else if (f.x) out << 'x';
    else if (f.p) out << '+';
    else out << '.';
    return out;
}


int n, m;
vector<vector<field>> f;


bool valid_x(int r, int c)
{
    for (int cc = 0; cc < n; ++cc) {
        if (f[r][cc].x) return false;
    }
    for (int rr = 0; rr < n; ++rr) {
        if (f[rr][c].x) return false;
    }
    return true;
}

bool valid_p(int r, int c)
{
    for (int d = -min(r, c); d + max(r, c) < n; ++d) {
        if (f[r + d][c + d].p) return false;
    }
    c += r;
    r = 0;
    while (c >= n) {
        --c;
        ++r;
    }
    while (c >= 0 && r < n) {
        if (f[r][c].p) return false;
        --c;
        ++r;
    }
    return true;
}

void solve(int)
{
    cin >> n >> m;

    f.assign(n, vector<field>(n));

    for (int i = 0; i < m; ++i) {
        char type;
        int r, c;
        cin >> type >> r >> c;
        --r; --c;
        if (type == '+' || type == 'o') f[r][c].p = true;
        if (type == 'x' || type == 'o') f[r][c].x = true;
    }

    auto grid_copy = f;



    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            if (valid_x(r, c)) {
                f[r][c].x = true;
            }
        }
    }

    for (int c = 0; c < n; ++c) {
        for (int r: {0, n - 1}) {
            if (valid_p(r, c)) {
                f[r][c].p = true;
            }
        }
    }
    for (int r = 0; r < n; ++r) {
        for (int c: {0, n - 1}) {
            if (valid_p(r, c)) {
                f[r][c].p = true;
            }
        }
    }


    int y = 0, z = 0;
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            field t = f[r][c];
            y += t.p + t.x;
            if (t != grid_copy[r][c]) ++z;
        }
    }
    cout << y << " " << z << "\n";

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            field t = f[r][c];
            if (t != grid_copy[r][c]) {
                cout << t << " " << r + 1 << " " << c + 1 << "\n";
            }
        }
    }
    cout << flush;
    assert(y == 2 * n - min(2, n) + n);
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
