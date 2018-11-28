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

int p;

int solve(map<int, int>& v, int left, map<map<int, int>, int>& dp)
{
    if (dp.find(v) != dp.end()) {
        return dp[v];
    }
    int res = 0;
    int extra = (left == 0) ? 1 : 0;
    for (int i = 1; i < p; ++i) {
        if (v[i] > 0) {
            v[i]--;
            int left2 = (p - i + left)%p;
            res = max(res, solve(v, left2, dp) + extra);
            v[i]++;
        }
    }
    return dp[v] = res;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        int n;
        cin >> n >> p;
        map<int, int> v;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int g;
            cin >> g;
            if (g%p == 0) {
                res++;
            } else {
                v[g%p]++;
            }
        }
        map<map<int, int>, int > dp;
        cout << "Case #" << cas << ": " << res + solve(v, 0, dp) << endl;
    }
}
