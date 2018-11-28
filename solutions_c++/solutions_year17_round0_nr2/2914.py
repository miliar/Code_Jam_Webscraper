#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    srand(time(0));

#ifdef HOME
    freopen("/home/acarus/input.txt", "r", stdin);
    freopen("/home/acarus/output.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    for (int test_case = 1; test_case <= t; ++test_case) {
        string s;
        cin >> s;

        for (int i = s.size() - 2; i >= 0; --i) {
            if (s[i] > s[i + 1]) {
                --s[i];
                for (int j = i + 1; j < s.size(); ++j) s[j] = '9';
            }
        }
        cout << "Case #" << test_case << ": ";
        int pos = 0;
        while (pos < s.size() && s[pos] == '0') ++pos;
        while (pos < s.size()) cout << s[pos++];
        cout << endl;
    }
    return 0;
}