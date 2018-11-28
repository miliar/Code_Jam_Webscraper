#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <climits>
#include <string>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef double long ld;

int solve(int i, int tc, int tj, vector<pair<int, pair<int, int> > >& gaps, vector<vector<vector<int> > >& dp)
{
    if (i == gaps.size()) {
        if (tc != 0 || tj != 0) {
            return 100000;
        }
        return 0;
    }
    if (dp[i][tc][tj] != -1) {
        return dp[i][tc][tj];
    }
    if (tc == 0) {
        int res = 0;
        for (int j = i; j < gaps.size(); ++j) {
            res += (gaps[j].second.first == 0);
            res += (gaps[j].second.second == 0);
        }
        return res;
    }
    if (tj == 0) {
        int res = 0;
        for (int j = i; j < gaps.size(); ++j) {
            res += (gaps[j].second.first == 1);
            res += (gaps[j].second.second == 1);
        }
        return res;
    }
    int res = 1000000;
    for (int t = 0; t <= gaps[i].first; ++t) {
        int t1 = gaps[i].first - t;
        if (tc >= t && tj >= t1) {
            int next = solve(i+1, tc - t, tj - t1, gaps, dp);
            if (t == 0) {
                next += (gaps[i].second.first == 0);
                next += (gaps[i].second.second == 0);
            } else if (t1 == 0) {
                next += (gaps[i].second.first == 1);
                next += (gaps[i].second.second == 1);
            } else {
                next += (gaps[i].second.first == 1);
                next += (gaps[i].second.second == 0);
                next++;
            }
            res = min(res, next);
        }
        if (tc >= t1 && tj >= t && t != 0 && t1 != 0) {
            int next = solve(i+1, tc - t1, tj - t, gaps, dp);
            next += (gaps[i].second.first == 0);
            next += (gaps[i].second.second == 1);
            next++;
            res = min(res, next);
        }
    }
    //cerr << i << ' ' << tc << ' ' << tj << ' ' << res << endl;
    return dp[i][tc][tj] = res;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        int ac, aj;
        cin >> ac >> aj;
        int tc = 720, tj = 720;
        vector<pair<int, pair<int, int> > > v(ac + aj);
        for (int i = 0; i < ac; ++i) {
            cin >> v[i].first >> v[i].second.first;
            v[i].second.second = 1;
            tj -= v[i].second.first - v[i].first;
        }
        for (int i = 0; i < aj; ++i) {
            cin >> v[ac+i].first >> v[ac+i].second.first;
            v[ac+i].second.second = 0;
            tc -= v[ac+i].second.first - v[ac+i].first;
        }
        sort(v.begin(), v.end());
        vector<pair<int, pair<int, int> > > gaps;
        int last = 0, lastOwner = -1;
        if (v.size() > 0) {
            last = v[v.size()-1].second.first;
            lastOwner = v[v.size()-1].second.second;
        }
        int base = 0;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i].first != last && (last != 1440 || v[i].first != 0)) {
                int l = v[i].first - last;
                if (l < 0) {
                    l = 1440 - last + v[i].first;
                }
        //        cerr << "gap " << last << ' ' << v[i].first << ' ' << lastOwner << "," << v[i].second.second << endl;
                gaps.push_back({ l, { lastOwner, v[i].second.second }});
            } else {
                if (lastOwner != v[i].second.second) {
                    base++;
                }
            }
            last = v[i].second.first;
            lastOwner = v[i].second.second;
        }
        //for (int i = 0; i < gaps.size(); ++i) {
        //  cerr << gaps[i].first << ' ' << gaps[i].second.first << ' ' << gaps[i].second.second << endl;
        //}
        //cerr << tc << ' ' << tj << ' ' << base << endl;
        vector<vector<vector<int> > > dp(gaps.size(), vector<vector<int> >(tc+1, vector<int>(tj+1, -1)));
        cout << "Case #" << cas << ": " << base + solve(0, tc, tj, gaps, dp) << endl;
    }
}
