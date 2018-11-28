#include <cstdio>
#include <cstring>

int n;
char in[32];
char out[32];

bool go(int p, int lt) {
    out[p] = '\0';
    // printf("GO %d %d %s\n", p, lt, out);
    if (p >= n) {
        return true;
    }
    char po = 0;
    if (p == 0) {
        po = '0' - 1;
    } else {
        po = out[p - 1];
    }
    char ci = in[p];
    if (lt) {
        ci = '9' + 1;
    }
    for (out[p] = '9'; out[p] >= '1'; --out[p]) {
        if (out[p] <= ci && out[p] >= po) {
            if (go(p + 1, out[p] < ci)) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%s", in);
        n = strlen(in);
        printf("Case #%d: ", t);
        if (go(0, false)) {
            out[n] = '\0';
            printf("%s\n", out);
        } else {
            for (int i = 0; i + 1 < n; ++i) {
                printf("9");
            }
            printf("\n");
        }
    }
    return 0;
}
