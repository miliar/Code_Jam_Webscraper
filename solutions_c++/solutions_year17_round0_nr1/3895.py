/*************************************************************************
	> File Name: main.cpp
	> Author: cxlove
	> Mail: cxlove321@gmail.com
	> Created Time: 六  4/ 8 20:01:09 2017
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
char str[10005];
int k;

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, cas = 0;
    scanf("%d" , &t);
    while (t --) {
        scanf("%s %d", str, &k);
        int n = strlen(str);
        int ans = 0;
        for(int i = 0 ; i <= n - k ; i ++) {
            if(str[i] == '-') {
                for(int j = 0 ; j < k ; j ++) {
                    str[i + j] = str[i + j] == '+' ? '-' : '+';
                }
                ans ++;
            }
        }
        int flag = 1;
        for(int i = 0 ; i < n ; i ++) {
            if(str[i] == '-') {
                flag = 0;
            }
        }
        printf("Case #%d: ", ++ cas);
        if(!flag) {
            puts("IMPOSSIBLE");
        }
        else {
            printf("%d\n", ans);
        }
    }

    return 0;
}

