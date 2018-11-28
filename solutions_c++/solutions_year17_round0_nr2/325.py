#include <cstdint>
#include <iostream>
#include <sstream>
#include <stdio.h>
using namespace std;

void solve()
{
    string s;
    cin >> s;

    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i + 1 < s.size(); i++) {
            if (s[i] > s[i + 1]) {
                s[i]--;
                for (int j = i + 1; j < s.size(); j++) {
                    s[j] = '9';
                }
                changed = true;
                break;
            }
        }
    }

    istringstream iss(s);
    int64_t ans;
    iss >> ans;
    printf("%ld\n", ans);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
