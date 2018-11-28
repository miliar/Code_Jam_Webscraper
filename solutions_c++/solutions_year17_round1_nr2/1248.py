#include <bits/stdc++.h>
using namespace std;

const double EP = 1e-6;
typedef pair <int, int> pii;
const int MAX = 52;
int test, n, m, r[MAX], q;
pii range[MAX][MAX];
bool fr[MAX][MAX];

int get_low(int x, int y){
    int mn = (int)(1.0 * x / 1.1 + 1.0 - EP);
    if (mn == 0)
        return 0;
    return (mn - 1) / y + 1;
}

int get_high(int x, int y){
    int mx = (int)(1.0 * (x + EP) / 0.9);
    return mx / y;
}

pii intersect(pii x, pii y){
    if (x.first > y.first)
        swap(x, y);
    if (x.second < y.first)
        return pii(-1, -1);
    return pii(y.first, min(x.second, y.second));
}

bool ok(int col){
    pii cur = range[1][col], tmp;
    for (int i = 2; i <= n; ++i){
        bool check = false;
        for (int j = 1; j <= m; ++j)
        if (!fr[i][j]){
            tmp = intersect(cur, range[i][j]);
            if (tmp.first == -1)
                continue;

            check = true;
            cur = tmp;
            break;
        }
        if (!check)
            return false;
    }
    return true;
}

int get(){
    for (int col = 1; col <= m; ++col)
    if (!fr[1][col] && ok(col))
        return col;
    return 0;
}

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int tt = 1; tt <= test; ++tt){
        scanf("%d %d", &n, &m);
        for (int i = 1; i <= n; ++i)
            scanf("%d", r + i);
        memset(fr, false, sizeof(fr));
        for (int i = 1; i <= n; ++i){
            for (int j = 1; j <= m; ++j){
                scanf("%d", &q);
                range[i][j] = pii(get_low(q, r[i]), get_high(q, r[i]));
            }
            sort(range[i] + 1, range[i] + 1 + m, [](const pii& x, const pii& y)->bool{
                if (x.second != y.second)
                    return x.second < y.second;
                return x.first > y.first;
            });
            for (int j = 1; j <= m; ++j)
            if (range[i][j].first > range[i][j].second)
                fr[i][j] = true;
        }

        int col, res = 0;
        while ((col = get()) != 0){
            ++res;
            fr[1][col] = true;
            pii cur = range[1][col], tmp;
            for (int i = 2; i <= n; ++i){
                for (int j = 1; j <= m; ++j)
                if (!fr[i][j]){
                    tmp = intersect(cur, range[i][j]);
                    if (tmp.first == -1)
                        continue;

                    cur = tmp;
                    fr[i][j] = true;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", tt, res);
    }
    return 0;
}
