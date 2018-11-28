#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

char s[1010];

int main () {
//        freopen ("in.txt", "r", stdin);
//        freopen ("out.txt", "w", stdout);
        int T, k;
        scanf ("%d", &T);
        for (int cas = 1; cas <= T; cas++) {
                scanf ("%s%d", s, &k);
                int len = strlen (s);
                int flag = 0, ans = 0;
                for (int i = 0; i < len; i++) {
                        if (s[i] == '-') {
                                if (i + k - 1 >= len) {
                                        flag = 1;
                                        break;
                                }
                                for (int j = i, l = 1; l <= k; j++, l++) {
                                        if (s[j] == '-')        s[j] = '+';
                                        else    s[j] = '-';
                                }
                                ans++;
                        }
                }
                if (flag) {
                        printf ("Case #%d: IMPOSSIBLE\n", cas);
                } else {
                        printf ("Case #%d: %d\n", cas, ans);
                }
        }
        return 0;
}
