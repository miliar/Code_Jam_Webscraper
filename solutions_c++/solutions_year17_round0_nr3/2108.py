#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

// First, let's do simulation!
/*
void simulation(long long N, long long K) {
    vector<int> A(N + 2, 0);
    A[0] = A[N + 1] = 1;

    int mn, mx, p;
    for (int i = 0; i < K; i ++) {
        mn = -1;
        mx = -1;
        p = 0;

        for (int j = 1; j <= N; j ++) {
            if (A[j] == 1) {
                continue;
            }

            int L, R;
            for (int k = j - 1; k >= 0; k --) {
                if (A[k] == 1) {
                    L = j - k - 1;
                    break;
                }
            }
            for (int k = j + 1; k <= N + 1; k ++) {
                if (A[k] == 1) {
                    R = k - j - 1;
                    break;
                }
            }

            if (mn < min(L, R)) {
                mn = min(L, R);
                mx = max(L, R);
                p = j;
            } else if (mn == min(L, R) && mx < max(L, R)) {
                mx = max(L, R);
                p = j;
            }
        }
        A[p] = 1;
    }

    long long x = 1;
    while (x <= K) {
        x *= 2;
    }
    long long rmx = ((N - K) + (x / 2)) / x;
    long long rmn = (N - K) / x;

    if (rmx != mx || rmn != mn) {
        printf(" WRONG WRONG WRONG \n");
    }

    printf("(%3lld, %3lld) : %d %d\n", N, K, mx, mn);
}

*/

int main() {
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test ++) {
        long long N, K;
        scanf("%lld %lld", &N, &K);

        long long x = 1;
        while (x <= K) {
            x *= 2;
        }
        long long rmx = ((N - K) + (x / 2)) / x;
        long long rmn = (N - K) / x;
        
        printf("Case #%d: %lld %lld\n", test, rmx, rmn);
    }
    
    return 0;
}
