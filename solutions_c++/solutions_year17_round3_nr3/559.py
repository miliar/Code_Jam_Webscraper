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

bool eqn(double a, double b) {
    return abs(a - b) < 1e-14;
}

// end is exclusive
double maximize(int end, double u, vector<double> &p, vector<double> &accum) {
    int n = end;
    double mean = (accum[end]+u) / n;
    int j = 0;
    while (j < end && (!eqn(p[j], mean) && p[j] < mean))
        j++;
    if (j == end) {
        return pow(mean, n);
    }
    double res = 1.0;
    FOR(i, j, n) {
        res *= p[i];
    }
    return res * maximize(j, u, p, accum);
}

int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        int n, k;
        cin >> n >> k;

        double u;
        cin >> u;
        vector<double> p(n);
        FOR(i, 0, n) {
            cin >> p[i];
        }
        sort(p.begin(), p.end());
        vector<double> rest(n);
        FOR(i, 0, n) {
            rest[i] = 1.0 - p[i];
        }
        auto check = accumulate(rest.begin(), rest.end(), 0.0);
        if (eqn(check, u) || check < u) {
            cout << 1.0 << endl;
            continue;
        }

        vector<double> accum(n + 1, 0.0);
        IFOR(i, 1, n) {
            accum[i] = accum[i - 1] + p[i - 1];
        }
        double res = maximize(n, u, p, accum);
        printf("%.14f\n", res);

    }
    return 0;
}