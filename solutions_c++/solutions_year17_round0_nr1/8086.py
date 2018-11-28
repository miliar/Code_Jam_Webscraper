#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int _ = 1; _ <= t; _++) {
        string s;
        int k;
        cin >> s;
        cin >> k;
        int count = 0;
        int pos = s.size() - 1;
        while (s[pos] == '+') {
            pos--;
        }
        // pos stands at first '-'
        while (pos + 1 >= k) {
            int it = pos;  // iterator
            for (int __ = 1; __ <= k; __++) {
                s[it] = (s[it] == '+') ? '-' : '+';
                it--;
            }
            count++;
            // move pos to next '-'
            while (s[pos] == '+') {
                pos--;
            }
        }
        if (pos < 0) {
            cout << "Case #" << _ << ": " << count << endl;
        } else {
            cout << "Case #" << _ << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}