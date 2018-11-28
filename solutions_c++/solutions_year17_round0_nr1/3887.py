#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxL = 1000 + 5;

int T, l, k, ans;
int type[maxL];

char s[maxL];

int Get(int x) {
    int ret = 0;
    for (int i = x; i; i -= i & -i)
        ret += type[i];
    return ret % 2;
}

void Change(int x) {
    for (int i = x; i <= l; i += i & -i)
        type[i] += 1;
}

int main() {
    //freopen("1.in", "r", stdin);
    //freopen("1.txt", "w", stdout);
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; ++testCase) {
        scanf("%s", s);
        l = strlen(s);
        memset(type, 0, sizeof(type));
        for (int i = 0; i < l; ++i) {
            if (s[i] == '-') {
                Change(i + 1);
                Change(i + 2);
            }
        }
        scanf("%d", &k);
        ans = 0;
        for (int i = 1; i <= l; ++i) {
            if (Get(i) == 0) continue;
            if (l - i + 1 < k) {
                ans = -1;
                break;
            }
            ++ans;
            Change(i);
            if (i + k <= l) Change(i + k);
        }
        printf("Case #%d: ", testCase);
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
