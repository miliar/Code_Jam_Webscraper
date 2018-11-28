#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int T, n, k, ans;
string s;

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        cin >> s >> k;
        ans = 0;
        for (unsigned i = 0; i < s.length() - k + 1; i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = i; j < i + k; j++) {
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        for (unsigned i = s.length() - k; i < s.length(); i++) {
            if (s[i] == '-') {
                ans = -1;
                break;
            }
        }
        cout << "Case #" << id << ": ";
        if (ans == -1) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
}
