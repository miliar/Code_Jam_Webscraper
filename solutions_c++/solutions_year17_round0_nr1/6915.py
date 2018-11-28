#include <iostream>

using namespace std;

void flip(string &s, int l, int k) {
    for (int i = l; i < l + k; i++) {
        if (s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
    }
}

int main() {
    int TN;

    cin >> TN;

    for (int TC = 0; TC < TN; TC++) {
        string s;
        int k;

        cin >> s >> k;

        int flipsCount = 0;
        for (int i = 0; i < s.length() - k + 1; i++) {
            if (s[i] == '-') {
                flip(s, i, k);
                flipsCount ++;
            }
        }

        bool hasMinus = 0;
        for (int i = s.length() - k; i < s.length(); i++)
            if (s[i] == '-')
                hasMinus = true;

        cout << "Case #" << (TC + 1) << ": ";
        if (hasMinus)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << flipsCount << endl;
    }
}

