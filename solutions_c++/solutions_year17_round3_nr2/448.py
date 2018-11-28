#include <bits/stdc++.h>

using namespace std;

int compute(int k1, int k2, const auto &vec1, const auto &vec2, const auto &point) {
    int count1 = 0, count2 = 0;
    for (auto i = 0; i < point.size(); i++) {
        if (point[i].second) {
            count2 += point[i].first.second - point[i].first.first;
        } else {
            count1 += point[i].first.second - point[i].first.first;
        }
    }
    for (int i = 0; i < k1; i++) {
        count1 += vec1[i];
    }
    for (int i = 0; i < k2; i++) {
        count2 += vec2[i];
    }
    if (max(count1, count2) > 12 * 60) {
        return -1;
    }
    return (point.size() - vec1.size() - vec2.size()) + 2 * (vec1.size() - k1 + vec2.size() - k2); 
}

int solution() {
    int n, m;
    cin >> n >> m;
    vector <pair<pair <int, int>, int>> point(n + m);
    for (int i = 0; i < n; i++) {
        cin >> point[i].first.first >> point[i].first.second;
        point[i].second = 0;
    }
    for (int i = n; i < n + m; i++) {
        cin >> point[i].first.first >> point[i].first.second;
        point[i].second = 1;
    }
    if (n + m == 1) {
        return 2;
    }
    sort(point.begin(), point.end());
    vector <int> first, second;
    for (int i = 0; i < n + m; i++) {
        int next = (i + 1) % (n + m);
        if (point[i].second != point[next].second)
            continue;
        int duration = point[next].first.first - point[i].first.second;
        if (next == 0)
            duration += 24 * 60; 
        if (point[i].second == 0) {
            first.push_back(duration);
        } else {
            second.push_back(duration);
        } 
    }
    sort(first.begin(), first.end());
    sort(second.begin(), second.end());
    int min_changes = 100100;
    for (int k1 = 0; k1 <= first.size(); k1++) {
        for (int k2 = 0; k2 <= second.size(); k2++) {
            auto res = compute(k1, k2, first, second, point);
            if (res == -1)
                continue;
            min_changes = min(min_changes, res);
        }
    }
    return min_changes;
}


int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": " << solution() << '\n';
    }
    return 0;
}
