#include <bits/stdc++.h>

using namespace std;

const string IMPOSSIBLE = "IMPOSSIBLE";

string solve() {
    int n, r, ry, y, yb, b, rb;
    cin >> n >> r >> ry >> y >> yb >> b >> rb;

    r -= yb;
    y -= rb;
    b -= ry;

    if (r < 0 || y < 0 || b < 0) return IMPOSSIBLE;

    int *o, *p, *q;
    char O, P, Q;

    if (r >= y && y >= b) {
        o = &r, O = 'R';
        p = &y, P = 'Y';
        q = &b, Q = 'B';
    } else if (r >= b && b >= y) {
        o = &r, O = 'R';
        p = &b, P = 'B';
        q = &y, Q = 'Y';
    } else if (y >= r && r >= b) {
        o = &y, O = 'Y';
        p = &r, P = 'R';
        q = &b, Q = 'B';
    } else if (y >= b && b >= r) {
        o = &y, O = 'Y';
        p = &b, P = 'B';
        q = &r, Q = 'R';
    } else if (b >= r && r >= y) {
        o = &b, O = 'B';
        p = &r, P = 'R';
        q = &y, Q = 'Y';
    } else if (b >= y && y >= r) {
        o = &b, O = 'B';
        p = &y, P = 'Y';
        q = &r, Q = 'R';
    }

    vector<string> slots(*o);

    for (int i = 0; i < *o; i++) {
        if (*p) {
            slots[i] += P;
            --*p;
        } else if (*q) {
            slots[i] += Q;
            --*q;
        } else {
            return IMPOSSIBLE;
        }
    }

    for (int i = 0; i < *o; i++) {
        if (*p) {
            slots[i] += P;
            --*p;
        } else if (*q) {
            slots[i] += Q;
            --*q;
        } else {
            break;
        }
    }

    string result_a;
    for (int i = 0; i < *o; i++) {
        result_a += O;
        result_a += slots[i];
    }

    if (result_a == "") {
        string result_b;
        if (rb && ry == 0 && yb == 0) {
            for (int i = 0; i < rb; i++) {
                result_b += "VY";
            }
        } else if (ry && rb == 0 && yb == 0) {
            for (int i = 0; i < ry; i++) {
                result_b += "OB";
            }
        } else if (yb && rb == 0 && ry == 0) {
            for (int i = 0; i < yb; i++) {
                result_b += "GR";
            }
        } else {
            return IMPOSSIBLE;
        }

        return result_b;
    }

    string result_b;
    for (char c: result_a) {
        result_b += c;

        if (c == 'R' && yb) {
            for (int i = 0; i < yb; i++) {
                result_b += "GR";
            }
            yb = 0;
        }

        if (c == 'Y' && rb) {
            for (int i = 0; i < rb; i++) {
                result_b += "VY";
            }
            rb = 0;
        }

        if (c == 'B' && ry) {
            for (int i = 0; i < ry; i++) {
                result_b += "OB";
            }
            ry = 0;
        }
    }

    if (ry || yb || rb) {
        return IMPOSSIBLE;
    }

    return result_b;
}

int main() {
    int t;
    cin >> t;

    for (int c = 1; c <= t; c++) {
        cout << "Case #" << c << ": " << solve() << endl;
    }
}
