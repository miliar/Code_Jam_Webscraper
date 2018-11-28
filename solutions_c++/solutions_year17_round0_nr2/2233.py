#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int test;
string s;

int main () {
    freopen("input.txt" , "r" , stdin);
    freopen("output.txt" , "w" , stdout);
    cin >> test;

    for (int t = 1; t <= test; t++) {
        cout << "Case #" << t << ": ";
        cin >> s;
        int l = s.size();

        int p = -1;

        for (int i = 1; i < l; i++) {
            if (s[i] < s[i - 1]) {
                p = i - 1;
                break;
            }
        }

        if (p == -1) {
            cout << s << endl;
            continue;
        }

        while (s[p] == s[p - 1] && p) p--;

        if (p == 0 && s[0] == '1') {
            for (int i = 1; i < l; i++) cout << '9';
            cout << endl;
            continue;
        }

        for (int i = 0; i < p; i++) cout << s[i];
        cout << (char) (s[p] - 1);
        for (int i = p + 1; i < l; i++) cout << '9';
        cout << endl;
    }
    return 0;
}
