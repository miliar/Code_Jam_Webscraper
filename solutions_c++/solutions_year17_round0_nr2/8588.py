#include <iostream>
#include <string>

using namespace std;

char set9char (char c) { return '9'; }

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    
    for (int t = 0; t < T; t++) {
        long long n;
        cin >> n;
        
        string s = to_string(n);
        if (s.length() == 2) {
            if (s[1] < s[0]) {
                s[1] = '9';
                s[0]--;
            }
        } else if (s.length() > 2) {
            bool decrease_next = false;
            for (size_t i = s.length() - 1; i > 0; i--) {
                if (decrease_next) {
                    decrease_next = false;
                    if (s[i - 1] != '0') {
                        s[i - 1]--;
                    } else {
                        s[i - 1] = '9';
                        decrease_next = true;
                    }
                    if (s[i] != '9')
                        transform(s.begin() + i, s.end(), s.begin() + i, set9char);
                        //for (size_t j = i; j < s.length(); j++) s[j] = '9';
                } else if (s[i - 1] > s[i]) {
                    if (s[i - 1] != '0') {
                        s[i - 1]--;
                    } else {
                        s[i - 1] = '9';
                        decrease_next = true;
                    }
                    if (s[i] != '9')
                        transform(s.begin() + i, s.end(), s.begin() + i, set9char);
                        //for (size_t j = i; j < s.length(); j++) s[j] = '9';
                }
            }
        }
        cout << "Case #" << (t + 1) << ": " << stoll(s) << endl;
    }
    
    return 0;
}
