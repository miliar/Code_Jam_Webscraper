#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cmath>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first) {
        return a.second < b.second;
    }
    return a.first > b.first;
}

pair<int, int> solve(int n, int k) {
    bool(*fn_pt)(pair<int, int>,pair<int, int>) = cmp;
    set<pair<int, int>, bool(*)(pair<int, int>,pair<int, int>)> s(cmp);
    s.insert(mp(n, 0));
    for (int i = 0; i < k - 1; i++) {
        auto t = *s.begin();
        s.erase(s.begin());
        pair<int, int> a, b;
        int l = t.first;
        int place = t.second;
        if (l == 1) {
            continue;
        }
        if (l == 2) {
            s.insert(mp(1, place + 1));
            continue;
        }
        if (l % 2) {
            a.first = b.first = l / 2;
            a.second = place;
            b.second = place + l / 2 + 1;
        } else {
            a.first = l / 2 - 1;
            b.first = l / 2;
            a.second = place;
            b.second = place + l / 2;
        }
        s.insert(a);
        s.insert(b);
    }
    auto t = *s.begin();
    if (t.first % 2) {
        return mp(t.first / 2, t.first / 2);
    } else {
        return mp(t.first / 2, t.first / 2 - 1);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int z = 0; z < t; z++) {
        string s;
        int n, k;
        cin >> n >> k;
        auto ans = solve(n, k);
        cout << "Case #" << z + 1 << ": " << ans.first << ' ' << ans.second << '\n';
    }
    return 0;
}