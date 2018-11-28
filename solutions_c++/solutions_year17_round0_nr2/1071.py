/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/04/08
 *  Name:
 *      b.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int cas, a[20], b[20], cnt;
long long n, ans;
bool dfs(const int &cur, const int &tot, const int &flag, const int &choose = 0) {
    if (cur == tot)
        return true;
    if (flag) {
        if ((b[cur] = a[cur]) >= choose && dfs(cur + 1, tot, flag, b[cur]))
            return true;
        if (a[cur] != 0 && (b[cur] = a[cur] - 1) >= choose && dfs(cur + 1, tot, 0, b[cur] = a[cur] - 1))
			return true;
    } else {
        return dfs(cur + 1, tot, 0, b[cur] = 9);
    }
    return false;
}
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        scanf("%lld", &n);
        for (cnt = 0; n; n /= 10, cnt++)
            a[cnt] = n % 10;
        reverse(a, a + cnt);
        dfs(0, cnt, 1);
        for (int i = 0; i < cnt; i++)
            n = n * 10 + b[i];
		printf("Case #%d: %lld\n", t, n);
    }

    return 0;
}
