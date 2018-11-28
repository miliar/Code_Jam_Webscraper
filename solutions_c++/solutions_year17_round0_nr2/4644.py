#include <iostream>
#include <string>
using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        string str; cin >> str;
        for (int k = 0; k < str.length(); k++) {
            for (int j = 1; j < str.length() ; j++) {
                if (str[j - 1] > str[j]) {
                    str[j - 1]--;
                    for (j; j < str.length(); j++) {
                        str[j] = '9';
                    }
                }
            }
        }
        if (str[0] == '0') {
            str.erase(0, 1);
        }
        cout << "Case #" << i << ": " << str << endl;
    }
}

