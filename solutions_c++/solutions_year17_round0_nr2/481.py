/* Task solution for GCJ 2017
 * Tested with GCC 5.4.0
 * Build command line:
 *  g++ -std=gnu++14 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        string S;
        cin >> S;
        char *s = const_cast<char*>(S.c_str());
        char *p = s;
        while (p[0] <= p[1]) {
            ++p;
        }
        if (p[1]) {
            while (p > s && p[0] == p[-1]) {
                --p;
            }
            --p[0];
            while (*++p) {
                p[0] = '9';
            }
        }
        while (s[0] == '0') {
            ++s;
        }
        if (!s[0]) {
            --s;
        }
        cout << "Case #" << T << ": " << s << endl;
    }
    return 0;
}
