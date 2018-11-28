#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int cnt[10];
int n, p;
int ans;

void Try(int x, int y) {
    int cur = min(cnt[x] / 2, cnt[y]);
    ans += cur;
    cnt[x] -= cur * 2;
    cnt[y] -= cur;
}

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &n, &p);
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            cnt[x % p]++;
        }
        ans = cnt[0];
        cnt[0] = 0;
        for (int i = 1; i <= p / 2; i++) {
            int j = p - i;
            int cur = (i == j ? cnt[i] / 2 : min(cnt[i], cnt[j]));
            ans += cur;
            cnt[i] -= cur;
            cnt[j] -= cur;
        }
        if (p == 4) {
            Try(1, 2);
            Try(3, 2);
        }
        for (int i = 1; i < p ; i++) {
            int cur = cnt[i] / p;
            ans += cur;
            cnt[i] -= cur * p;
        }
        if (accumulate(cnt, cnt + p, 0) > 0) ans++;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
/*
10
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
10 4
2 2 2 2 1 1 1 1 1 1
10 4
2 2 2 2 1 3 1 3 1 3
4 3
2 2 2 2
4 4
2 3 3 3

*/
