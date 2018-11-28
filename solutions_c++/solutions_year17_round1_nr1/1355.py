#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int M = 30;
char grid[M][M];
int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                cout << "Case #" << c << ":\n";
                int n, m;
                cin >> n >> m;
                for(int i = 1; i <= n; i++) {
                        for(int j = 1; j <= m; j++)
                                cin >> grid[i][j];
                }
                bool emp[M];
                memset(emp, 0, sizeof emp);
                for(int i = 1; i <= n; i++) {
                        for(int j = 1; j <= m; j++) {
                                if(grid[i][j] == '?')continue;
                                int id = j + 1;
                                char cur = grid[i][j];
                                while(id <= m && grid[i][id] == '?') {
                                        grid[i][id++] = cur;
                                }
                                id = j - 1;
                                while(id > 0 && grid[i][id] == '?') {
                                        grid[i][id--] = cur;
                                }
                                emp[i] = 1;
                        }
                }
                int it = 50;
                while(it--) {
                        for(int i = 1; i <= n; i++) {
                                if(!emp[i] && emp[i + 1]) {
                                        for(int j = 1; j <= m; j++) {
                                                grid[i][j] = grid[i + 1][j];
                                        }
                                        emp[i] = 1;
                                }
                                else if(!emp[i] && emp[i - 1]) {
                                        for(int j = 1; j <= m; j++) {
                                                grid[i][j] = grid[i - 1][j];
                                        }
                                        emp[i] = 1;
                                }
                        }
                }
                for(int i = 1; i <= n; i++) {
                        for(int j = 1; j <= m; j++) {
                                cout << grid[i][j];
                        }
                        cout << "\n";
                }
        }
        return 0;
}

