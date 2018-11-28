#include <set>
#include <map>
#include <vector>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

void solve(int cs) {
    cout << "Case #" << cs << ": ";
    int n, R, Y, B, T;
    cin >> n >> R >> T >> Y >> T >> B >> T;
    if (R > Y + B or Y > B + R or B > Y + R) {
       cout << "IMPOSSIBLE" << endl;
       return; 
    }
    string s = string(n, '0');
    char last = '0';
    for (int i = 0; i < n; ++i) {
       vector < pair <int, char> > h;
       h.push_back(make_pair(R, 'R'));
       h.push_back(make_pair(Y, 'Y'));
       h.push_back(make_pair(B, 'B')); 
       sort(h.begin(), h.end());
       for (int j = h.size() - 1; j >= 0; --j) {
           if (h[j].second != last) {
               s[i] = h[j].second;
               if (h[j].second == 'R') {
                   R--;
               } else if (h[j].second == 'B') {
                   B--;
               } else {
                   Y--;
               }
               last = h[j].second;
               break;
           }
       }
    }
    if (s[0] == s[n - 1]) {
        swap(s[n - 1], s[n - 2]);
    }
    cout << s;
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}
