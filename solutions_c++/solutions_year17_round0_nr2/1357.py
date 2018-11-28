#include <cstdio>
#include <cstring>
using namespace std;

FILE *fout = fopen ("TN.out", "w");
FILE *fin  = fopen ("TN.in", "r");
char s[20];

void solve() {
    int m, x;
    fscanf(fin, "%s\n", s);
    for (m = 1; s[m] != '\0'; ++m) {
        if (s[m] < s[m-1])
            break;
    }
    if (s[m] == '\0') {
        fprintf(fout, "%s\n", s);
        return;
    }
    for (x = m-2; x >= 0; --x) {
        if (s[m-1] != s[x])
            break;
    }
    --s[x+1];
    for (int i = x+2; s[i] != '\0'; ++i)
        s[i] = '9';
    fprintf(fout, "%s\n", s + !(s[0]-'0'));
}

int main() {
    int T;
    fscanf(fin, "%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        fprintf(fout, "Case #%d: ", i);
        solve();
    }
    return 0;
}
