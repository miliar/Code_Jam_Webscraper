#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {

    int t, n;
    std::string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> s >> n;  // read s and then n.

        bool * pancake_up_side_down = new bool[s.length()];

        for (int j = 0; j < s.length(); ++j) {
            if (s[j] == '-') {
                pancake_up_side_down[j] = true;
            } else {
                pancake_up_side_down[j] = false;
            }
        }

        int count = 0;
        for (int u = 0; u < s.length(); ++u) {
            if (pancake_up_side_down[u] && (u + n-1 < s.length()) ) {
                ++count;
                for (int i = u ; i < n+u ; ++i) {
                    pancake_up_side_down[i] = !pancake_up_side_down[i];
                }
            }
        }

        int j = 0;
        for (j = 0; j < s.length(); ++j) {
            if (pancake_up_side_down[j]) {
                cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                break;
            }
        }

        if (j == s.length()) {
            cout << "Case #" << i << ": " << count << endl;
        }
    }
}

