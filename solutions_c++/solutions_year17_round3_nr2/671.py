#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
//#include "utils/haha.h"
//#include "utils/max_flow.h"
using namespace std;
typedef pair<int, int> PII;
typedef pair<string, string> PSS;
typedef pair<int, PII> PIP;
typedef long long ll;
typedef pair<ll, ll> PLL;
typedef pair<double, double> PDD;
typedef pair<ll, PII> PLP;
#define CLS(x, v) (memset((x), (v), sizeof((x))))
const double pi = acos(-1);

int ac, aj;


int dp[210][800][800];

void solve(int ncase) {
    cout << "Case #" << ncase << ": ";
    cin >> ac >> aj;
    if (ac + aj == 0) {
        cout << 0 << endl;
        return;
    }
    vector<PIP> range;
    int leftA = 720, leftB = 720;
    for(int i = 0; i < ac; i++) {
        int x, y;
        cin >> x >> y;
        leftA -= y - x;
        range.push_back(PIP(x, PII(y, 0)));
    }

    for(int i = 0; i < aj; i++) {
        int x, y;
        cin >> x >> y;
        leftB -= y - x;
        range.push_back(PIP(x, PII(y, 1)));
    }
    sort(range.begin(), range.end());
    int offset = range[0].first;
    for(auto &p : range) {
        p.first -= offset;
        p.second.first -= offset;
    }
    /*t1[range[0].second.second] += range[0].first;
    t1[range.back.second.second] += 1440 - range.back().second.first;
    for(int i = 1; i < range.size(); i++) {
        tt[range[i-1].second.second][range[i].second.second] += range[i].first - range[i-1].second.first;
    }
    */
    for(int i = 0; i <= range.size(); i++) {
        for(int j = 0; j <= 720; j++) {
            for(int k = 0; k <= 720; k++) {
                dp[i][j][k] = 1441;
            }
        }
    }
    //before i == 0;
    for(int t = 0; t <= leftA && t <= range[0].first; t++) {
        int z[2];
        z[0] = t;
        z[1] = range[0].first - t;
        if (z[1] > leftB) continue;
        int &u = dp[0][leftA - z[0]][leftB - z[1]];
        if (z[1 - range[0].second.second]) u = 1;
        else u = 0;
    }
    //cout << range.size() << endl;
    for(int i = 0; i <= range.size(); i++) {
        for(int la = 0; la <= leftA; la++) {
            for(int lb = 0; lb <= leftB; lb++) {
                if (dp[i][la][lb] <= 1440) {
                    //printf("dp[%d][%d][%d] = %d\n", i, la, lb, dp[i][la][lb]);
                    if (i == range.size()) continue;
                    int len = range[(i+1) % range.size()].first - range[i].second.first;
                    if (len < 0) len += 1440;
                    for(int t = 0; t <= len && t <= la; t++) {
                        int z[2] = {t, len - t};
                        if (z[1] > lb) continue;
                        int &u = dp[i+1][la - z[0]][lb - z[1]];
                        if (range[(i+1)%range.size()].second.second != range[i].second.second) {
                            u = min(u, dp[i][la][lb] + 1);
                            continue;
                        }
                        if (z[1-range[i].second.second]) {
                            u = min(u, dp[i][la][lb] + 2);
                        } else {
                            u = min(u, dp[i][la][lb]);
                        }
                    }
                    
                    /*if (i + 1 < range.size()) {
                        int len = range[i+1].first - range[i].second.first;
                        for(int t = 0; t <= len && t <= la; t++) {
                            int z[2] = {t, len - t};
                            if (z[1] > lb) continue;
                            int &u = dp[i+1][la - z[0]][lb - z[1]];
                            if (range[i-1].second.second != range[i].second.second) {
                                u = min(u, dp[i][la][lb] + 1);
                                continue;
                            }
                            if (z[1-range[i-1].second.second]) {
                                u = min(u, dp[i][la][lb] + 2);
                            } else {
                                u = min(u, dp[i][la][lb]);
                            }
                        }
                    } else {
                        int z[2] = {la, lb};
                        assert(la + lb == 1440 - range[i].second.first);
                        int &u = dp[i+1][0][0];
                        if (z[1-range[i].second.second]) u = min(u, dp[i][la][lb]+1);
                        else u = min(u, dp[i][la][lb]);
                        if (z[1-range[i].second.second] == 0) {
                        printf("wrong dp[%d][%d][%d] = %d\n", i, la, lb, dp[i][la][lb]);
                        }
                    }*/
                }
            }
        }
    }
    cout << dp[range.size()][0][0] << endl;
}


int main() {
    //ios::sync_with_stdio(false);
    cout << std::fixed;
    cout << setprecision(16);
#ifdef _zzz_
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
#endif
    //precalc();
    int T = 1;
    scanf("%d", &T);
    //cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
