#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

char s[1010];

int solve(const int k) {
    const int n = strlen(s);
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '-') {
            if (i + k > n) {
                return -1;
            }
            for (int j = 0; j < k; ++j) {
                s[i + j] = (s[i + j] == '-' ? '+' : '-');
            }
            ++res;
        }
    }
    return res;
}

int main(int argc, char const *argv[]) {
    FILE *fin = fopen("problemA.in", "r");
    FILE *fout = fopen("problemA.txt", "w");

    int t = 0, k = 0;
    fscanf(fin, "%d", &t);

    for (int i = 0; i < t; ++i) {
        fscanf(fin, "%s %d", s, &k);
        int res = solve(k);
        if (res == -1) {
            fprintf(fout, "Case #%d: IMPOSSIBLE\n", i + 1);
        } else {
            fprintf(fout, "Case #%d: %d\n", i + 1, res);    
        }
    }

    return 0;
}