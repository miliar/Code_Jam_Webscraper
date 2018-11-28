#include <bits/stdc++.h>

using namespace std;

bool not_happy(string s) {
    return (s.find("-") != -1);
}

bool flip_once(string &s, int &c, int k) {
    c++;
    int first = s.find("-");

    if ((first + k) > s.size())
        return false;

    for (int j = first; j < (k + first); ++j)
        s[j] = (s[j] == '+') ? '-' : '+';

    return true;
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        // scan input
        string s;
        int k;
        cin >> s;
        cin >> k;
        // process input
        int c = 0;
        bool hope;
        string ans = "0";

        while (not_happy(s)) {
            hope = flip_once(s, c, k);
            ans = to_string(c);

            if (!hope) {
                ans = "IMPOSSIBLE";
                break;
            }
        }

        // print answer
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}

