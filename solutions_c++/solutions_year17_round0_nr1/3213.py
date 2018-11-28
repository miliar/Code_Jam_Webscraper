#include <bits/stdc++.h>
#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)

using namespace std;

int main() {
    int T;
    cin >> T;
    fin(I, T) {
        string s;
        int k;
        cin >> s >> k;
        int n = s.size();
        vector<bool> t(n);
        fin(i, n) t[i] = s[i] == '+';        
        cout << "Case #" << I + 1 << ": ";
        int m = 0;
        fin(i, n) {
            if (!t[i]) {
                if (i + k - 1 >= n) {
                    cout << "IMPOSSIBLE" << endl;
                    m = -1;
                    break;
                }
                fin2(j, i, i + k) t[j] = !t[j];
                m++;
            }
        }
        if (m >= 0) cout << m << endl;
    }
}
