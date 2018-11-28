#include <bits/stdc++.h>
#define FI(i, a, b) for (int i = (a); i <= (b); i++)
#define FD(i, a, b) for (int i = (a); i >= (b); i--)
using namespace std;
using LL = long long;

map<LL, LL> mp;
set<LL> se;

void work(int testCase) {
    LL n, k;
    scanf("%lld %lld", &n, &k);
    mp.clear();
    se.clear();
    LL cnt = 0;
    se.insert(n);
    mp[n] = 1;
    while (!se.empty()) {
        LL range = *se.rbegin();
        se.erase(range);
        LL num = mp[range];
        LL left = (range - 1) / 2;
        LL right = range - 1 - left;
        cnt += num;
        if (cnt >= k) {
            printf("Case #%d: %lld %lld\n", testCase, right, left);
            return;
        }
        mp[left] += num;
        mp[right] += num;
        se.insert(left);
        se.insert(right);
    }
}
int main() {
    int T;
    scanf("%d", &T);
    FI(i, 1, T)
    work(i);
}