#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<string, int> mp(1024);
int min_step = INT_MAX;

int cal(const string &s, int k, int cnt) {
    if (all_of(s.begin(), s.end(), [](char ch) { return ch == '+'; })) {
        if (cnt < min_step) {
            min_step = cnt;
        }
        return cnt;
    }
    if (cnt >= min_step || cnt > k * s.size()) {
        return -1;
    }
    if (mp.find(s) == mp.end() || mp[s] > cnt) {
        mp[s] = cnt;
    } else {
        return -1;
    }
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {

            for (int j = max(0, i - k + 1); j <= min(i, (int) s.size() - k); ++j) {
                string tmp(s);
                for_each(tmp.begin() + j, tmp.begin() + j + k, [](char &ch) { ch = (ch == '+' ? '-' : '+'); });
                int ret = cal(tmp, k, cnt + 1);
                if (ret != -1 && ret < min_step) {
                    min_step = ret;
                }
            }
        }
    }
    if (min_step == INT_MAX) {
        return -1;
    }
    return min_step;

}

int main() {

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        s.reserve(1000);
        int k;
        cin >> s >> k;
        mp.clear();
        min_step = INT_MAX;
        cal(s, k, 0);
        if (min_step == INT_MAX) {
            cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << (i + 1) << ": " << min_step << endl;
        }
    }

    return 0;
}