#include <bits/stdc++.h>

using namespace std;

long double solution() {
    int n, k;
    long double u;
    cin >> n >> k;
    cin >> u;
    vector <long double> p(n);
    for (auto &x : p) {
        cin >> x;
    }
    p.push_back(1);
    sort(p.begin(), p.end());
    auto level = p[0];
    bool flag = false;
    for (auto i = 0; i + 1 < p.size(); i++) {
        if (u < (p[i + 1] - p[i]) * (i + 1)) {
            level = p[i] + u / (i + 1);
            flag = true;
            break;
        }
        u -= (p[i + 1] - p[i]) * (i + 1);
    }
    if (!flag) {
        return 1;
    }
    long double prob = 1;
    for (const auto &x : p) {
        prob *= max(x, level);
    }
    return prob;
}


int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout.precision(20);
        cout << fixed;
        cout << "Case #" << test << ": " << solution() << '\n';
    }
    return 0;
}
