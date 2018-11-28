/***************************************************************************
 * 
 * Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 /**
 * @file A.cpp
 * @author fangzhaofa(fangzhaofa@gmail.com)
 * @date 2017/04/08 11:07:57
 * @brief 
 *  
 **/

#include <stdio.h>
#include <string.h>

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    char str[1024];
    int K;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%s%d", str, &K);
        int len = strlen(str);
        int ans = 0;
        bool ok = true;
        for (int i = 0; i < len; ++i) {
            if (str[i] == '+') {
                continue;
            }
            if (i + K > len) {
                ok = false;
                break;
            }
            ++ans;
            for (int j = i; j < i + K; ++j) {
                str[j] = (str[j] == '-' ? '+' : '-');
            }
        }
        printf("Case #%d: ", cas);
        if (!ok) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}

/* vim: set ts=4 sw=4 sts=4 tw=100 */
