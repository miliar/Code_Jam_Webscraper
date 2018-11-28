#include <bits/stdc++.h>

using namespace std;

typedef long long li;

void solve(int);

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
}

void solve(int test_case) {
    int n, k;
    cin >> n >> k;
    set<pair<int, int> > all;
    all.insert({ n, 0 });
    int l = -1, r = -1;
    for (int i = 0; i < k; i++) {
        auto cur = *all.rbegin();
        all.erase(cur);
        int start = cur.second;
        r = (cur.first - 1) / 2;
        l = (cur.first - 1) / 2 + (cur.first - 1) % 2;
        all.insert({ l, start });
        all.insert({ r, start + l + 1 });
    }
    cout << "Case #" << test_case << ": " << l << ' ' << r << endl;
}
