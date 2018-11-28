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
    freopen("/Users/ramis/Downloads/C-large.in.txt","rt",stdin);
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
set<int> was;
void f(int n) {
    if (n == 0 || was.count(n)) return;
    was.insert(n);
    int l = (n - 1) / 2;
    int r = n - l - 1;
    f(l);
    f(r);
}

pair<int, int> solve(int n, int k) {
    was.clear();
    f(n);
    map<int, int> cnt;
    cnt[n] = 1;
    was.erase(n);
    for (auto it = was.rbegin(); it != was.rend(); ++it) {
        int s = 0;
        for (int m = 2 * *it; m <= n; ++m) {
            int l = (m - 1) / 2;
            int r = m - 1 - l;
            if (l > *it) break;
            if (cnt.count(m)) s += (l == r ? 2 : 1) * cnt.at(m);
        }
        
        cnt[*it] = s;
    }
    int res = n;
    for (auto it = cnt.rbegin(); it != cnt.rend() && k > 0; ++it) {
        res = it->first;
        k -= it->second;
    }
    res -= 1;
    return mp(res / 2, res - res / 2);
}

pair<int, int> naive(int n, int k) {
    priority_queue<int> q;
    q.push(n);
    int l = 0, r = 0;
    forn(i, k) {
        int cur = q.top() - 1;
        q.pop();
        l = cur / 2;
        r = cur - l;
        if (r) q.push(r);
        if (l) q.push(l);
    }
    if (l > r) swap(l, r);
    return mp(l, r);
}


void smain() {
    int n, k;
    cin >> n;
    for (int cas = 1; cin >> n >> k; ++cas) {
        auto res = solve(n, k);
        cout << "Case #" << cas << ": " << res.second << ' ' << res.first << '\n';
        cerr << "Case #" << cas << ": " << res.second << ' ' << res.first << endl;
    }
}

