#include "bits/stdc++.h"
#define puba push_back
#define ff first
#define ss second
#define bend(_x) begin(_x), end(_x)
#define szof(_x) ((int) (_x).size())
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9 + 7;
const ll INFL = 1e18 + 123;
const double PI = atan2(0, -1);

map<vector<int>, int> mem[5];
int p;

int rec(vector<int> v, int sum) {
    if (mem[sum].count(v)) {
        return mem[sum][v];
    }
    int& val = mem[sum][v];
    for (int i = 1; i < szof(v); ++i) {
        if (v[i]) {
            v[i]--;
            val = max(val, rec(v, (sum + i) % p) + (sum == 0));
            v[i]++;
        }
    }
    return val;
}

int solve() {
    int n;
    scanf("%d%d", &n, &p);

    vector<int> inp(p);
    for (int i = 0; i < n; ++i) {
        int num;
        scanf("%d", &num);
        inp[num % p]++;
    }

    int ans = inp[0];
    inp[0] = 0;

    cout << ans + rec(inp, 0) << "\n";

    return 0;
}

int main() {
    //freopen(TASK_NAME ".in", "r", stdin);
    //freopen(TASK_NAME ".out", "w", stdout);
    cerr << fixed << setprecision(15);
    cout << fixed << setprecision(15);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    #ifdef LOCAL
        cerr << "time: " << clock() << endl;
    #endif
    return 0;
}