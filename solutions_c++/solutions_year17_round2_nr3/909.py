#include "math.h"
#include <algorithm>
#include <set>
#include <complex>
#include <stack>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
#define rep(i, n) for (lli i = 0; i < (n); i++)
#define rrep(i, n) for (lli i = (n)-1; i >= 0; i--)
using namespace std;
typedef long long int lli;

int n, q;
double e[10005], s[10005];

double d[200][200];

using ll = __int128;
int main()
{
    int t;
    cin >> t;
    rep(I, t)
    {
        cin >> n >> q;
        rep(i, n)
        {
            cin >> e[i] >> s[i];
        }
        rep(i, n)
        {
            rep(j, n)
            {
                cin >> d[i][j];
                if (d[i][j] == -1)
                    d[i][j] = 1e20;
            }
        }
        rep(i, n) d[i][i] = 0;
        double time[200][200] = {};
        rep(i, 200) rep(j, 200) time[i][j] = 1e20;
        rep(i, 200) time[i][i] = 0;
        rep(i, n)
        {
            queue<pair<double, int>> que;
            que.push(make_pair(0, i));
            while (!que.empty()) {
                auto cur = que.front().second;
                auto dis = que.front().first;
                que.pop();
                //cout << cur << endl;
                rep(j, n)
                {
                    if (j != i)
                        if (dis + d[cur][j] <= e[i] && time[i][j] > (d[cur][j] + dis) / s[i]) {
                            time[i][j] = min(time[i][j], (dis + d[cur][j]) / s[i]);
                            que.push(make_pair(dis + d[cur][j], j));
                        }
                }
            }
        }
        rep(k, n) rep(i, n) rep(j, n)
        {
            if (time[i][j] > time[i][k] + time[k][j])
                time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
        }
        /*rep(i, n) rep(j, n)
        {
            cout << i << " " << j << " " << time[i][j] << endl;
        }
        */
        vector<double> ans(q);
        int u, v;
        rep(i, q)
        {
            cin >> u >> v;
            u--, v--;
            ans[i] = time[u][v];
        }
        printf("Case #%d: ", I + 1);
        rep(i, q)
            printf("%.10f ", ans[i]);
        cout << endl;
    }
}
