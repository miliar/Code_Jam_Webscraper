#include <bits/stdc++.h>
using namespace std;

#define ifthen(x, y, z) (x ? y: z)
#define mp make_pair
#define mt make_tuple

const int INF = 1e9 + 1;
const double pi = acos(-1);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i+1 << ": ";
        int n;
        cin >> n;
        int r, o, y, g, b, v;
        cin >> r >> o >> y >> g >> b >> v;
        if ((r+b < y) || (r+y < b) || (y+b < r)) {
            cout << "IMPOSSIBLE";
        } else {
            string s = "";
            char start = 0;
            while (r+b+y > 0) {
                int mx = max({r, b, y});
                // cerr << r << ' ' << b << ' ' << y << endl;
                int r_val(0), b_val(0), y_val(0);
                if (mx == r) {
                    r_val = 1;
                    if (start == 'R')
                        r_val++;
                }
                if (mx == b) {
                    b_val = 1;
                    if (start == 'B')
                        b_val++;
                }
                if (mx == y) {
                    y_val = 1;
                    if (start == 'Y')
                        y_val++;
                }
                // cerr << r_val << ' ' << b_val << ' ' << y_val << ' ' << start << endl;
                int mx_val = max({r_val, b_val, y_val});
                if (mx_val == r_val) {
                    s = s + "R";
                    if (start == 0)
                        start = 'R';
                    r--;
                    if (b+y > 0) {
                        if (b == y) {
                            if (start == 'Y') {
                                s = s + "Y";
                                y--;
                            }
                            else {
                                s = s + "B";
                                b--;
                            }
                        } else {
                            int s_mx = max(b, y);
                            if (s_mx == b) {
                                s = s + "B";
                                b--;
                            } else {
                                s = s + "Y";
                                y--;
                            
                            }
                        }
                    }
                } else if (mx_val == b_val) {
                    s = s + "B";
                    if (start == 0)
                        start = 'B';
                    b--;
                    if (r+y > 0) {
                        if (r == y) {
                            if (start == 'Y') {
                                s = s + "Y";
                                y--;
                            }
                            else {
                                s = s + "R";
                                r--;
                            }
                        } else {
                            int s_mx = max(r, y);
                            if (s_mx == r) {
                                s = s + "R";
                                r--;
                            } else {
                                s = s + "Y";
                                y--;
                            }
                        }
                    }
                } else if (mx_val == y_val) {
                    s = s + "Y";
                    if (start == 0)
                        start = 'Y';
                    y--; 
                    if (r+b > 0) {
                        if (r == b) {
                            if (start == 'B') {
                                s = s + "B";
                                b--;
                            }
                            else {
                                s = s + "R";
                                r--;
                            }
                        } else {
                            int s_mx = max(r, b);
                            if (s_mx == r) {
                                s = s + "R";
                                r--;
                            } else {
                                s = s + "B";
                                b--;
                            }
                        }
                    }
                }
            }
            cout << s;
        }
        cout << '\n';
    }
    return 0;
}
