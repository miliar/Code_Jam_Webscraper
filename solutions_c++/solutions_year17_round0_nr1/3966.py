#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

const int maxn = 1000 + 5;
char str[maxn];
int k;
void flip(int s) {
    for (int i = s; i < s + k; i++) {
        if (str[i] == '-') str[i] = '+';
        else str[i] = '-';
    }
}
int main() {
    int T; scanf("%d", &T);
    for (int Cas = 1; Cas <= T; Cas++) {
        scanf("%s", str);
        scanf("%d", &k);
        int len = strlen(str);
        int cnt = 0;
        for (int i = 0; i <= len - k; i++) {
            if (str[i] == '-') {
                flip(i);
                cnt++;
            }
        }
        bool suc = true;
        for (int i = 0; i < len; i++) {
            if (str[i] == '-') suc = false;
        }
        printf("Case #%d: ", Cas);
        if (suc) {
            printf("%d\n", cnt);
        } else puts("IMPOSSIBLE");
    }
    return 0;
}
