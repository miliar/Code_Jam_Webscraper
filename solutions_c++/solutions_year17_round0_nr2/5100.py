#define pB
#ifdef pB

#include <iostream>
#include <string>
using namespace std;

int main() {
    int tc,count=0;
    cin >> tc;

    while (tc--) {
        string s; cin >> s;
        int i = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] <= s[i + 1])
                continue;

            else {
                if (s[i] != '0') {
                    s[i] -= 1;
                    for (int j = i + 1; j < s.size(); j++)
                        s[j] = '9';
                }
                else {
                    for (int j = i; j < s.size(); j++)
                        s[j] = '9';
                }
                i -= 2;
                while (s[0] == '0') {
                    s = s.substr(1, s.size()-1);
                }
            }
        }
        cout << "Case #" << ++count << ": " << s << endl;

    }

    return 0;
}

#endif
