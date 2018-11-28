 /**
 * @file B.cpp
 * @author fangzhaofa(fangzhaofa@gmail.com)
 * @date 2017/04/08 11:38:16
 * @brief 
 *  
 **/

#include <stdio.h>
#include <string.h>

char num[30];

void solve(int cas) {
    int len = strlen(num);
    for (int i = len - 2; i >= 0; --i) {
        if (num[i] <= num[i + 1]) {
            continue;
        }
        --num[i];
        for (int j = i + 1; j < len; ++j) {
            num[j] = '9';
        }
    }
    printf("Case #%d: %s\n", cas, (num[0] == '0' ? num + 1 : num));
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%s", num);
        solve(cas);
    }
    return 0;
}

/* vim: set ts=4 sw=4 sts=4 tw=100 */
