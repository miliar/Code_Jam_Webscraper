#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; ++i) {
        string chars;
        int k;
        cin >> chars;
        cin >> k;
        bool success = true;
        int flips = 0;
        for (int j = 0; j < chars.length(); ++j) {
            if (chars[j] == '-') {
                if (j + k > chars.length()) {
                    success = false;
                    break;
                }
                for (int m = 0; m < k; ++m) {
                    if (chars[j + m] == '-') {
                        chars[j + m] = '+';
                    }
                    else {
                        chars[j + m] = '-';
                    }
                }
                ++flips;
            }
        }
        if (success) {
            cout << "Case #" << i+1 << ": " << flips << endl;
        }
        else {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
