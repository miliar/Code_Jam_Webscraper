#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <queue>

using namespace std;

#define DEBUG

int T;
int a, b;
vector < pair < int, int > > sa, sb;

const int N = 24 * 60;

bool is_inter(pair<int, int> x, int l, int r) {
    if (l < r) {
        return (x.first >= l && x.first < r) || (x.second > l && x.second <= r);
    }

    return (x.first >= 0 && x.first < r) || x.first >= l;
}

bool is_in(pair<int, int> x, int l, int r) {
    if (l < r) {
        return x.first >= l && x.second <= r;
    }

    return x.second <= r || x.first >= l;
}

int solve() {
    scanf("%d %d", &a, &b);

    sa.resize(a);
    for (int i = 0; i < a; ++i) {
        scanf("%d %d", &sa[i].first, &sa[i].second);
    }

    sort(sa.begin(), sa.end());

    sb.resize(b);
    for (int i = 0; i < b; ++i) {
        scanf("%d %d", &sb[i].first, &sb[i].second);
    }

    sort(sb.begin(), sb.end());

    if (a + b <= 1) {
        return 2;
    }

    for (int l = 0; l < N; ++l) {
        int r = (l + 720) % N;

        int a_in = 0;
        int a_inter = 0;

        for (int i = 0; i < sa.size(); ++i) {
            if (is_inter(sa[i], l, r)) {
                ++a_inter;
            }

            if (is_in(sa[i], l, r)) {
                ++a_in;
            }
        }

        int b_in = 0;
        int b_inter = 0;

        for (int i = 0; i < sb.size(); ++i) {
            if (is_inter(sb[i], l, r)) {
                ++b_inter;
            }

            if (is_in(sb[i], l, r)) {
                ++b_in;
            }
        }

        if (sa.size() > 0 && a_in == sa.size() && b_inter == 0) {
            return 2;
        }

        if (sb.size() > 0 && b_in == sb.size() && a_inter == 0) {
            return 2;
        }
    }

    return 4;
}

int main() {
    ios::sync_with_stdio(false);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: %d\n", t, solve());
    }

    return 0;
}