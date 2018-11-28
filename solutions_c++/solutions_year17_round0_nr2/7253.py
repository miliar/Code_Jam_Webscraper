#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("tidynumbers.in", "r", stdin);
    freopen("tidynumbers.out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        string s;

        cin >> s;
        cout << "Case #" << i << ": ";

        int pos = -1;
        for (int j = 0; j < s.size()-1; j++) {

            if (s[j] > s[j+1]) {
                pos = j;
                break;
            }

        }

        if (pos == -1) {
            cout << s << endl;
            continue;
        }

        while ((s[pos] == s[pos-1]) && (pos > 0))
            pos--;

        if ((pos == 0) && (s[pos] == '1')) {
            for (int j = 0; j < s.size()-1; j++)
                cout << "9";
            cout << endl;
            continue;
        }

        if (pos == 0) {
            cout << (char)(s[pos]-1);
            for (int j = 0; j < s.size()-1; j++)
                cout << "9";
            cout << endl;
            continue;
        }

        for (int j = 0; j < pos; j++)
            cout << s[j];
        cout << (char)(s[pos]-1);
        for (int j = (pos+1); j < s.size(); j++)
            cout << "9";

        cout << endl;
    }

    return 0;
}
