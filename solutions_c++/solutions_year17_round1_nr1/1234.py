#include <bits/stdc++.h>
#define LL long long int

using namespace std;

const int INF = 0x7FFFFFFF;

void
Filework(void){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
}

char g[105][105];
char dp[105][105];
char row[105];
char col[105];
int flag;

int
main(){

	Filework();

	int T, t;
	int i, j, k, p;
	int m, n;
	char ch;

	scanf("%d", &T);
	for(t = 1; t <= T; t ++){
        printf("Case #%d:\n", t);
        scanf("%d%d", &n, &m);
        scanf("%c", &ch);
        for(i = 1; i <= n; i ++){
            row[i] = '?';
            for(j = 1; j <= m; j ++){
                scanf("%c", &g[i][j]);
            }
            scanf("%c", &ch);
        }
        for(i = 1; i <= n; i ++){
            for(j = 1; j <= m; j ++){
                if(g[i][j] == '?'){
                    flag = 0;
                    for(k = j - 1; k >= 1; k --){
                        if(g[i][k] != '?'){
                            g[i][j] = g[i][k];
                            flag = 1;
                            break;
                        }
                    }
                    for(k = j + 1; k <= m && (flag == 0); k ++){
                        if(g[i][k] != '?'){
                            g[i][j] = g[i][k];
                            flag = 1;
                            break;
                        }
                    }
                }
            }
        }
        for(i = 1; i <= n; i ++){
            for(j = 1; j <= m; j ++){
                if(g[i][j] == '?'){
                    flag = 0;
                    for(k = i - 1; k >= 1; k --){
                        if(g[k][j] != '?'){
                            flag = 1;
                            break;
                        }
                    }
                    for(p = 1; p <= m; p ++){
                        g[i][p] = g[k][p];
                    }
                    for(k = i + 1; k <= n && (flag == 0); k ++){
                        if(g[k][j] != '?'){
                            flag = -1;
                            break;
                        }
                    }
                    if(flag == -1){
                        for(p = 1; p <= m; p ++){
                            g[i][p] = g[k][p];
                        }
                    }
                }
            }
        }
        for(i = 1; i <= n; i ++){
            for(j = 1; j <= m; j ++){
                printf("%c", g[i][j]);
            }
            printf("\n");
        }
	}


return 0;
}
