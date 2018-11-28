#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 1e3 + 5;

char s[maxn];

int main(int argc, char const *argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T, kase = 1; cin>>T;
    while (T --) {
        scanf("%s", s);
        long len = strlen(s);
        int k; cin>>k;
        int ans = 0;
        for (int i = 0; i <= len - k; i ++) {
            if (s[i] == '+') continue;
            ans ++;
            for (int j = i; j < i + k; j ++) {
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
        bool flag = true;
        for (int i = 0; i < len; i ++)
            if (s[i] == '-') {
                flag = false;
                break;
            }
        if (flag) printf("Case #%d: %d\n", kase ++, ans);
        else printf("Case #%d: IMPOSSIBLE\n", kase ++);
    }
    return 0;
}