#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;
const double PI = acos(-1);

int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        int n, k;
        cin >> n >> k;
        // r, h
        vector<pair<long long, long long>> cakes(n);
        vector<long long> rh(n);
        FOR(i, 0, n) {
            cin >> cakes[i].first >> cakes[i].second;
        }
        sort(cakes.begin(), cakes.end(), greater<pair<long long, long long>>());

        FOR(i, 0, n) {
            rh[i] = cakes[i].first * cakes[i].second;
        }
        double maxx = 0.0;

        IFOR(i, 0, n - k) {
            // start point = i
            vector<long long> rh_tmp(n - i - 1);
            copy(rh.begin() + i + 1, rh.end(), rh_tmp.begin());
            sort(rh_tmp.begin(), rh_tmp.end(), greater<long long>());

            auto res1 = accumulate(rh_tmp.begin(), rh_tmp.begin() + (k - 1), 0LL);
            maxx = max(maxx, (res1 + cakes[i].first*cakes[i].second) * 2 * PI + PI*cakes[i].first*cakes[i].first);
        }
        printf("%.14f\n", maxx);

    }
    return 0;
}