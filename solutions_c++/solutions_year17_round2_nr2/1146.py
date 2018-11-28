//from iabrother/driver
//cf #348 div.2 DÃ‚ ¬“∏„Ã‚
#include <iostream>
#include <cstdio>
#include <cstdlib>
#define maxn 1000010
using namespace std;
pair <int, int> req[2*maxn];
int ans[maxn];
int main() {
    int n, q;
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= q; ++i) {
        int t;
        scanf("%d", &t);
        if (t == 1) {
            int w;
            scanf("%d", &w);
            w = (w + n + n) % n;
            req[i] = {t, w};
        } else {
            req[i] = {t, 0};
        }
    }
    int ind1 = 1, ind2 = 2, ind3 = 3;
    for (int i = 1; i <= q; ++i) {
        if (req[i].first == 2) {
            if (ind1 % 2 == 0) {
                --ind1;
            } else {
                ++ind1;
            }
            if (ind2 % 2 == 0) {
                --ind2;
            } else {
                ++ind2;
            }
            if (ind3 % 2 == 0) {
                --ind3;
            } else {
                ++ind3;
            }
        } else {
            ind1 += req[i].second;
            if (ind1 > n) {
                ind1 -= n;
            }
            ind2 += req[i].second;
            if (ind2 > n) {
                ind2 -= n;
            }
            ind3 += req[i].second;
            if (ind3 > n) {
                ind3 -= n;
            }
        }
    }
    if (n == 2) {
        if (ind1 == 1) {
            cout << "1 2";
        } else {
            cout << "2 1";
        }
        return 0;
    }
    ans[ind1] = 1;
    ans[ind2] = 2;
    ans[ind3] = 3;
    int last = ind3;
    int ind;
    for (int i = 4; i <= n; ++i) {
        if (i % 2 == 0) {
            ind = last + (ind2 - ind1);
            if (ind > n) {
                ind -= n;
            }
            if (ind <= 0) {
                ind += n;
            }
            ans[ind] = i;
            last = ind;
        } else {
            ind = last + (ind3 - ind2);
            if (ind > n) {
                ind -= n;
            }
            if (ind <= 0) {
                ind += n;
            }
            ans[ind] = i;
            last = ind;
        }
    }
    for (int i = 1; i <= n; ++i) {
        printf("%d ", ans[i]);
    }
    return 0;
}
