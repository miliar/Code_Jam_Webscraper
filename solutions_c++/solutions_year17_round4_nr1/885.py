#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;
typedef long double LD;

int T, cas = 1;
int N, P, G, c[4];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        int ans = 0;
        memset(c, 0, sizeof(c));
        scanf("%d %d", &N, &P);
        for (int i = 0; i < N; i++) {
            scanf("%d", &G);
            c[G % P] += 1;
        }
        ans += c[0];
        if (P == 2) {
            ans += ((c[1] + 1) / 2);
        }
        else if (P == 3) {
            int inc = min(c[1], c[2]);
            ans += inc;
            c[1] -= inc;
            c[2] -= inc;
            if (c[1] > 0) {
                ans += ((c[1] + 2) / 3);
            }
            else if (c[2] > 0) {
                ans += ((c[2] + 2) / 3);
            }
        }
        else if (P == 4) {
            int inc = min(c[1], c[3]);
            ans += inc;
            c[1] -= inc;
            c[3] -= inc;
            ans += (c[2] / 2);
            c[2] &= 1;
            if (c[2] == 0) {
                if (c[1] > 0) {
                    ans += ((c[1] + 3) / 4);
                }
                else if (c[3] > 0) {
                    ans += ((c[3] + 3) / 4);
                }
            }
            else {
                if (c[1] > 0) {
                    if (c[1] >= 2) {
                        ans++;
                        c[1] -= 2;
                        c[2]--;
                    }
                    ans += ((c[1] + 3) / 4);
                    c[1] %= 4;
                    if (c[1] == 0 && c[2] > 0) ans++;
                }
                else if (c[3] > 0) {
                    if (c[3] >= 2) {
                        ans++;
                        c[3] -= 2;
                        c[2]--;
                    }
                    ans += ((c[3] + 3) / 4);
                    c[3] %= 4;
                    if (c[3] == 0 && c[2] > 0) ans++;
                }
                else {
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
        cas++;
    }
    return 0;
}