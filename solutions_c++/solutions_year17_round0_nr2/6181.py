#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

string find(const string &s) {
    string res = "0";
    res += s;
    bool bad = false;
    for (int i = 1; i < res.size(); ++i) {
        if (bad) {
            res[i] = '9';
            continue;
        }
        if (res[i] < res[i - 1]) {
            int j = i;
            while (res[j] < res[j - 1]) {
                res[j] = '9';
                --res[j - 1];
                --j;
            }
            bad = true;
        }
    }
    reverse(res.begin(), res.end());
    while (res.size() > 1 && res.back() == '0') {
        res.pop_back();
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    int test;
    cin >> test;
    for (int tt = 0; tt < test; ++tt) {
        cout << "Case #" << tt + 1 << ": ";
        string s;
        cin >> s;
        cout << find(s) << "\n";
    }
    return 0;
}
