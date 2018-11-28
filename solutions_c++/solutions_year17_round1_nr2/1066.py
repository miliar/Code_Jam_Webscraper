#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

const int maxn = 100;
int G[maxn][maxn], R[maxn];

int T, n, p, Case = 1;
vector<int> c;

int main()
{
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &n, &p);
        for(int i = 0; i < n; i++)
            scanf("%d", &R[i]);
        for(int i = 0; i < n; i++)
            for(int j = 0; j < p; j++)
                scanf("%d", &G[i][j]);
        vector<int> c;
        for(int i = 0; i < p; i++)
            c.push_back(i);
        int ans = 0;
        if(1) {
            do {
                int cnt = 0, k1, k2;
                for(int i = 0; i < c.size(); i++) {
                    int x = G[0][c[i]], y = G[1][i];
                    k1 = x * 10 / R[0] / 9; 
                    k2 = ceil(x * 10 / R[0] / 11);
                    bool ok = false;
                    for(int k=k2; k <= k1 && !ok; k++) {
                        if(9 * k * R[0] <= 10 * x && 10 * x <= 11 * k * R[0])
                        if(n == 1 || 9 * k * R[1] <= 10 * y && 10 * y <= 11 * k * R[1])
                            ok = true;
                    }
                    if(ok) cnt++;
                }
                ans = max(ans, cnt);
            } while(next_permutation(c.begin(), c.end()));
        }
        printf("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}