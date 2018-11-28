#include <iostream>
#include <string>
using namespace std;

int T;
string str;

int main() {
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> str;
        int len = str.length();
        for (int i = 0; i < len-1; i++) {
            if (str[i] > str[i+1]) {
                int k;
                for (int j = i; j >= 0; j--) {
                   if (str[i] == str[j])
                       k = j;
                }
                str[k]--;
                for(int j = k+1; j < len; j++)
                    str[j] = '9';
                break;
            }
        }
        int k = 0;
        for (int i = 0; i < len; i++)
            if (str[i] != '0') {
                k = i;
                break;
            } 
        cout << "Case #" << t+1 << ": ";
        for (int i = k; i < len; i++)
            cout << str[i];
        cout << endl;
    }
    return 0;
}
