#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 60
typedef long long LL;

int n, m;
bool vis[MAXN][MAXN];
char Map[MAXN][MAXN];
bool mark[MAXN][MAXN];
bool ccc[MAXN][MAXN];

bool Solve(int i, int j)
{
    int k; bool flag1 = true, flag2 = true;
    for(k = j + 1; flag1 && k <= m; ++k){
        if(Map[i][k] == '|' || Map[i][k] == '-'){
            flag1 = false;
            break;
        }
        if(Map[i][k] == '#') break;
        ccc[i][k] = true;
    }
    for(k = j - 1; flag1 && k; --k){
        if(Map[i][k] == '|' || Map[i][k] == '-'){
            flag1 = false;
            break;
        }
        if(Map[i][k] == '#') break;
        ccc[i][k] = true;
    }

    for(k = i + 1; flag2 && k <= n; ++k){
        if(Map[k][j] == '|' || Map[k][j] == '-'){
            flag2 = false;
            break;
        }
        if(Map[k][j] == '#') break;
        ccc[k][j] = true;
    }
    for(k = i - 1; flag2 && k; --k){
        if(Map[k][j] == '|' || Map[k][j] == '-'){
            flag2 = false;
            break;
        }
        if(Map[k][j] == '#') break;
        ccc[k][j] = true;
    }

    if(!flag1 && !flag2) return false;
    if(flag1 && flag2) return true;
    vis[i][j] = true;
    if(flag1){
        Map[i][j] = '-';
        for(k = j + 1; flag1 && k <= m; ++k){
            vis[i][k] = true;
            if(Map[i][k] == '#') break;
        }
        for(k = j - 1; flag1 && k; --k){
            vis[i][k] = true;
            if(Map[i][k] == '#') break;
        }
    }
    else{
        Map[i][j] = '|';
        for(k = i + 1; flag2 && k <= n; ++k){
            vis[k][j] = true;
            if(Map[k][j] == '#') break;
        }
        for(k = i - 1; flag2 && k; --k){
            vis[k][j] = true;
            if(Map[k][j] == '#') break;
        }
    }
    return true;
}

bool Check(int i, int j)
{
    if(i > n){
        int x, y;
        for(x = 1; x <= n; ++x){
            for(y = 1; y <= m; ++y)
                if(Map[x][y] == '.' && !vis[x][y] && !mark[x][y])
                    break;
            if(y <= m) break;
        }
        if(x <= n) return false;
        return true;
    }
    if((Map[i][j] == '|' || Map[i][j] == '-') && !vis[i][j]){
        int k;
        Map[i][j] = '-';
        for(k = j + 1; k <= m; ++k){
            mark[i][k] = true;
            if(Map[i][k] == '#') break;
        }
        for(k = j - 1; k; --k){
            mark[i][k] = true;
            if(Map[i][k] == '#') break;
        }
        if(Check(i + (j == m ? 1 : 0), (j == m ? 1 : (j + 1))))
            return true;
        for(k = j + 1; k <= m; ++k){
            mark[i][k] = false;
            if(Map[i][k] == '#') break;
        }
        for(k = j - 1; k; --k){
            mark[i][k] = false;
            if(Map[i][k] == '#') break;
        }

        Map[i][j] = '|';
        for(k = i + 1; k <= n; ++k){
            mark[k][j] = true;
            if(Map[k][j] == '#') break;
        }
        for(k = i - 1; k; --k){
            mark[k][j] = true;
            if(Map[k][j] == '#') break;
        }
        if(Check(i + (j == m ? 1 : 0), (j == m ? 1 : (j + 1))))
            return true;
        for(k = i + 1; k <= n; ++k){
            mark[k][j] = false;
            if(Map[k][j] == '#') break;
        }
        for(k = i - 1; k; --k){
            mark[k][j] = false;
            if(Map[k][j] == '#') break;
        }
        return false;
    }
    else{
        return Check(i + (j == m ? 1 : 0), (j == m ? 1 : (j + 1)));
    }
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int i, j, k, T; bool flag;
    for(scanf("%d", &T), k = 1; k <= T; ++k){
        memset(vis, 0, sizeof(vis));
        memset(mark, 0, sizeof(mark));
        memset(ccc, 0, sizeof(ccc));
        flag = true;
        scanf("%d %d", &n, &m);
        for(i = 1; i <= n; ++i)
            for(j = 1; j <= m; ++j)
                scanf(" %c", &Map[i][j]);
        for(i = 1; i <= n; ++i)
            for(j = 1; j <= m; ++j)
                if(Map[i][j] == '|' || Map[i][j] == '-')
                    flag &= Solve(i, j);
        for(i = 1; i <= n; ++i)
            for(j = 1; j <= m; ++j)
                if(Map[i][j] == '.' && !ccc[i][j])
                    flag = false;
        if(!flag) printf("Case #%d: IMPOSSIBLE\n", k);
        else{
            if(Check(1, 1)){
                printf("Case #%d: POSSIBLE\n", k);
                for(i = 1; i <= n; ++i){
                    for(j = 1; j <= m; ++j)
                        printf("%c", Map[i][j]);
                    printf("\n");
                }
            }
            else printf("Case #%d: IMPOSSIBLE\n", k);
        }
    }
}
