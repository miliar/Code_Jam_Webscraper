#include <iostream>
using namespace std;
int main () {
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n;
        string s;
        cin >> s;
        n = s.length();
        for (int k = 0; k < n; k ++) {
            bool changed = 0;
            for (int i = 0; i < n; i ++)
                if (changed)
                    s[i] = '9';
                else if (i < n - 1 && s[i] > s[i + 1]) {
                    s[i]--;
                    changed = 1;
                }
        }
        int first = 0;
        while (s[first] == '0')
            ++first;
        cout << "Case #" << t << ": ";
        for (int i = first; i < n; i ++)
            cout << s[i];
        cout << endl;
    }
    return 0;
}
