#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<bool> makediff(const string s) {
    vector<bool> ret(s.size());
    char last = '+';
    for (int i = 0; i < s.size(); i++) {
        if (last != s[i]) ret[i] = true;
        else ret[i] = false;
        last = s[i];
    }
    return ret;
}

bool flip(vector<bool> &diff, int pos, int k) {
    diff[pos] = !diff[pos];
    if (pos + k > diff.size()) return false;
    if (pos + k < diff.size()) diff[pos + k] = !diff[pos + k];
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int II = 1; II <= T; II++) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        vector<bool> diff = makediff(s);
        bool res = true;
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (diff[i]) {
                res = res && flip(diff, i, k);
                count++;
            }
        }
        if (res) printf("Case #%d: %d\n", II, count);
        else printf("Case #%d: IMPOSSIBLE\n", II);
    }
    return 0;
}
