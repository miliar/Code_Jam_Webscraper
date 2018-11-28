#include <cstddef>
#include <iostream>
#include <string>

using namespace std;

int solve(string s, size_t k)
{
    int ret = 0;
    size_t n = s.length();
    size_t steps = n + 1 - k;
    for (size_t i = 0; i < steps; ++i) {
        if (s[i] == '-') {
            for (size_t j = 0; j < k; ++j) {
                s[i + j] = (s[i + j] == '-') ? '+' : '-';
            }
            ++ret;
        }
    }
    for (size_t i = 0; i < k; ++i) {
        if (s[n - i - 1] == '-') {
            return -1;
        }
    }
    return ret;
}

int main()
{
    size_t t;
    cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        string s;
        size_t k;
        cin >> s >> k;
        int sol = solve(s, k);
        cout << "Case #" << i << ": ";
        if (sol == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << sol;
        }
        cout << endl;
    }
}

