#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    for (int l = 1; l <= n; l++) {
        cout << "Case #" << l << ": ";
        string s; cin >> s;
        int t; cin >> t;
        int flips = 0;
        bool flippable = true;
        for (int i = 0; i <= s.length() - t; i++) {
            if (s[i] == '-') {
                flips++;
                for (int j = i; j < i + t; j++) {
                    s[j] = (s[j] == '-') ? '+' : '-';
                }
            } 
        }

        for (int i = s.length() - t + 1; i < s.length(); i++) {
            if (s[i] == '-') {
                cout << "IMPOSSIBLE" << endl;
                flippable = false;
                break;
            }
        }

        if (flippable) {
            cout << flips << endl;
        }
    }
}
