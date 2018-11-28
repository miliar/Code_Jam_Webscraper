#include <iostream>
#include <string>

using namespace std;

int main() {
        size_t testnum;
        cin >> testnum;
        for (size_t test {1}; test <= testnum; ++test) {
                cout << "Case #" << test << ": ";
                string s;
                size_t k;
                cin >> s >> k;
                int cnt {0};
                for (size_t i {0}; i < s.length(); ++i) {
                        if (s[i] == '+') continue;
                        size_t j {i + k};
                        if (j > s.length()) {
                                cout << "IMPOSSIBLE" << endl;
                                cnt = -1;
                                break;
                        }
                        for (size_t l {i}; l < j; ++l) {
                                if (s[l] == '+')
                                        s[l] = '-';
                                else
                                        s[l] = '+';
                        }
                        ++cnt;
                }
                if (cnt >= 0)
                        cout << cnt << endl;
        }
        return 0;
}