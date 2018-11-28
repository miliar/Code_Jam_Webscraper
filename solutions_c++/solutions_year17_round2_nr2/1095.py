#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define xx first
#define yy second

#ifndef _WIN32
#define gc getchar_unlocked
#else
#define gc getchar
#endif // _WIN32
void ri(int &a) {
    a = 0;
    register int x = gc();
    bool neg = false;
    while (x < '0' || x > '9') {
        if (x == '-') neg = true;
        x = gc();
    }
    while (x >= '0' && x <= '9') {
        a = (a << 3) + (a << 1) + (x-'0');
        x = gc();
    }
    if (neg) a = -a;
}

const int maxn = 100100, INF = (1 << 30)-1;
int t;

int main() {
    freopen("output.out", "w", stdout);
    ri(t);
    for (int casenum = 1, x, y, z, xy, yz, xz; casenum <= t; casenum++) {
        printf("Case #%d: ", casenum);
        string ansa = "", ansb = "", ansc = "", ansxyz = "";
        ri(x), ri(x), ri(xy), ri(y), ri(yz), ri(z), ri(xz);
        for (int i = 0; i < xy; i++) ansa += "BO";
        for (int i = 0; i < yz; i++) ansb += "RG";
        for (int i = 0; i < xz; i++) ansc += "YV";
        if (z < xy || x < yz || y < xz) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        z -= xy;
        x -= yz;
        y -= xz;
        if (xy > 0 && yz > 0 || xy > 0 && xz > 0) {
            z--;
            ansa += "B";
        }
        if (yz > 0 && xz > 0 || yz > 0 && xy > 0) {
            x--;
            ansb += "R";
        }
        if (xz > 0 && xy > 0 || xz > 0 && yz > 0) {
            y--;
            ansc += "Y";
        }
        if (x < 0 || y < 0 || z < 0) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        string ans = ansa+ansb+ansc;
        if (x > 0 || y > 0 || z > 0) {
            int sz = ans.size();
            char prv, nd;
            if (sz != 0) prv = ans[sz-1], nd = ans[0];
            int prev;
            bool rip = false;
            if (prv == 'O') {
                rip |= z == 0;
                z--;
                ansxyz += "B";
                prev = 3;
            } else if (prv == 'G') {
                rip |= x == 0;
                x--;
                ansxyz += "R";
                prev = 1;
            } else if (prv == 'V') {
                rip |= y == 0;
                y--;
                ansxyz += "Y";
                prev = 2;
            } else if (prv == 'R') prev = 1;
            else if (prv == 'Y') prev = 2;
            else prev = 3;
            if (sz == 0) {
                if (x >= y && x >= z) {
                    x--;
                    ansxyz += "R";
                    nd = 'R';
                    prev = 1;
                } else if (y >= x && y >= z) {
                    y--;
                    ansxyz += "Y";
                    nd = 'Y';
                    prev = 2;
                } else {
                    z--;
                    ansxyz += "B";
                    nd = 'B';
                    prev = 3;
                }
            }
            if (rip) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            while (x > 0 || y > 0 || z > 0) {
                if (prev == 1) {
                    if (y > z || (y == z && nd == 'Y')) {
                        y--;
                        ansxyz += "Y";
                        prev = 2;
                    } else {
                        z--;
                        ansxyz += "B";
                        prev = 3;
                    }
                } else if (prev == 2) {
                    if (x > z || (x == z && nd == 'R')) {
                        x--;
                        ansxyz += "R";
                        prev = 1;
                    } else {
                        z--;
                        ansxyz += "B";
                        prev = 3;
                    }
                } else {
                    if (x > y || (x == y && nd == 'R')) {
                        x--;
                        ansxyz += "R";
                        prev = 1;
                    } else {
                        y--;
                        ansxyz += "Y";
                        prev = 2;
                    }
                }
            }
            if (x < 0 || y < 0 || z < 0 || (nd == 'R' && prev == 1) || (nd == 'Y' && prev == 2) || (nd == 'B' && prev == 3)) {
                printf("IMPOSSIBLE\n");
                continue;
            }

        }
        printf("%s%s\n", ans.c_str(), ansxyz.c_str());
    }
    return 0;
}
