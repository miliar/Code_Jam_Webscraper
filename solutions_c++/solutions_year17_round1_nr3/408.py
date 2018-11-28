#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

const int flag = 0;

int LastOne(long long a, long long b) {
    if (a % b == 0) {
        return 0;
    }
    return 1;
}

bool CheckB(long long hk, long long ad, long long b, long long i) {
    return true;
}

bool CheckD(long long ak, long long d, long long j) {
    return true;
}

long long Work(long long hd, long long ad, long long hk, long long ak, long long b, long long d) {
    if (hd <= ak * 2) {
        if (hd < ak && ad >= hk) { return 1; }
        if (b == 0 && d == 0) { return -1; }
    }
    long long ans = (long long)1 << 50;
    long long ori = ans, maxb = 100, maxd = ((d == 0) ? 0 : (ak / d + 1));
    for (long long i = 0; i <= maxb; i++) {
        for (long long j = 0; j <= maxd; j++) {
            long long num = 0;
            long long thd = hd, tad = ad, thk = hk, tak = ak, ti = i, tj = j;
            while (num <= 10000) {
                num++;
                if (tj > 0) {
                    if (thd <= tak - d) {
                        thd = hd - tak;
                    } else {
                        tj--;
                        tak -= d;
                        if (tak < 0) { tak = 0; }
                        thd -= tak;
                    }
                    continue;
                }
                if (ti > 0) {
                    if (thd <= tak) {
                        thd = hd - tak;
                    } else {
                        ti--;
                        tad += b;
                        thd -= tak;
                    }
                    continue;
                }
                if (thd <= tak && thk > tad) {
                    thd = hd - tak;
                } else {
                    thd -= tak;
                    thk -= tad;
                    if (thk <= 0) { break; }
                    if (thd <= 0) { num = 1e9; break; }
                }
            }
            ans = min(ans, num);
        }
    }
    if (ans > 10000) { return -1; }
    return ans;
}

int main() {
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("c0.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int hd, ad, hk, ak, b, d;
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        long long ans = Work(hd, ad, hk, ak, b, d);
        printf("Case #%d: ", t);
        if (ans == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%lld\n", ans);
        }
    }
    return 0;
}
