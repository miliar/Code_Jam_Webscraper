#include <iostream>
#include <string>
using namespace std;
void flip(string& s, int pos, int k) {
    for (int i = pos; i < pos + k; i++) {
        s[i] = (s[i] == '+' ? '-' : '+');
    }
}

void print(int testNum, const string& answer) {
    cout << "Case #" << testNum << ": " << answer << "\n";
}


int main(void) {
    int t;
    cin >> t;

    for (int testNum = 1; testNum <= t; testNum++) {
        string s;
        int k;
        cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '-') {
                cnt++;
                if (i + k > (int)s.size()) {
                    print(testNum, "IMPOSSIBLE");
                    break;
                }
                flip(s, i, k);
            }
            if (i == (int)s.size() - 1) {
                print(testNum, to_string(cnt));
            }
        }

    }
    return 0;
}
