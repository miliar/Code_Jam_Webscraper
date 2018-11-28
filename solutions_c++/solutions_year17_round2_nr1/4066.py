#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <stack>
#include <list>
#include <forward_list>
#include <algorithm> // max...
#include <utility> // pair
#include <complex>
#include <climits> // int, ll...
#include <limits> // double...
#include <cmath> // abs, atan...
#include <cstring> // memset
#include <string>
#include <functional> // greater, less...
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, double> id;
typedef pair<double, int> di;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef vector<id> vid;
typedef vector<vi> vvi;
typedef map<int, int> mii;
typedef map<int, ll> mil;
typedef map<ll, ll> mll;

#define ONLINE_JUDGE

int main() {
#ifdef ONLINE_JUDGE
    freopen("A-small-attempt0.in", "r", stdin);
        freopen("A-small-attempt0.out", "w", stdout);
        //freopen("X-large-practice.in", "r", stdin);
        //freopen("X-large-practice.out", "w", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    //freopen("output.out", "w", stdout);
#endif
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int D, N;
        cin >> D >> N;

        vdd h;
        for (int i = 0; i < N; i++) {
            int k, s;
            cin >> k >> s;
            h.push_back(ii(k, s));
        }

        sort(h.begin(), h.end());

        // find slowest horse.
        double slowestv = h[0].second;
        auto its = h.begin();
        for (auto i = ++h.begin(); i < h.end(); ++i) {
            if ((*i).second < slowestv) {
                slowestv = (*i).second;
                its = i;
            }
        }

        // remove all horses to the right.
        auto it = its; ++it;
        for (; it < h.end(); ++it) {
            h.erase(it);
        }

        double time = 0;
        while (h.size() != 1) {
            auto it = its; --it;
            double d1 = (*its).first, s1 = (*its).second;
            double d2 = (*it).first, s2 = (*it).second;

            double t = (d1 - d2) / (s2 - s1);
            double d = d1 + s1 * t;
            if (d <= D) { // combine horses, remove (d2, s2)
                (*its).first = d;
                h.erase(it);
                time += t;
            } else { // remove (d1, s1)
                h.erase(its);
                its = it;
            }
        }

        double d1 = (*its).first, s1 = (*its).second;
        double time2 = (D - d1) / s1;
        double S = D / (time + time2);

        printf("Case #%d: %6f\n", t, S);
    }

    return 0;
}