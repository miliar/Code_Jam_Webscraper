#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

using namespace std;

int cache[5][5][101][101][101];

int solve(int p, int cmod, int a, int b, int c) {
    if (a == -1 || b == -1 || c == -1)
        return 0;
    if (a == 0 && b == 0 && c == 0)
        return 0;
    if (cache[p][cmod][a][b][c] != -1)
        return cache[p][cmod][a][b][c];
    int ans = 0;
    if (a > 0)
        ans = max(ans, solve(p, (cmod+1)%p, a-1, b, c));
    if (b > 0)
        ans = max(ans, solve(p, (cmod+2)%p, a, b-1, c));
    if (c > 0)
        ans = max(ans, solve(p, (cmod+3)%p, a, b, c-1));
        
    if (cmod == 0)
        ans+=1;
    cache[p][cmod][a][b][c]= ans;
    return ans;
}

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    int i,j,k,l,m;
    for (i = 2; i <= 4; i++)
        for (j = 0; j < 5; j++)
            for (k = 0; k <= 100; k++)
                for (l = 0; l <= 100; l++)
                    for (m = 0; m <= 100; m++)
                        cache[i][j][k][l][m] = -1;
    fprintf(stderr, "cmp\n");
    solve(2,0,100,0,0);
    fprintf(stderr, "cmp\n");
    solve(3,0,100,100,0);
    fprintf(stderr, "cmp\n");
    solve(4,0,100,100,100);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        int n, p;
        scanf("%d%d", &n, &p);
        
        int mods[4] = {0};
        int i;
        for (i = 0; i < n; i++) {
            int t;
            scanf("%d", &t);
            mods[t%p]++;
        }
        
        printf("%d\n", mods[0] + solve(p, 0, mods[1], mods[2], mods[3]));
        
        

    }
}
        