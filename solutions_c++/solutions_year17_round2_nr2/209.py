#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int ti = 1; ti <= testcase; ti++) {
        printf("Case #%d: ", ti);
        int s, r, o, y, g, b, v;
        // N, R, O, Y, G, B, and V.
        scanf("%d%d%d%d%d%d%d", &s, &r, &o, &y, &g, &b, &v);
        if (s == 1) {
            char w = 'Y';
            if (b > 0) w = 'B';
            if (r > 0) w = 'R';
            if (o > 0) w = 'O';
            if (g > 0) w = 'G';
            if (v > 0) w = 'V';
            printf("%c", w);
            printf("\n");
        } else
        if (y == v && y * 2 == s) {
            for (int i = 0; i < y; i++) {
                printf("YV");
            }
            printf("\n");
        } else if (o == b && o * 2 == s) {
            for (int i = 0; i < b; i++) {
                printf("OB");
            }
            printf("\n");
        } else if (r == g && r * 2 == s) {
            for (int i = 0; i < r; i++) {
                printf("RG");
            }
            printf("\n");
        } else if (v != 0 && y < v + 1 || o != 0 && b < o + 1 || g != 0 && r < g + 1) {
            printf("IMPOSSIBLE\n");
        } else {
            int a[3];
            char c[3];
            a[0] = y - v;
            a[1] = b - o;
            a[2] = r - g;
            if (a[0] > a[1] && a[0] > a[2]) {
                c[0] = 'Y';
                c[1] = 'B';
                c[2] = 'R';
            } else if (a[1] > a[2]) {
                s = a[0]; a[0] = a[1]; a[1] = s;
                c[0] = 'B';
                c[1] = 'Y';
                c[2] = 'R';
            } else {
                s = a[0]; a[0] = a[2]; a[2] = s;
                c[0] = 'R';
                c[1] = 'B';
                c[2] = 'Y';
            }
            if (a[0] <= a[1] + a[2]) {
                string ans = "";
                while (a[0] > 0) {
                    ans = ans + c[0];
                    a[0]--;
                    if (a[1] > 0) {
                        a[1]--;
                        ans += c[1];
                        if (a[2] + a[1] > a[0]) {
                            a[2]--;
                            ans += c[2];
                        }
                    } else {
                        ans += c[2];
                    }
                }
                string ans1 = "";
                string pattern = "";
                for (int i = 0; i < ans.size(); i++) {
                    int m = 0;
                    if (v > 0 && ans[i] == 'Y') {
                        m = v;
                        pattern = "YV";
                        v = 0;
                    }
                    if (g > 0 && ans[i] == 'R') {
                        m = g;
                        pattern = "RG";
                        g = 0;
                    }
                    if (o > 0 && ans[i] == 'B') {
                        m = o;
                        pattern = "BO";
                        o = 0;
                    }
                    for (int j = 0; j < m; j++) {
                        ans1 += pattern;
                    }
                    ans1 += ans[i];
                }

                printf("%s\n", ans1.c_str());
            } else {
                printf("IMPOSSIBLE\n");
            }
        }
    }
}