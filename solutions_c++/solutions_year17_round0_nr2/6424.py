#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int cse = 1; cse <=T; cse++) {
        string s;
        cin >> s;

        cout << "Case #"  << cse << ": ";
        if (s.size() == 1) {
            cout << s[0] << endl;
        } else {
            for (int i = 1; i < s.size(); i++) {
                if (s[i] < s[i-1]) {
                    for (int j = i; j < s.size(); j++)                      
                        s[j] = '9';
                    s[i-1] = s[i-1] - 1;
                    for (int j = i-1; j >=1; j--) {
                        if (s[j] >= s[j-1]) break;
                        else {
                            s[j-1] = s[j];
                            s[j] = '9';
                        }
                    }
                    break;
                }
            }
            int j = 0;
            while (s[j] == '0') j++;
            for (; j < s.size(); j++) {
                cout << s[j];
            }
            cout << endl;
        }
    }
    return 0;
}
