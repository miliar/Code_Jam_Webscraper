#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
    int t, k;
    char str[1024];
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%s %d", str, &k);
        int ans = 0;
        for (int i = 0; str[i+k-1]; i++) {
            if (str[i] == '+') continue;
            ans++;
            for (int j = 0; j < k; j++)
                str[i+j] = str[i+j] == '+' ? '-' : '+';
        }
        int can = 1;
        for (int i = 0; str[i]; i++)
            can &= str[i] == '+';
        printf("Case #%d: ", tt);
        if (can) printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}