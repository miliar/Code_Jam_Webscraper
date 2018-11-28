#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int a[100], f[100][100];
        int n, p;
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &f[i][j]);
            }
            sort(f[i], f[i] + p);
        }
        int ans = 0;
        pair<int, int> g[100][100];
        int b[3000];
        int num = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                g[i][j].first = (f[i][j] - f[i][j] / 11) / a[i];
                if ((f[i][j] - f[i][j] / 11) % a[i] != 0) {
                    g[i][j].first++;
                }
                g[i][j].second = (f[i][j] + f[i][j] / 9) / a[i];
                b[num++] = g[i][j].first;
            }
        }
        sort(b, b + num);
        int h[100];
        for (int i = 0; i < n; i++) { h[i] = 0; }
        for (int i = 0; i < num; i++) {
            bool valid = true;
            for (int j = 0; j < n; j++) {
                while (h[j] < p && (g[j][h[j]].second < b[i] || g[j][h[j]].first > g[j][h[j]].second)) { h[j]++; }
                if (h[j] >= p) {
                    valid = false;
                    break;
                }
            }
            if (!valid) {
                break;
            }
            bool check = true;
            for (int j = 0; j < n; j++)
            if (g[j][h[j]].first > b[i]) {
                check = false;
                break;
            }
            if (check) {
                ans++;
                for (int j = 0; j < n; j++) {
                    h[j]++;
                }
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
