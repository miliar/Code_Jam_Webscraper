#include <bits/stdc++.h>
#define int long long
#define double long double
#define eps 1e-9

using namespace std;

void solve(int x) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    cout << "Case #" << x << ':' << ' ';
    int last = -1;
    string s = "";
    int c = -1;
    for (int i = 0; i < N; i++) {
        if (c == 0 && R == 1) {
            R = 0;
        }
        if (c == 1 && Y == 1) {
            Y = 0;
        }
        if (c == 2 && B == 1) {
            B = 0;
        }
        if (last == -1) {
            if (R > Y && R > B) {
                s += 'R';
                c = last = 0;
            } else {
                if (Y > B) {
                    s += 'Y';
                    c = last = 1;
                } else {
                    s += 'B';
                    c = last = 2;
                }
            }
            continue;
        }
        if (last == 0) {
            if (Y > B) {
                s += 'Y';
                Y--;
                last = 1;
            } else {
                s += 'B';
                B--;
                last = 2;
            }
            continue;
        }
        if (last == 1) {
            if (R > B) {
                s += 'R';
                R--;
                last = 0;
            } else {
                s += 'B';
                B--;
                last = 2;
            }
            continue;
        }
         if (last == 2) {
            if (R > Y) {
                s += 'R';
                R--;
                last = 0;
            } else {
                s += 'Y';
                Y--;
                last = 1;
            }
            continue;
        }
    }
    //cout << s;
    if (R == 0 && Y == 0 && B == 0) {
        cout << s;
    } else {
        cout << "IMPOSSIBLE";
    }
    cout << '\n';
}


signed main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
