#include <bits/stdc++.h>
using namespace std;

long long A[50], B[50][50], r[50];

pair<long long, long long> getl(long long i) {
    return make_pair(i * 9 / 10 + ((i * 9) % 10 > 0), i * 11 / 10);
}

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    long long T, tI, N, P, t, i, j, k;
    bool e;
    scanf("%lld", &T);
    for (tI = 0; tI < T; tI++) {
        t = 0;
        e = 1;
        scanf("%lld %lld", &N, &P);
        for (i = 0; i < N; i++) scanf("%lld", &A[i]), r[i] = 0;
        for (i = 0; i < N; i++) {
            for (j = 0; j < P; j++) scanf("%lld", &B[i][j]);
            sort(B[i], B[i] + P);
        }
        for (i = 1; i < 1000001 && e; i++) {
            for (j = 0; j < N && e; j++) {
                while (r[j] < P && B[j][r[j]] < getl(A[j] * i).first) r[j]++;
                if (r[j] > P - 1) {e = 0; break;}
                if (B[j][r[j]] > getl(A[j] * i).second) break;
            }
            if (j > N - 1) {
                for (j = 0; j < N; j++) r[j]++;
                i--;
                t++;
            }
        }
        printf("Case #%lld: %lld\n", tI + 1, t);
    }
    return 0;
}
