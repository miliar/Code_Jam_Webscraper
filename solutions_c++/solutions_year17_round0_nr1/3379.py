#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int casenum, K, len;
char s[1010];
int cake[1010];

void debug() {
    printf("d  ");
    for(int i = 0;i < len;i ++) {
        printf("%d", cake[i]);
    }
    printf("\n");
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        scanf("%s%d", s, &K);
        len = strlen(s);
        for(int i = 0;i < len;i ++) {
            if(s[i] == '+') cake[i] = 1;
            else cake[i] = 0;
        }
        int ans = 0;
        for(int i = 0;i <= len - K; i++) {
            if(cake[i] == 0) {
                ans ++;
                for(int j = i; j < i + K;j ++) {
                    cake[j] = 1 - cake[j];
                }
                // debug();
            }
        }
        bool flag = true;
        for(int i = 0;i < len;i ++) {
            if(cake[i] == 0) {
                flag = false;
                break;
            }
        }
        printf("Case #%d: ", cs);
        if(flag) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
