#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <cassert>

using namespace std;

#define mp make_pair
#define sqr(x) ((x)*(x))

typedef long long ll;

int n, p;
vector<int> a;
vector<int> b;
vector<long double> abl;
vector<long double> ans;
int inf;

long double col_time(pair<int, int> ks1, pair<int, int> ks2) {
    return 1.0l * (ks1.first - ks2.first) / (ks2.second - ks1.second);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        int n, d;
        cin >> d >> n;

        vector<pair<int, int> > ks(n);
        for (int i = 0; i < n; i++) {
            cin >> ks[i].first >> ks[i].second;
        }

        sort(ks.begin(), ks.end());

        long double total = 0;
        long double pos = ks[0].first;
        for (int i = 0; i < n; i++) {
            long double minct = (1.0l * d - pos) / ks[i].second;
            bool will_col = false;
            for (int j = i + 1; j < n; j++) {
                if (ks[j].second == ks[i].second) {
                    continue;
                }

                long double ct = col_time(ks[i], ks[j]);

                if (ct < 0) {
                    continue;
                }

                if (minct > ct) {
                    will_col = true;
                    minct = ct;
                    break;
                }
            }

            total += minct;
            pos += minct * ks[i].second;
            if (!will_col) {
                break;
            }
        }

        cout << fixed << setprecision(22) << 1.0l * d / total << endl;
    }
}