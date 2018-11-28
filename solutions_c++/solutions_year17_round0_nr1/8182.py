#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t;
    string str, s;
    cin >> t;
    getline(cin, str);
    for (int i = 0; i < t; i++) {
        getline(cin, str);
        int space_loc = str.find_first_of(' ');
        s = str.substr(0, space_loc);
        size_t f = stoi(str.substr(space_loc + 1), nullptr);
        int count = 0;
        for (size_t k = 0, n = s.length(); k < n; k++) {
            if (s[k] == '-') {
                if (n - k >= f) {
                    count++;
                    for (size_t flips = 0; flips < f; flips++) {
                        s[k + flips] = s[k + flips] == '-' ? '+' : '-';
                    }
                } else {
                    cout << "Case #" << i + 1 << ": IMPOSSIBLE" << "\n";
                    break;
                }
            } else if (s[k] == '+' && k == n - 1){
                cout << "Case #" << i + 1 << ": " << count << "\n";
            }
        }
    }
    return 0;
}
