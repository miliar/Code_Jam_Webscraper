#include <bits/stdc++.h>

using namespace std;

char M[25][26];

int main (void) {
    int t;
    scanf ("%d", &t);
    for (int c = 1; c <= t; c++) {
        map<char, bool> used;
        printf ("Case #%d:\n", c);
        int n, m;
        scanf ("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf ("%s", M[i]);
        }
        char curr = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (curr == 0 && M[i][j] != '?' && !used[M[i][j]]) {
                    curr = M[i][j];
                    int left = j;
                    for (int k = j-1; k >= 0; k--) {
                        if (M[i][k] == '?') M[i][k] = curr, left = k;
                        else    break;
                    }
                    int right = j;
                    for (int k = j+1; k < m; k++) {
                        if (M[i][k] == '?') M[i][k] = curr, right = k;
                        else break;
                    }
                    for (int l = i+1; l < n; l++) {
                        bool ok = true;
                        for (int k = left; k <= right; k++) {
                            if (M[l][k] != '?') ok = false;
                        }
                        if (ok) {
                            for (int k = left; k <= right; k++) {
                                M[l][k] = curr;
                            }
                        } else  break;
                    }
                    for (int l = i-1; l >= 0; l--) {
                        bool ok = true;
                        for (int k = left; k <= right; k++) {
                            if (M[l][k] != '?') ok = false;
                        }
                        if (ok) {
                            for (int k = left; k <= right; k++) {
                                M[l][k] = curr;
                            }
                        } else  break;
                    }
                    curr = 0;
                    used[M[i][j]] = true;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            printf ("%s\n", M[i]);
        }
    }
}
