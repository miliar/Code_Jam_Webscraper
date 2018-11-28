#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void print(int testNum, const string& answer) {
    cout << "Case #" << testNum << ": " << answer << "\n";
}

string repeat(int sym, int size) {
    string s;
    for (int i = 0; i < size; i++) {
        s.push_back(sym);
    }
    return s;
}


int main(void) {
    int t;
    cin >> t;

    for (int testNum = 1; testNum <= t; testNum++) {
        string s;
        cin >> s;
        int lastTrouble = s.size();
        for (int i = 0; i < (int)s.size() - 1; i++) {
            if (s[i] > s[i + 1]) {
                lastTrouble = i;
                break;
            }
        }
        if (lastTrouble == (int)s.size()) {
            print(testNum, s);
        } else {
            int was = 0;
            for (int i = (int)s.size() - 1; i >= 0; i--) {
                if (lastTrouble >= i) {
                    if ((i == 0 && s[i] > '1') || (i > 0 && s[i] > s[i - 1])) {
                        s[i]--;
                        for (int j = i + 1; j < (int)s.size(); j++) {
                            s[j] = '9';
                        }
                        print(testNum, s);
                        was = 1;
                        break;
                    }
                }
            }
            if (!was) {
                print(testNum, repeat('9', (int)s.size() - 1));
            }
        }
    }
    return 0;
}
