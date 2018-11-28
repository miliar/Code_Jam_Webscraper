#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() {
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    int n;
    cin >> n;

    for (int test = 1; test <= n; test++) {
        cout << "Case #" << test << ": ";

        string s;
        cin >> s;
        int k;
        cin >> k;

        int count = 0;
        for (int i = 0; i < s.size() - k + 1; i++) {
            if (s[i] == '-') {
                count++;
                for (int j = i; j < i + k; j++) {
                    s[j] = (s[j] == '+') ? '-' : '+';
                }
                // cerr << i << s << endl;
            }
        }


        bool impossible = false;
        for (int i = s.size() - k; i < s.size(); i++) {
            if (s[i] == '-') {
                impossible = true;
                break;
            }
        }

        if (impossible) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << count << endl;
        }

        getline(cin, s);
    }
}