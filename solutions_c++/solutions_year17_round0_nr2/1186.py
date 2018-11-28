#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
#include <stdlib.h>
using namespace std;

void smain();
int main() {
    ios_base::sync_with_stdio(0);
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/B-large.in.txt","rt",stdin);
    freopen(TASK".out","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define LL long long
#define int long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-8
#define N 1000002
/* --------- END TEMPLATE CODE --------- */

int solve(int n) {
    vector<int> d;
    for (; n; n /= 10) d.push_back(n % 10);
    reverse(d.begin(), d.end());
    int m = d.size();
    while (1) {
        int i = 1;
        for (; i < m && d[i] >= d[i-1]; ++i);
        if (i == m) break;
        d[i - 1] -= 1;
        for (; i < m; ++i) d[i] = 9;
    }
    for (auto i : d) n = 10 * n + i;
    return n;
}

void smain() {
    int n;
    cin >> n;
    for (int cas = 1; cin >> n; ++cas) {
        cout << "Case #" << cas << ": " << solve(n) << '\n';

    }
}

