#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <iomanip>
#include <string>

using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;
typedef pair<int, int> PII;

string genring(int dbsz, string db, string one) {
    string ring = "";
    for (int i = 0; i < dbsz; ++i) ring += db;
    ring += one;
    return ring;
}
struct Col {
    char c;
    int num;
    Col(char c, int num) : c(c), num(num) {}
    bool operator>(const Col& cl) const {
        return num > cl.num;
    }
    bool operator<(const Col& cl) const {
        return num < cl.num;
    }
};

char getmaxofotheranddecrease(vector<Col>& cols, char ntu) {
    if ((cols[0].num >= cols[1].num && ntu == cols[2].c) ||
        (cols[0].num >= cols[2].num && ntu == cols[1].c)) {
        --cols[0].num;
        return cols[0].c;
    }
    if ((cols[1].num >= cols[0].num && ntu == cols[2].c) ||
        (cols[1].num >= cols[2].num && ntu == cols[0].c)) {
        --cols[1].num;
        return cols[1].c;
    }
    --cols[2].num;
    return cols[2].c;
}

string solve_small(int r, int b, int y) {
    vector<Col> cols;
    cols.push_back(Col('R', r));
    cols.push_back(Col('B', b));
    cols.push_back(Col('Y', y));
    sort(cols.begin(), cols.end());
    reverse(cols.begin(), cols.end());
    int n = r+b+y;
    string sol(n, cols[0].c);
    --cols[0].num;
    for (int i = 1; i < n; ++i) {
        sol[i] = getmaxofotheranddecrease(cols, sol[i-1]);
    }
    return sol;
}

int main() {
    ios::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        cout << "Case #" << tc << ": ";
        int r, rc;
        int b, bc;
        int y, yc;
        int n;
        cin >> n >> r >> bc >> y >> rc >> b >> yc;
        string rring = "", yring = "", bring = "";
        if (((r+rc == n && r != rc) || (r+rc < n && r+1 < rc)) || ((y+yc == n && y != yc) || (y+yc < n && y+1 < yc)) ||
            ((b+bc == n && b != bc) || (b+bc < n && b+1 < bc)) ||
            (rc > r || yc > y || bc > b) ||
            (r && rc == r && r+rc < n) || (y && yc == y && y+yc < n) || (b && bc == b && b+bc < n)) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        if (rc) {
            rring = genring(rc, "RG", "R");
            r -= rc;
            if (r == 0) {rring.pop_back(); cout << rring << '\n';  continue; }
        }
        if (yc) {
            yring = genring(yc, "YV", "Y");
            y -= yc;
            if (y == 0) { yring.pop_back(); cout << yring << '\n';  continue; }
        }
        if (bc) {
            bring = genring(bc, "BO", "B");
            b -= bc;
            if (b == 0) { bring.pop_back(); cout << bring << '\n';  continue; }
        }
        if (r > y+b || y > r+b || b > y+r) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        string sol = solve_small(r, b, y);
        for (int i = 0; i < sol.size(); ++i) {
            if (sol[i] == 'R' && rc) {
                cout << rring; rc = 0;
            }
            else if (sol[i] == 'Y' && yc) {
                cout << yring; yc = 0;
            }
            else if (sol[i] == 'B' && bc) {
                cout << bring; bc = 0;
            }
            else cout << sol[i];
        }
        cout << '\n';
    }
}