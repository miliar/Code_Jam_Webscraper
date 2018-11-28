#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

#define FU(i, a, b) for (auto i = (a); i < (b); ++i)
#define fu(i, b) FU(i, 0, b)
#define FD(i, a, b) for (auto i = (b) - 1; i >= (a); --i)
#define fd(i, b) FD(i, 0, b)
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb emplace_back

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        bool ok = false;
        while (!ok) {
            ok = true;
            for (int i = 0, e = s.size(); i < e - 1; ++i) {
                if (s[i] > s[i+1]) {
                    --s[i];
                    while (++i < e)
                        s[i] = '9';
                    ok = false;
                    break;
                }
            }
        }
        int i = 0;
        while (s[i] == '0')
            ++i;
        cout << "Case #" << t << ": ";
        for (int e = s.size(); i < e; ++i)
            cout << s[i];
        cout << endl;
    }
    return 0;
}
