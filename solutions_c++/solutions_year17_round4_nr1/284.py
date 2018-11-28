/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/05/13
 *  Name:
 *      a.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int cas, n, p, a[200], cnt[10];
int work() {
    if (p == 2)
        return cnt[0] + ((cnt[1] + 1) >> 1);
    if (p == 3) {
        int ans = cnt[0];
        int mini = min(cnt[1], cnt[2]);
        ans += mini;
        ans += (max(cnt[1], cnt[2]) - mini + 2) / 3;
        return ans;
    }
    int ans = cnt[0];
    ans += cnt[2] >> 1;
    cnt[2] &= 1;
    int mini = min(cnt[1], cnt[3]);
    ans += mini;
    int rest = max(cnt[1], cnt[3]) - mini;
    if (cnt[2]) {
        ans++;
        if (rest >= 2) {
            rest -= 2;
            ans += (rest + 3) / 4;
        } 
    } else {
        ans += (rest + 3) / 4;
    }
    return ans;
}
int main() {
    cin >> cas;
    for (int t = 1; t <= cas; t++) {
        cin >> n >> p;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        memset(cnt, 0, sizeof cnt);
        for (int i = 0; i < n; i++)
            cnt[a[i] % p]++;
        printf("Case #%d: %d\n", t, work());
    }

    return 0;
}
