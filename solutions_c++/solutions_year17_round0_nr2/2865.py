#include <iostream>
#include <string>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    for (int c = 1; c <= tc; ++c) {
        string str;
        cin >> str; 
        int p = 0;
        for (; p + 1 < str.size(); ++p) {
            if (str[p] > str[p + 1]) {
                break;
            }
        }
        cout << "Case #" << c << ": ";
        if (p + 1 == str.size()) {
            cout << str << endl;
        } else {
            for (; p > 0 && str[p - 1] == str[p]; --p);
            --str[p];
            for (++p; p < str.size(); ++p) {
                str[p] = '9';
            }
            if (str[0] == '0') {
                str = str.substr(1, str.size() - 1);
            }
            cout << str << endl;
        }
    }
    return 0;
}