#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 5555;

int T, cas;

LL n; char ch[30];

bool Dfs(int cur, int tot) {
    if (cur == tot - 1) return true;
    if (ch[cur] >= ch[cur + 1]) {
        if (ch[cur] == ch[cur + 1]) {
            if (Dfs(cur + 1, tot)) {
                return true;
            }
        }
        if (ch[cur] != '0') {
            if (cur && ch[cur] - 1 < ch[cur - 1]) {
                return false;
            }
            ch[cur] --;
            for (int i = cur + 1; i < tot; i ++)
                ch[i] = '9';
            return true;
        } else {
            return false;
        }
    } else {
        return Dfs(cur + 1, tot);
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> T;
    while (T --) {
        scanf("%lld", &n);
        printf("Case #%d: ", ++ cas);
        int len = 0;
        memset(ch, 0, sizeof(ch));
        for (; n; n /= 10) {
            ch[len ++] = n % 10 + '0';
        }
        reverse(ch, ch + len);
//        cout << ch << endl;
        if (!Dfs(0, len)) {
            for (int i = 0; i < len - 1; i ++) {
                printf("9");
            }
            puts("");
        } else {
            if (ch[0] == '0')
                printf("%s\n", ch + 1);
            else
                printf("%s\n", ch);
        }
    }
}
