#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>

using namespace std;

void solve_case() {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    vector<char> ans;
    vector<pair<int, char> > ps;
    if (R > 0) ps.push_back(make_pair(R, 'R'));
    if (Y > 0) ps.push_back(make_pair(Y, 'Y'));
    if (B > 0) ps.push_back(make_pair(B, 'B'));
    sort(ps.begin(), ps.end());
    if (ps.size() == 1) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if (ps[0].first == ps[ps.size() - 1].first) {
        int t = ps[0].first;
        for (int i = 0; i < t; i++) {
            for (int j = 0; j < ps.size(); j++) {
                cout << ps[j].second;
            }
        }
        cout << endl;
        return;
    }
    if (ps.size() == 2) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if ((ps[0].first + ps[1].first) < ps[2].first) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    for (int i = 0; i < ps[0].first; i++) {
        for (int j = 0; j < 3; j++) {
            ans.push_back(ps[j].second);
        }
    }
    ps[1].first -= ps[0].first;
    ps[2].first -= ps[0].first;
    for (int i = 0; i < ps[1].first; i++) {
        for (int j = 1; j < 3; j++) {
            ans.push_back(ps[j].second);
        }
    }
    ps[2].first -= ps[1].first;
    while(ps[2].first > 0) {
        auto it = ans.begin();
        auto nxt = it + 1;
        while(nxt != ans.end()) {
            if ((*it != ps[2].second) && (*nxt != ps[2].second)) {
                ans.insert(nxt, ps[2].second);
                ps[2].first--;
                break;
            }
            nxt++; it++;
        }
    }
    for (char a : ans) {
        cout << a;
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    int i = 1;
    while (t--) {
        cout << "Case #" << i++ << ": ";
        solve_case();
    }
}
