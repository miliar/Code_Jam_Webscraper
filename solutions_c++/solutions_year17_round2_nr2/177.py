/*
 * (c) fushar (Ashar Fuadi)
*/

#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

const string IMPOSSIBRU = "IMPOSSIBLE";

int T;
int N, R, O, Y, G, B, V;

string combine(int& a, char ca, int& b, char cb) {
    if (b > a) {
        return IMPOSSIBRU;
    }

    string res;
    while (a) {
        res += ca;
        a--;
        if (b) {
            res += cb;
            b--;
        } else {
            break;
        }
    }
    return res;
}

string solve() {
    if (!R && G == 1) {
        return N > 1 ? "IMPOSSIBRU" : "G";
    }
    if (!Y && V == 1) {
        return N > 1 ? "IMPOSSIBRU" : "V";
    }
    if (!B && O == 1) {
        return N > 1 ? "IMPOSSIBRU" : "O";
    }

    string sR = combine(R, 'R', G, 'G');
    string sY = combine(Y, 'Y', V, 'V');
    string sB = combine(B, 'B', O, 'O');

    if (sR == IMPOSSIBRU || sY == IMPOSSIBRU || sB == IMPOSSIBRU) {
        return IMPOSSIBRU;
    }
    if (!sR.empty() && sR.size() % 2 == 0) {
        return sY.empty() && sB.empty() ? sR : IMPOSSIBRU;
    }
    if (!sY.empty() && sY.size() % 2 == 0) {
        return sR.empty() && sB.empty() ? sY : IMPOSSIBRU;
    }
    if (!sB.empty() && sB.size() % 2 == 0) {
        return sR.empty() && sY.empty() ? sB : IMPOSSIBRU;
    }

    assert(!O && !G && !V);

    priority_queue<pair<int, char>> rem;
    if (R) rem.push(make_pair(R, 'R'));
    if (Y) rem.push(make_pair(Y, 'Y'));
    if (B) rem.push(make_pair(B, 'B'));

    while (rem.size() >= 2) {
        pair<int, char> u = rem.top(); rem.pop();
        pair<int, char> v = rem.top(); rem.pop();
        if (u.second > v.second) {
            swap(u, v);
        }

        if (u.second == 'R' && v.second == 'Y') {
            sY += "RY";
            R--, Y--;
        } else if (u.second == 'B' && v.second == 'R') {
            sR += "BR";
            B--, R--;
        } else {
            sY += "BY";
            B--, Y--;
        }

        u.first--;
        v.first--;

        if (u.first) {
            rem.push(u);
        }
        if (v.first) {
            rem.push(v);
        }
    }

    if (R > 1 || Y > 1 || B > 1) {
        return IMPOSSIBRU;
    }

    if (R && (sB.empty() || sY.empty())) {
        return IMPOSSIBRU;
    }
    if (Y && (sR.empty() || sB.empty())) {
        return IMPOSSIBRU;
    }
    if (B && (sR.empty() || sY.empty())) {
        return IMPOSSIBRU;
    }

    return sR + (B ? "B" : "") + sY + (R ? "R" : "") + sB + (Y ? "Y" : "");
}

bool valid[256][256];

bool ok(string s) {
    int n = s.size();
    REP(i, n) {
        char a = s[i], b = s[(i+1)%n];
        if (!valid[a][b]) {
            return false;
        }
    }
    return true;
}

int main() {
    valid['R']['Y'] = valid['Y']['R'] = true;
    valid['R']['B'] = valid['B']['R'] = true;
    valid['B']['Y'] = valid['Y']['B'] = true;

    valid['R']['G'] = valid['G']['R'] = true;
    valid['Y']['V'] = valid['V']['Y'] = true;
    valid['B']['O'] = valid['O']['B'] = true;

    cin >> T;
    REP(tc, T) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        string res = solve();
        if (!ok(res)) {
            res = IMPOSSIBRU;
        }
        cout << "Case #" << (tc+1) << ": " << res << endl;
    }
}
