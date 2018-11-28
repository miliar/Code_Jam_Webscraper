#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int T;
int n, m;
int cost[100];
vector<int> a[100];

void solve(int num) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", cost + i);
        a[i].clear();
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int x;
            scanf("%d", &x);
            a[i].pb(x);
        }
        sort(all(a[i]));
    }
    vector<int> it;
    for (int i = 0; i < n; i++) it.pb(0);
    int ans = 0;
    for (int k = 1;;) {
        bool ok = true;
        bool finish = false;
        for (int i = 0; i < n; i++) {
            if (it[i] == m) {
                finish = true;
                break;
            }
            double L = 0.9 * k * cost[i];
            double R = 1.1 * k * cost[i];
            while (it[i] < m && a[i][it[i]] < L) it[i]++;
            if (it[i] < m && a[i][it[i]] > R) ok = false;
            if (it[i] == m) ok = false;
        }
        if (finish) break;
        if (!ok) {
            k++;
            continue;
        }
        ans++;
        for (int i = 0; i < n; i++) it[i]++;
    }
    printf("Case #%d: %d\n", num, ans);
}

int main(){

    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        solve(i);
    }

    return 0;
}
