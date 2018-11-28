#include <bits/stdc++.h>
using namespace std;

#define ifthen(x, y, z) (x ? y: z)
#define mp make_pair
#define mt make_tuple

const int INF = 1e9 + 1;
const double pi = acos(-1);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.precision(20);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        cout << "Case #" << i+1 << ": ";
        
        bool flag = true;
        while (flag) {
            int prev = -1;
            flag = false;
            for (int j = 0; j < s.size(); ++j) {
                if (s[j] < prev) {
                    flag = true;
                    s[j-1] -= 1;
                    for (int k = j; k < s.size(); ++k)
                        s[k] = '9';
                }
                prev = s[j];
            }
        }
        flag = false;
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] > '0' or flag) {
                flag = true;
                cout << s[j];
            }
        }
        cout << '\n';
    }
    return 0;
}
