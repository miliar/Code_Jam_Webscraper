#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <map>

using namespace std;

long long n,k;
map<long long, long long> m;

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        cin >> n >> k;
        m.clear();
        m[n] = 1;

        k--;
        while (k > 0) {
            long long x = m.rbegin() -> first;
            k -= m[x];
            if (k < 0) break;
            if (x % 2 == 0) {
                m[x/2-1] += m[x];
                m[x/2] += m[x];
            } else {
                m[x/2] += 2 * m[x];
            }
            m.erase(x);
        }

        cout << "Case #" << TC << ": ";
        long long x = m.rbegin() -> first;
        cout << x/2 << ' ' << (x-1)/2 << '\n';
    }
}
