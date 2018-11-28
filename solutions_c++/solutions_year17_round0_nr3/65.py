#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, tI, i, j;
    long long N, K, r;
    pair<long long, long long> A[2], B[2];
    scanf("%d", &T);
    for (tI = 0; tI < T; tI++) {
        scanf("%lld %lld", &N, &K);
        A[0] = make_pair(N, 1);
        A[1] = make_pair(N - 1, 0);
        while (K > 0) {
            K -= A[0].second;
            if (K < 1) {r = A[0].first; break;}
            K -= A[1].second;
            if (K < 1) {r = A[1].first; break;}
            B[0].first = A[0].first / 2;
            B[1].first = A[0].first / 2 - 1;
            if (A[0].first % 2) {
                B[0].second = A[0].second * 2 + A[1].second;
                B[1].second = A[1].second;
            } else {
                B[0].second = A[0].second;
                B[1].second = A[0].second + A[1].second * 2;
            }
            A[0] = B[0];
            A[1] = B[1];
        }
        printf("Case #%d: %lld %lld\n", tI + 1, r / 2, (r - 1) / 2);
    }
    return 0;
}
