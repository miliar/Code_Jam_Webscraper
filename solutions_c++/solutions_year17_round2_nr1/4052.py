#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <bitset>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int t;
int d, n;
pair<pair<double, double>, pair<double, double> > h[1010];
double tt, pp, ttt, ppp, tttt, pppp;

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        printf("Case #%d: ", cas);
        scanf("%d %d", &d, &n);
        for(int i = 0; i < n; ++i) {
            int p, v;
            scanf("%d %d", &p, &v);
            h[i].first.first = p;
            h[i].first.second = v;
            h[i].second.first = h[i].second.second = 0;
        }
        sort(h, h + n, greater<pair<pair<double, double>, pair<double, double> > >());
        for(int i = 1; i < n; ++i) {
            if (h[i].first.second <= h[i - 1].first.second) {
                if (h[i - 1].second.first != 0 && h[i - 1].second.second < h[i].first.second) {
                    tt = (h[i - 1].second.first - h[i - 1].first.first) / h[i - 1].first.second;
                    pp = h[i].first.first + tt * h[i].first.second;
                    ttt = (h[i - 1].second.first - pp) / (h[i].first.second - h[i - 1].second.second);
                    ppp = pp + ttt * h[i].first.second;
                    if (ppp < d) {
                        h[i].second.first = ppp;
                        h[i].second.second = h[i - 1].second.second;
                    }
                }
            } else {
                tt = (h[i - 1].first.first - h[i].first.first) / (h[i].first.second - h[i - 1].first.second);
                pp = h[i].first.first + tt * h[i].first.second;
                if (h[i - 1].second.first == 0) {
                    if (pp < d) {
                        h[i].second.first = pp;
                        h[i].second.second = h[i - 1].first.second;
                    }
                } else {
                    if (h[i - 1].second.first < pp) {
                        ttt = (h[i - 1].second.first - h[i - 1].first.first) / h[i - 1].first.second;
                        ppp = h[i].first.first + ttt * h[i].first.second;

                        tttt = (h[i - 1].second.first - ppp) / (h[i].first.second - h[i - 1].second.second);
                        pppp = ppp + h[i].first.second * tttt;
                        if (pppp < d) {
                            h[i].second.first = pppp;
                            h[i].second.second = h[i - 1].second.second;
                        }
                    } else {
                        ttt = (h[i - 1].second.first - pp) / (h[i].first.second - h[i - 1].second.second);
                        ppp = pp + ttt * h[i].first.second;
                        if (ppp < d) {
                            h[i].second.first = ppp;
                            h[i].second.second = h[i - 1].second.second;
                        }
                    }
                }
            }
        }

        if (h[n - 1].second.first == 0) {
            tt = ((double)d - h[n - 1].first.first) / h[n - 1].first.second;
            double vv = d / tt;
            printf("%.10lf\n", vv);
        } else {
            tt = (h[n - 1].second.first - h[n - 1].first.first) / h[n - 1].first.second;
            tt += ((double)d - h[n - 1].second.first) / h[n - 1].second.second;
            double vv = d / tt;
            printf("%.10lf\n", vv);
        }

    }

    return 0;
}
