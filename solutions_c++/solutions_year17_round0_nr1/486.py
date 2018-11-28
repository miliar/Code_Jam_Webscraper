/* Task solution for GCJ 2017
 * Tested with GCC 5.4.0
 * Build command line:
 *  g++ -std=gnu++14 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int m = 0;
        queue<int> q;
        bool r = true;
        for (int i = 0; i < n; ++i) {
            if (!q.empty() && q.front() == i) {
                r = !r;
                q.pop();
            }
            if ((s[i] == '+') != r) {
                if (i + k <= n) {
                    r = !r;
                    q.push(i + k);
                    ++m;
                } else {
                    m = -1;
                    break;
                }
            }
        }
        cout << "Case #" << T << ": ";
        if (m >= 0) {
            cout << m;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
