#include <cstdio>
#include <cstring>
using namespace std;

FILE *fout = fopen ("A.out", "w");
FILE *fin  = fopen ("A.in", "r");

char s, ans[30][30];
int r, c;
void solve() {
    memset(ans, '\0', sizeof(ans));
    fscanf(fin, "%d %d\n", &r, &c);
    int x = 0, y = 0;
    int ub = 1, db = r, lb = 1, rb = c;
    for (int i = 1; i <= r; ++i) {
        for (int j = 1; j <= c; ++j) {
            fscanf(fin, "%c", &s);
            if (s != '?') {
                if (x != i) {
                    lb = 1;
                    ub = x + 1;
                }
                else {
                    lb = y + 1;
                }
                x = i;
                y = j;
                for (int e = ub; e <= db; ++e)
                for (int f = lb; f <= rb; ++f)
                    ans[e][f] = s;
            }
        }
        fscanf(fin, "\n");
    }
    for (int i = 1; i <= r; ++i)
        fprintf(fout, "%s\n", ans[i]+1);
}

int main() {
    int T;
    long long n, k;
    fscanf(fin, "%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        fprintf(fout, "Case #%d:\n", i);
        solve();
    }
    return 0;
}
