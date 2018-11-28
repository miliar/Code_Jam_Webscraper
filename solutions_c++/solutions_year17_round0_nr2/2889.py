#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Q
{
    uint32_t    m_ntc;
public:
    int main();
private:
    void solve(uint32_t tcnum);
};

int Q::main()
{
    uint32_t i;
    cin >> m_ntc;
    for (i = 1; i <= m_ntc; ++i) {
        solve(i);
    }
    return 0;
}

void Q::solve(uint32_t tcnum)
{
    string s;
    cin >> s;
    int32_t slen = (int32_t)s.size();

    int32_t i;
    for (i = 0; i < slen - 1; ++i) {
        if (s[i] > s[i + 1]) {
            break;
        }
    }
    if (i < (slen - 1)) {
        bool first_fill = true;
        for (; i >= 0; --i) {
            if (s[i] <= s[i + 1]) {
                break;
            }
            --s[i];
            if (first_fill) {
                first_fill = false;
                fill(s.begin() + i + 1, s.end(), '9');
            }
            else {
                s[i + 1] = '9';
            }
        }
    }

    cout << "Case #" << tcnum << ": ";
    if (s[0] != '0') {
        cout << s[0];
    }
    for (i = 1; i < slen; ++i) {
        cout << s[i];
    }
    cout << "\n";
}

int
main()
{
    return Q().main();
}
