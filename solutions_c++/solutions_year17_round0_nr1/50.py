#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int Test, n, m;
char s[11111];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &Test);
    for (int Case = 1; Case <= Test; Case ++){
        scanf("%s%d", s, &m);
        n = strlen(s);
        bool flag = true;
        int ret = 0;
        for (int i = 0; i < n; i ++)
        if (s[i] == '-') {
            if (i + m > n) {
                flag = false;
                break;
            }
            ret ++;
            for (int j = 0; j < m; j ++) {
                if (s[i+j] == '+') {
                    s[i+j] = '-';
                } else {
                    s[i+j] = '+';
                }
            }
        }
        printf("Case #%d: ", Case);
        if (flag) {
            printf("%d\n", ret);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
