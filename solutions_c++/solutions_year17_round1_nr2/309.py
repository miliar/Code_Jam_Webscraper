#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<vector>

#include<ctime>
using namespace std;

const int maxn = 11000;
int a[maxn];
int b[maxn][maxn];
struct node {
    int l, r;
    node(){}
    node(int l, int r) :l(l), r(r){}
};
node w[maxn][maxn];
vector<pair<int,int> > g[maxn];
bool vis[1100000];

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T, cas = 0; 
    scanf("%d", &T);
    while (T--) { 
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) scanf("%d", &b[i][j]);
        
        memset(vis,0,sizeof(vis));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                double t2 = b[i][j] / (0.9 * a[i]);
                double t1 = b[i][j] / (1.1 * a[i]);
                int l = (int)ceil(t1);
                int r = (int)floor(t2);
                if (l > r) l = -1;
                vis[l] = true;
                vis[r] = true;
                w[i][j] = node(l, r);
            }
        }
        //for (int i = 1; i <= n; i++) sort(w[i].begin(), w[i].end(), cmp);
            
        int ans = 0;
        for (int x = 1; x <= 1000000; x++) {
            if (!vis[x]) continue;
            int sum = 0;
            for (int i = 1; i <= n; i++) {
                g[i].clear();
                for (int j = 1; j <= m; ++j) {
                    node tmp = w[i][j];
                    if (tmp.l == -1) continue;
                    if (tmp.l <= x && tmp.r >= x) {
                        if (g[i].size() == 0) sum++;
                        g[i].push_back(make_pair(tmp.r, j));
                    }
                }
            }
            if (sum == n) {
                for (int i = 1; i <= n; i++) {
                    sort(g[i].begin(), g[i].end());
                    pair<int,int> tmp = g[i][0];
                    w[i][tmp.second].l = -1;
                }
                x--;
                ans++;
            }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
