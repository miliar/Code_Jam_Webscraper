#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;


char next_char(int r1, int b1, int y1, char r, char b, char y, char last) {
    if (r1 >= b1 && r1 >= y1) {
        if (last != r) {
            return r;
        } else {
            if (b1 >= y1) {
                if (last != b) {
                    return b;
                } else {
                    return y;
                }
            } else {
                if (last != y) {
                    return y;
                } else {
                    return b;
                }
            }
        }
    } else {
        return next_char(b1, y1, r1, b, y, r, last);
    }
}

void go(int rr1, int rr2, char r, char g) {

    if (rr2 > 0) {
        cout << r << g << r;
        rr2--;
    } else {
        cout << r;
        for (int j = 0; j < rr1; ++j) {
            cout << g << r;
        }
    }

}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    for (int z = 0; z < t; ++z) {
        int n;
        cin >> n;
        int r, o, y, g, b, v;
        cin >> r >> o >> y >> g >> b >> v;

        cout << "Case #" << z + 1 << ": ";

        int y1 = y - v;
        int r1 = r - g;
        int b1 = b - o;

        if (y1 < 0 || r1 < 0 || b1 < 0) {
            cout << "IMPOSSIBLE\n";
        } else {

            if (r1 > y1 + b1) {
                r1 = y1 + b1;
            }

            if (y1 > r1 + b1) {
                y1 = r1 + b1;
            }

            if (b1 > r1 + y1) {
                b1 = r1 + y1;
            }

            int sy1 = y1;
            int sr1 = r1;
            int sb1 = b1;

            char last = '-';
            string s;
            char f = '-';
            int m = r1 + b1 + y1;
            for (int i = 0; i < m; ++i) {
                if (f == 'R' && r1 != 0) r1++;
                if (f == 'B' && b1 != 0) b1++;
                if (f == 'Y' && y1 != 0) y1++;

                last = next_char(r1, b1, y1, 'R', 'B', 'Y', last);

                if (f == 'R' && r1 != 0) r1--;
                if (f == 'B' && b1 != 0) b1--;
                if (f == 'Y' && y1 != 0) y1--;

                if (last == 'R') r1--;
                if (last == 'B') b1--;
                if (last == 'Y') y1--;
                s += last;
                if (i == 0) f = last;
            }

            y1 = sy1;
            r1 = sr1;
            b1 = sb1;

            int yy2 = y - y1 - v;
            int yy1 = v - yy2;

            int rr2 = r - r1 - g;
            int rr1 = g - rr2;

            int bb2 = b - b1 - o;
            int bb1 = o - bb2;

            if (yy1 < 0 || yy2 < 0 || rr1 < 0 || rr2 < 0 || bb1 < 0 || bb2 < 0) {
                cout << "IMPOSSIBLE\n";
            } else {

                for (int i = 0; i < m; ++i) {
                    if (s[i] == 'R') {
                        go(rr1, rr2, 'R', 'G');
                    }
                    if (s[i] == 'Y') {
                        go(yy1, yy2, 'Y', 'V');
                    }
                    if (s[i] == 'B') {
                        go(bb1, bb2, 'B', 'O');
                    }
                }

                if (m == 0) {
                    if (r == 0 && b == 0) {
                        for (int i = 0; i < y; ++i) {
                            cout << "YV";
                        }
                    } else if (y == 0 && b == 0) {
                        for (int i = 0; i < r; ++i) {
                            cout << "RG";
                        }
                    } else if (r == 0 && y == 0) {
                        for (int i = 0; i < b; ++i) {
                            cout << "BO";
                        }
                    } else {
                        cout << "IMPOSSIBLE";
                    }

                }

                cout << "\n";

            }

        }

    }



    return 0;
}
