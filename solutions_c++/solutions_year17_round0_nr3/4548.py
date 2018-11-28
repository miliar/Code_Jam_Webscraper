#include <bits/stdc++.h>

using namespace std;

std::vector<int> calculate_l(const std::vector<bool> &s) {
    std::vector<int> l(s.size());
    for (int j = 0; j < (int) s.size(); ++j) {
        if (s[j])
            l[j] = 0;
        else
            l[j] = l[j - 1] + 1; 
    }
    return l;
}

std::vector<int> calculate_r(const std::vector<bool> &s) {
    vector<int> r(s.size());
    for (int j = (int)s.size() - 1; j >= 0; --j) {
        if (s[j])
            r[j] = 0;
        else
            r[j] = r[j + 1] + 1;
    }
    return r;
}

pair<int, int> solve1(int n, int k) {
    vector<bool> s(n + 2);
    vector<int>  l(n + 2);
    vector<int>  r(n + 2);
    s[0] = s[n + 1] = true;
    int best_mins, best_maxs;
    for (int i = 0; i < k; ++i) {
        l = calculate_l(s);
        r = calculate_r(s);
        int best_location = 0;
        while (s[++best_location]) {}
        best_mins = min(l[best_location], r[best_location]);
        best_maxs = max(l[best_location], r[best_location]);
        for (int i = best_location + 1; i <= n; ++i) {
            int mins = min(l[i], r[i]);
            int maxs = max(l[i], r[i]);
            if (best_mins > mins)
                continue;
            if (best_mins == mins && best_maxs >= maxs)
                continue;
            best_location = i;
            best_mins = mins;
            best_maxs = maxs;
        }
        s[best_location] = true;
    }
    return {best_mins - 1, best_maxs - 1};
}

pair<int, int> solve2(int n, int k) {
    multiset<int, greater<int>> s;
    s.insert(n);
    int x, a, b;;
    for (int i = 0; i < k; ++i) {
        x = *s.begin();
        s.erase(s.begin());
        a = x / 2;
        b = x / 2 + x % 2;
        s.insert(a);
        s.insert(b - 1);
    }
    return {b - 1, a};
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        cin >> n >> k;
        //        auto res1 = solve1(n, k);
        auto res2 = solve2(n, k);
        //assert(res1 == res2);
        auto &res = res2;
        cout << "Case #" << i + 1 << ": " << res.second<< " "
             << res.first << "\n";
    }
}
