#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;

char s[110][110];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T, tot = 0;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++)
            scanf("%s", s[i]+1);
        
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (j > 1 && s[i][j] == '?' && s[i][j-1] != '?')
                    s[i][j] = s[i][j-1];
        
        for (int i = 1; i <= n; i++)
            for (int j = m; j >= 1; j--)
                if (j < m && s[i][j] == '?' && s[i][j+1] != '?')
                    s[i][j] = s[i][j+1];
        
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (i > 1 && s[i][j] == '?' && s[i-1][j] != '?')
                    s[i][j] = s[i-1][j];
        
        for (int i = n; i >= 1; i--)
            for (int j = 1; j <= m; j++)
                if (i < n && s[i][j] == '?' && s[i+1][j] != '?')
                    s[i][j] = s[i+1][j];
        printf("Case #%d:\n", ++tot);
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) {
                printf("%c", s[i][j]);
                if (j == m) printf("\n");
            }
    }
    return 0;
}