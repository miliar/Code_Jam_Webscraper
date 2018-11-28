#include <iostream>

using namespace std;

string RemoveZeroes(string s) {
    while (s.size() > 1 && s[0] == '0')
        s = s.substr(1);
    return s;
}

void Solve() {
    long long x;
    cin >> x;
    string s = to_string(x);

    while (true) {
        int pos = -1;
        for (int i = 0; i < (int) s.size() - 1; ++i)
            if (s[i] > s[i + 1]) {
                pos = i;
                break;
            }
        if (pos == -1) {
            cout << RemoveZeroes(s);
            return;
        }

        --s[pos];
        for ( pos = pos + 1; pos < s.size(); ++pos)
            s[pos] = '9';
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        Solve();
        cout << endl;
    }
    return 0;
}
