#include <iostream>
#include <string>
using namespace std;

int main()  {
    int T;
    cin >> T;
    for (int ti = 0; ti < T; ti++) {
        cout << "Case #" << ti+1 << ": ";
        string s;
        cin >> s;
        int j = -1;
        for (int i=0; i<s.length()-1; i++) {
            if (s[i] > s[i+1]) {
                j = i;
                break;
            }
        }
        if (j != -1) {
            s[j]--;
            while ((j>0) && (s[j] < s[j-1])) {
                j--;
                s[j]--;
            }
            if (j > 0) {
                for (int k=j+1; k<s.length(); k++) {
                    s[k] = '9';
                }
                cout << s << endl;
            } else {
                if (s[0] > '0') {
                    cout << s[0];
                }
                for (int k=0; k<s.length()-1; k++) {
                    cout << 9;
                }
                cout << endl;
            }
        } else {
            cout << s << endl;
        }
    }
}
