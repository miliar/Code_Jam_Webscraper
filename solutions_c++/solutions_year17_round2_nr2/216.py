#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back

const int N = 6;
const string IMPOSSIBLE = "IMPOSSIBLE";
int a[N];
bool possible;
const int R = 0;
const int O = 1;
const int Y = 2;
const int G = 3;
const int B = 4;
const int V = 5;

int mask[] = {0b1, 0b11, 0b10, 0b110, 0b100, 0b101};
char c[] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int give(int pos) {
    a[pos]--;
    return c[pos];
}

string get(int f, int s) {
    string res = "";
    if (!possible) {
        return res;
    }
    if (a[s] != 0) {
        res += give(f);
        while (a[s]) {
            res += give(s);
            res += give(f);
        }
        a[f]++;
    }

    return res;
}

string collect() {
    if (!possible) {
        return "";
    }
    int n = a[R] + a[B] + a[Y];
    pair<int, char> c[] = {{a[R], 'R'}, {a[B], 'B'}, {a[Y], 'Y'}};
    sort(c, c + 3, greater<pair<int, char>>());
    string s(n, '1');
    if (max({a[R], a[B], a[Y]}) > (n + 1) / 2) {
        possible = false;
    } else {
        for (int i = 0; i < 2 * c[0].fi; i += 2) {
            s[i] = c[0].se;
        }
        for (int i = 2 * c[0].fi; i < n; i += 2) {
            s[i] = c[1].se;
            c[1].fi--;
        }
        for (int i = 1; i < n; i += 2) {
            if (c[1].fi) {
                s[i] = c[1].se;
                c[1].fi--;
            } else {
                s[i] = c[2].se;
                c[2].fi--;
            }
        }
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] == s[(i + 1) % n] || s[i] == s[(i + n - 1) % n]) {
                possible = false;
                return "";
            }
        }
    }
    return s;
}

bool check(int f, int s, int n) {
    if (a[s] == 0) {
        return false;
    }
    if (a[s] > a[f]) {
        possible = false;
        return false;
    }
    if (a[s] == a[f]) {
        if (a[s] + a[f] == n) {
            while (a[s]) {
                printf("%c%c", give(s), give(f));
            }
            printf("\n");
            return true;
        } else {
            possible = false;
        }
    }
    return false;
}

bool check1(char c, char d, string &subst) {
    if (c == d && !subst.empty()) {
        printf("%s", subst.c_str());
        subst = "";
        return true;
    }
    return false;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt) {
        possible = true;
        printf("Case #%d: ", tt);
        int n;
        scanf("%d", &n);
//        cout << "\n";
        static int bbb[N];
        for (int i = 0; i < N; ++i) {
            scanf("%d", a + i);
//            cout << c[i] << ' ' << a[i] << "\n";
        }
        if (check(R, G, n) || check(Y, V, n) || check(B, O, n)) {
            continue;
        }

        string RS = get(R, G);
        string YS = get(Y, V);
        string BS = get(B, O);
        string collected = collect();
//        cout << RS << ' ' << YS << ' ' << BS << "\n"

        if (!possible) {
            printf("%s\n", IMPOSSIBLE.c_str());
        } else {
            for (auto x : collected) {
                if (!check1(x, 'R', RS) &&
                    !check1(x, 'Y', YS) &&
                    !check1(x, 'B', BS)) {
                    printf("%c", x);
                }
            }
            printf("\n");
        }
    }
}
