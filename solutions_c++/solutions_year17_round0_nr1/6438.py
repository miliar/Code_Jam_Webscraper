#include <bits/stdc++.h>

using namespace std;
char s[1010];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ca = 1;
    scanf("%d", &t);
    while(t--) {
        int k;
        scanf("%s%d", s, &k);
        printf("Case #%d: ", ca++);
        int n = strlen(s);
        bool flag = true;
        int ret = 0;
        for(int i = 0; i < n; i++)  {
            if(s[i] == '-') {
                if(i + k - 1 < n) {
                    for(int j = i; j < i + k; j++) {
                        if(s[j] == '-') s[j] = '+';
                        else s[j] = '-';
                    }
                    ret++;
                } else {
                    flag = false;
                }
            }
        }
        if(flag)
        printf("%d\n", ret);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
