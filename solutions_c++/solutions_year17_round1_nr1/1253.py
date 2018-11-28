#include <bits/stdc++.h>
using namespace std;

const int MAX = 30;
int test, n, m;
char s[MAX][MAX], last[MAX], kt;

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int tt = 1; tt <= test; ++tt){
        scanf("%d %d", &n, &m);
        for (int i = 1; i <= n; ++i){
            scanf("%s", s[i] + 1);
            last[i] = '?';
            for (int j = 1; j <= m; ++j)
            if (s[i][j] != '?')
                last[i] = s[i][j];
        }

        for (int i = 1; i <= n; ++i){
            kt = last[i];
            for (int j = m; j >= 1; --j){
                if (s[i][j] != '?')
                    kt = s[i][j];
                s[i][j] = kt;
            }
        }

        for (int j = 1; j <= m; ++j){
            last[j] = '?';
            for (int i = n; i >= 1; --i)
            if (s[i][j] != '?')
                last[j] = s[i][j];

            kt = last[j];
            for (int i = 1; i <= n; ++i){
                if (s[i][j] != '?')
                    kt = s[i][j];
                s[i][j] = kt;
            }
        }

        printf("Case #%d:\n", tt);
        for (int i = 1; i <= n; ++i)
            printf("%s\n", s[i] + 1);
    }
    return 0;
}
