#include <cstdio>
#include <queue>
using namespace std;

FILE *fout = fopen ("BS.out", "w");
FILE *fin  = fopen ("BS.in", "r");

void solve(long long n, long long k) {
    if (k == 1) {
        fprintf(fout, "%lld %lld\n", n/2, (n+1)/2 - 1);
        return;
    }
    solve(k%2 ? (n+1)/2 - 1 : n/2, k/2);
}

int main() {
    int T;
    long long n, k;
    fscanf(fin, "%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        fscanf(fin, "%lld %lld\n", &n, &k);
        fprintf(fout, "Case #%d: ", i);
        solve(n, k);
    }
    return 0;
}
