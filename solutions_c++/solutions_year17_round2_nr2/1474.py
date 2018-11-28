//
// Created by jeraz on 4/22/17.
//
#include <iostream>

using namespace std;

string makeString (int n, char a, int ac, char b, int bc, char c, int cc) {
    string out = "";
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            if (ac != 0) {
                out.append(string(1, a));
                ac--;
            } else {
                if (out[i-1] == a) {
                    if (bc > cc) {
                        out.append(string(1,b));
                        bc--;
                    } else {
                        out.append(string(1,c));
                        cc--;
                    }
                } else if (out[i-1] == b) {
                    out.append(string(1,c));
                    cc--;
                } else {
                    out.append(string(1,b));
                    bc--;
                }
            }
        } else {
            if (out[i-1] == a) {
                if (bc > cc) {
                    out.append(string(1,b));
                    bc--;
                } else {
                    out.append(string(1,c));
                    cc--;
                }
            } else if (out[i-1] == b) {
                out.append(string(1,c));
                cc--;
            } else {
                out.append(string(1,b));
                bc--;
            }
        }
    }
    return out;
}

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {

        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;

        if (r > b && r > y) {
            if (r > y + b) {
                cout  << fixed << "Case #" << i << ": IMPOSSIBLE" << endl;
                continue;
            }
            cout  << fixed << "Case #" << i << ": " << makeString(n,'R', r, 'B', b, 'Y', y) << endl;
        } else if (b > r && b > y) {
            if (b > r + y) {
                cout  << fixed << "Case #" << i << ": IMPOSSIBLE" << endl;
                continue;
            }
            cout  << fixed << "Case #" << i << ": " << makeString(n,'B', b, 'R', r, 'Y', y) << endl;
        } else {
            if (y > b + r) {
                cout  << fixed << "Case #" << i << ": IMPOSSIBLE" << endl;
                continue;
            }
            cout  << fixed << "Case #" << i << ": " << makeString(n,'Y', y, 'B', b, 'R', r) << endl;
        }
    }
}