#include <cstdio>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

map<vector<int>, int> memo;

int solve(vector<int> ds, int P) {
    if (memo.count(ds)) return memo[ds];
    int leftover = ds[0];
    int ans = 0;

    for(int i = 1; i < ds.size(); i++) {
        if (ds[i] > 0) {
            vector<int> nds = ds;
            nds[i] -= 1;
            nds[0] = (leftover + i) % P;

            ans = max(ans, (leftover == 0) + solve(nds, P));
        }
    }
    memo[ds] = ans;
    return ans;
}

int main() {
    int T; scanf("%d", &T); int test_id = 0;
    while (test_id < T) { test_id += 1;
        cerr << test_id << endl;
        printf("Case #%d: ", test_id);
        memo.clear();       
        int n, P; scanf("%d %d", &n, &P);
        vector<int> ds(P);
        for(int i = 0; i < n; i++) {
            int val; scanf("%d", &val);
            ds[val % P] += 1;
        }
        int ans = ds[0];
        ds[0] = 0;
        printf("%d\n", ans + solve(ds, P));
    }
}
