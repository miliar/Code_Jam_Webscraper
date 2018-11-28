#include "bits/stdc++.h"

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cout.precision(10);

    srand(unsigned(time(NULL)));

    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);

    int Tcase;
    cin >> Tcase;
    for (int test = 1; test <= Tcase; ++test) {
        string s;
        cin >> s;
        bool fl = true;
        while (fl) {
            fl = false;
            for (int i = 0; i < s.size() - 1; ++i) {
                if (s[i] > s[i + 1]) {
                    s[i] = (char) (s[i] - 1);
                    fl = true;
                    while (++i < s.size())
                        s[i] = '9';
                }
            }
        }
        if(s[0] == '0') {
            int x = (int) (s.size() - 1);
            s.clear();
            while (x--)
                s.push_back('9');
        }
        cout << "Case #" << test << ": " << s << "\n";
    }

}

