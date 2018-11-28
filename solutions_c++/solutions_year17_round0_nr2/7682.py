#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        vector<int> n(s.size());
        vector<int> maxd(s.size());
        n[0] = s[0] - '0';
        maxd[0] = n[0];
        for (int i = 1; i < s.size(); i++) {
            n[i] = s[i] - '0';
            maxd[i] = max(maxd[i-1], n[i]);
        }

        int j = 1;
        while (j < s.size()) {
            if (n[j] < n[j-1])
                break;
            j++;
        }

        for (int i = n.size() - 1; i >= j; i--) {
            n[i] = 9;
            n[i-1] = max(0, n[i-1] - 1);
        }
        for (int i = j - 1; i > 0; i--) {
            if (n[i] < maxd[i-1]) {
                n[i] = 9;
                n[i-1] = max(0, n[i-1] - 1);
            }
        }

        int i = 0;
        printf("Case #%d: ", t);
        for (; i < n.size(); i++)
            if (n[i] != 0)
                break;
        for (; i < n.size(); i++)
            cout << n[i];
        cout << endl;
    }
    return 0;
}
