
#include <cstdio>
#include <string>
#include <iostream>

int n, k, ans, p[1005];
std::string s;

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        std::cin >> s;
        for (int j = 0; j < s.size(); j++) p[j] = s[j] == '+';
        ans = 0;
        scanf("%d", &k);
        for (int j = 0; j < s.size() - k + 1; j++) {
            if (!p[j]) {
                for (int x = 0; x < k; x++) {
                    p[j + x] ^= 1;
                }
                ans++;
            }
        }
        const int l = s.size();
        int flag = 0;
        for (int j = 0; j < k && !flag; j++) {
            if (!p[l - j - 1]) flag = 1;
        }
        if (flag) printf("Case #%d: IMPOSSIBLE\n", i);
        else printf("Case #%d: %d\n", i, ans);
    }
}
