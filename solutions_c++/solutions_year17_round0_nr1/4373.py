#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;

const int inf = 1 << 30;

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        string str;
        cin >> str;
        int K;
        cin >> K;
        int ans = inf;

        vector<int> v(str.size());
        REP (i, 0, v.size()) v[i] = (str[i] == '+' ? 1 : 0);

        REP(__, 0, 2) {
            vector<int> temp = v;
            int cnt = 0;
            REP (i, 0, v.size() - K + 1) {
                if (temp[i] == 0) {
                    REP (j, i, i + K) {
                        temp[j] = 1 - temp[j];
                    }
                    cnt++;
                }
            }
            int check = 0;
            REP (i, 0, v.size()) {
                check += temp[i];
            }
            if (check == v.size()) ans = min(ans, cnt);
            reverse(v.begin(), v.end());
        }

        cout << "Case #" << _ + 1 << ": ";
        if (ans == inf) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }

    }
    return 0;
}
