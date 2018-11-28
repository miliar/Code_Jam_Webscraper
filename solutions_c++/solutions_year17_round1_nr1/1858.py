#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

const int MAXN = 25;

char grid[MAXN + 5][MAXN + 5];
int n,m;

bool safe(int j, int i1, int i2) {
    for (int i = i1; i <= i2; i++)
        if (grid[i][j] != '\?') return false;
    return true;
}

int main() {
    freopen("cake.in","r",stdin);
    freopen("cake.out","w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
        scanf("%d%d",&n,&m);
        vector<pair<int,int>> mines;
        for (c=0;c<n;c++) {
            scanf("%s",grid[c]);
            for (c2=0;c2<m;c2++) {
                if (grid[c][c2] != '\?') {
                    mines.push_back({c,c2});
                }
            }
        }
        for (pair<int,int> cell : mines) {
            int i1 = cell.first, i2 = cell.first;
            int j1 = cell.second, j2 = cell.second;
            for (i1--; i1 >= 0 && grid[i1][j1] == '\?'; i1--); i1++;
            for (i2++; i2 < n && grid[i2][j1] == '\?'; i2++); i2--;
            for (int i = i1; i <= i2; i++)
                for (int j = j1; j <= j2; j++)
                    grid[i][j] = grid[cell.first][cell.second];
        }
        for (pair<int,int> cell : mines) {
            int i1 = cell.first, i2 = cell.first;
            int j1 = cell.second, j2 = cell.second;
            for (i1--; i1 >= 0 && grid[i1][j1] == grid[cell.first][cell.second]; i1--); i1++;
            for (i2++; i2 < n && grid[i2][j1] == grid[cell.first][cell.second]; i2++); i2--;
            for (j1--; j1 >= 0 && safe(j1, i1, i2); j1--); j1++;
            for (j2++; j2 < m && safe(j2, i1, i2); j2++); j2--;
            for (int i = i1; i <= i2; i++)
                for (int j = j1; j <= j2; j++)
                    grid[i][j] = grid[cell.first][cell.second];
        }
        printf("Case #%d:\n",test);
        for (c=0;c<n;c++)
            printf("%s\n",grid[c]);
    }
    
    return 0;
}
