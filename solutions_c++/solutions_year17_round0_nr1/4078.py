#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#define REP(i, n) for(int i = 0; i < n; ++i)
#define RANGE(i, x, n) for(int i = x; i < n; ++i)
using namespace std;

const int MAX_N = 1e3 + 1;
int f[MAX_N];

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    REP(p, T) {
        memset(f, 0, sizeof f);
        string s;
        int K;
        cin >> s >> K;
        int sum = 0, res = 0;
        for(int i = 0; i + K - 1 < s.size(); ++i) {
            if((s[i] == '+' && sum % 2 == 1) || (s[i] == '-' && sum % 2 == 0)) {
                ++res;
                f[i] = 1;
            }
            sum += f[i];
            if(i - K + 1 >= 0) {
                sum -= f[i - K + 1];
            }
        }
        RANGE(i, s.size() - K + 1, s.size()) {
            if((s[i] == '+' && sum % 2 == 1) || (s[i] == '-' && sum % 2 == 0)) {
                res = -1;
                break;
            }
            if(i - K + 1 >= 0) {
                sum -= f[i - K + 1];
            }
        }
        if(res == -1) {
            cout << "Case #" << p+1 << ": IMPOSSIBLE" << endl;
        }else {
            cout << "Case #" << p+1 << ": " << res << endl;
        }
    }
}
