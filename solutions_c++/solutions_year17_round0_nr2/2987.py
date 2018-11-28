#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        string s;
        cin >> s;
        for (int i = s.size()-2; i >= 0; i--) {
            if (s[i] > s[i+1]) {
                for (int j = i+1; j < s.size(); j++) {
                    s[j] = '9';
                }
                s[i] = s[i]-1;
            }
        }
        if (s[0] == '0') {
            s = s.substr(1);
        }
        cout << s << "\n";
    }
}
