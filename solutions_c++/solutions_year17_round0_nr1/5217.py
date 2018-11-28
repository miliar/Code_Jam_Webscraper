#include <iostream>
#include <bitset>
#include <string>

using namespace std;

typedef unsigned int uint;

int get_blank(string s, int start) {
    uint i = start;
    
    for (; i < s.size() && s[i] != '-'; i++);

    return i;
}


int main() {
    int t;
    string  s;
    int k = 0;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> s >> k;
        // for (uint j = 0; j < s.size(); ++j)
        //     s[j] = (s[j] == '+') ? '1' : '0';

        uint x = get_blank(s, 0);
        uint count = 0;

        while (x + k <= s.size()) {
            for (uint j = x; j < x + k; j++) {
                s[j] = (s[j] == '-') ? '+' : '-';
            }
            count++;
            x = get_blank(s, x + 1);
            // cout << s << ' ' << x << '\n';
        }

        cout << "Case #" << i + 1 << ": ";
        if (x == s.size()) {
            cout << count;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << '\n';
    }
}
