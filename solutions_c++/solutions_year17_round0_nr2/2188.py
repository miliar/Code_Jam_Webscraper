#include <iostream>
#include <string>

typedef long long ll;

using namespace std;

void subtract_one(string &s, int i) {
    if (s[i] == '0') {
        s[i] = '9';

        if (i > 0) {
            subtract_one(s, i - 1);
        }
    }
    else {
        s[i]--;
    }
}

void fixup(string &s, int i) {
    s[i] = '9';

    subtract_one(s, i - 1);        
    
    if (i > 0) {
        if (s[i - 1] < s[i - 2]) {
            fixup(s, i - 1);
        }
    }
}

int main() {
    int T;
    
    cin >> T;

    for (int t = 1; t <= T; t++) {
        ll num;

        cin >> num;

        string num_str = to_string(num);

        for (int i = 1; i < num_str.size(); i++) {
            if (num_str[i] < num_str[i - 1]) {
                fixup(num_str, i);

                for (int j = i + 1; j < num_str.size(); j++) {
                    num_str[j] = '9';
                }

                break;
            }
        }
       
        ll ans = 0;

        for (int i = 0; i < num_str.size(); i++) {
            ans = (ans * 10) + (num_str[i] - '0');
        }

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
