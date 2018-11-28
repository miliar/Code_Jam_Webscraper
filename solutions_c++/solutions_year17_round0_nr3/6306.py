#include <algorithm>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

map<int, vector<int>, greater<int>> tree;

void calc(int tl, int tr) {
    if (tl > tr) {
        return;
    }
    int len = tr - tl + 1;
    int mid = (tl + tr) / 2;
    tree[len].push_back(mid);
    if (tl == tr) {
        return;
    }
    calc(tl, mid - 1);
    calc(mid + 1, tr);
}

void solve() {
    tree.clear();
    int n, k;
    scanf("%d %d", &n, &k);
    calc(0, n - 1);
    int c = 0;
    int last = 0;
    vector<bool> used(n, false);
    for (auto i : tree) {
        for (auto j : i.second) {
            last = j;
            used[j] = true;
            ++c;
            if (c == k) {
                break;
            }
        }
        if (c == k) {
            break;
        }
    }
    pair<int, int> ans = {0, 0};
    while (last - ans.first - 1 >= 0 && !used[last - ans.first - 1]) {
        ++ans.first;
    }
    while (last + ans.second + 1 < n && !used[last + ans.second + 1]) {
        ++ans.second;
    }
    ans = {max(ans.first, ans.second), min(ans.first, ans.second)};
    printf("%d %d\n", ans.first, ans.second);
}


int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t = 1;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
