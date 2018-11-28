#include <algorithm>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

int n, q;
vector<pair<int, int> > vs;
vector<vector<int> > bd;
double tbl[101][102];

double rec(int cur, int got, int rest)
{
    if (cur == n - 1) {
        return 0;
    }

    double& ret = tbl[cur][got];
    if (ret >= 0)
        return ret;

    ret = 1e100;
    int d = bd[cur][cur + 1];

    bool any = false;
    if (vs[cur].first >= d) {
        ret = min(ret, rec(cur + 1, cur, vs[cur].first - d) + (double)d / vs[cur].second);
        any = true;
    }
    if (rest >= d) {
        ret = min(ret, rec(cur + 1, got, rest - d) + (double)d / vs[got].second);
        any = true;
    }

    if (!any) {
        cout << cur << ", " << vs[cur].first << ", " << rest << ", " << d << ", " << bd[cur][cur + 1] << endl;
        assert(any);
    }

    return ret;
}

void solve()
{
    cin >> n >> q;

    vs.resize(n);
    for (auto& v : vs)
        cin >> v.first >> v.second;

    bd = vector<vector<int> >(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> bd[i][j];
        }
    }

    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++) {
    //         cerr << bd[i][j] << " ";
    //     }
    //     cerr << endl;
    // }

    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;

        for (int j = 0; j < 101; j++) {
            for (int k = 0; k < 102; k++) {
                tbl[j][k] = -1;
            }
        }

        double ans = rec(0, 0, 0);
        cout << " " << setiosflags(ios::fixed) << setprecision(12) << ans;
    }
    cout << endl;
}

void solve2()
{
    cin >> n >> q;

    vs.resize(n);
    for (auto& v : vs)
        cin >> v.first >> v.second;

    bd = vector<vector<int> >(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> bd[i][j];
        }
    }

    while (q--) {
        int u, v;
        cin >> u >> v;
        u--, v--;

        multimap<double, pair<int, pair<int, int> > > mm;
        mm.insert(make_pair(0, make_pair(u, make_pair(0, 0))));

        vector<vector<pair<int, int> > > dist(n, vector<pair<int, int> >(n, make_pair(-1, -1)));
        // dist[0][0] = make_pair(0, 0);

        while (mm.size()) {
            double cur_time = mm.begin()->first;
            int cur_pos = mm.begin()->second.first;
            int got = mm.begin()->second.second.first;
            int rest = mm.begin()->second.second.second;
            mm.erase(mm.begin());

            if (cur_pos == v) {
                cout << " " << setiosflags(ios::fixed) << setprecision(12) << cur_time;
                break;
            }

            if (dist[cur_pos][got].first >= 0 && dist[cur_pos][got].second >= rest) {
                continue;
            }
            dist[cur_pos][got] = make_pair(cur_time, rest);

            for (int i = 0; i < n; i++) {
                int d = bd[cur_pos][i];
                if (d < 0)
                    continue;

                if (rest >= d) {
                    mm.insert(make_pair(cur_time + (double)d / vs[got].second, make_pair(i, make_pair(got, rest - d))));
                }
                if (vs[cur_pos].first >= d) {
                    mm.insert(make_pair(cur_time + (double)d / vs[cur_pos].second, make_pair(i, make_pair(cur_pos, vs[cur_pos].first - d))));
                }
            }
        }
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ":";
        solve2();
    }
    return 0;
}