#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

void solve() {
    int N, C, M;
    vector<pair<int, int>> tickets;

    cin >> N >> C >> M;
    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y;
        tickets.emplace_back(x, y);
    }

    sort(tickets.begin(), tickets.end());
    map<int, int> people;
    int ans = 0;
    for (int i = 0; i < M; i++) {
        int p = tickets[i].first;
        int b = tickets[i].second;
        people[b]++;
        ans = max(ans, (i+1 + p - 1) / p);
    }
    for (const auto& kvp : people) {
        ans = max(ans, kvp.second);
    }

    int promote = 0;
    map<int, int> seat_to_count;
    for (int i = 0; i < M; i++) {
        int p = tickets[i].first;
        int b = tickets[i].second;
        if (seat_to_count[p] == ans) {
            promote++;
        } else {
            seat_to_count[p]++;
        }
    }

    cout << ans << ' ' << promote << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
