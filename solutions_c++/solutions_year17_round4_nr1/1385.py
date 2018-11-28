#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>

using namespace std;
const int N = 100;
int case_num;
int f[N][N][N][N];
int ok[N][N][N][N];


int n, p;

int dfs(int a1, int a2, int a3, int k) {
    if (ok[a1][a2][a3][k]) {
        return f[a1][a2][a3][k];
    }
    int res = 0;

    if (a1) {
        int last_k = (k + p - 1) % p;
        int x = dfs(a1 - 1, a2, a3, last_k);
        if (last_k == 0) 
            x++;
        res = max(res, x);
    }

    if (a2) {
        int last_k = (k + p - 2) % p;
        int x = dfs(a1, a2 - 1, a3, last_k);
        if (last_k == 0) 
            x++;
        res = max(res, x);
    }

    if (a3) {
        int last_k = (k + p - 3) % p;
        int x = dfs(a1, a2, a3 - 1, last_k);
        if (last_k == 0) 
            x++;
        res = max(res, x);
    }

    ok[a1][a2][a3][k] = 1;
    f[a1][a2][a3][k] = res;
    return res;
}


void solve() {
    memset(f, 0, sizeof(f));
    memset(ok, 0, sizeof(ok));
    ok[0][0][0][0] = 1;

    cin >> n >> p;
    vector<int> sum(4);
    int all = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        all += x;
        sum[x % p]++;
    }
    int ans = dfs(sum[1], sum[2], sum[3], all % p);
    ans += sum[0];
    cout << ans;
}


int main() {
    cin >> case_num;

    for (int i = 1; i <= case_num; ++i) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }

}

