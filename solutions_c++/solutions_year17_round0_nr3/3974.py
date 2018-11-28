#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

const int maxL = 20 + 5;

int T, k, n;

multiset<int> S;

int main() {
    //freopen("3.in", "r", stdin);
    //freopen("3.txt", "w", stdout);
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; ++testCase) {
        scanf("%d%d", &n, &k);
        S.clear();
        S.insert(n);
        int now, le, re;
        for (int i = 1; i <= k; ++i) {
            multiset<int>::iterator it;
            it = S.end(); --it;
            now = *it;
            S.erase(S.lower_bound(now));
            re = now >> 1;
            le = now - 1 - re;
            S.insert(le);
            S.insert(re);
        }
        printf("Case #%d: %d %d\n", testCase, re, le);
    }
    return 0;
}
