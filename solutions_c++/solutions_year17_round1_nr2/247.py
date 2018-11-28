#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define sz(x) (int)x.size()
#define mp(a,b) make_pair(a,b)
#define pb push_back
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;

const int N = 55;
const double eps = 1e-9;
int T, n, p;
int R[N];
int Q[N][N];
int ti[N * N * 10], tn;
int dcmp(double x) {
    if (fabs(x) < eps) return 0;
    return x < 0 ? -1 : 1;
}

int vis[N][N];
vi tmp[N];

int X;
bool cmp(int a, int b) {
    return Q[X][a] < Q[X][b];
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    int cas = 0;
    while (T--){
        scanf("%d%d", &n, &p);
        for (int i = 1; i <= n; i++) scanf("%d",&R[i]);
        tn = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= p; j++) {
                vis[i][j] = 0;
                scanf("%d", &Q[i][j]);
                int l = floor(Q[i][j] / 0.9); l /= R[i];
                int r = ceil(Q[i][j] / 1.1); r /= R[i];
                for (int f = -1; f <= 1; f++) ti[tn++] = l + f, ti[tn++] = r + f;
              //  printf("%d %d %d %d\n", i, j, l / R[i], r / R[i]);
            }
        }
        sort(ti, ti + tn);
        tn = unique(ti, ti + tn) - ti;
        int ans = 0;
        for (int i = 0; i < tn; i++) {
            if (ti[i] == 0) continue;
            int Min = inf;
            //printf("%d\n", ti[i]);
            for (int x = 1; x <= n; x++){
                tmp[x].clear();
                for (int y = 1; y <= p; y++) {
                    if (vis[x][y]) continue;
                    if (dcmp(0.9 * ti[i] * R[x] - Q[x][y]) <= 0 && dcmp(Q[x][y] - 1.1 * ti[i] * R[x]) <= 0)
                        tmp[x].pb(y);
                }
                X = x;
                sort(tmp[x].begin(), tmp[x].end(), cmp);
                Min = min(Min, sz(tmp[x]));
            }
            for (int x = 1; x <= n; x++){
                for (int j = 0; j < Min; j++)
                    vis[x][tmp[x][j]] = 1;
            }
            ans += Min;
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
