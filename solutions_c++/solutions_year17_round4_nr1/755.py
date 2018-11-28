#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
using namespace std;

int A[4];

int main() {
    int T;
    scanf("%d", &T);
    for (int Cas = 1; Cas <= T; Cas++) {
        memset(A, 0, sizeof(A));
        int n, p; scanf("%d%d", &n, &p);
        for (int i = 1; i <= n; i++) {
            int x; scanf("%d", &x);
            A[x % p]++;
        }
        int res = 0;
        if(p == 2) {
            res = A[0] + (A[1] + 1) / 2;
        }  else if(p == 3) {
            res = A[0] + min(A[1], A[2]) + 
                (max(A[1], A[2]) - min(A[1], A[2]) + 2) / 3;
        }
        printf("Case #%d: %d\n", Cas, res);
    }
}
