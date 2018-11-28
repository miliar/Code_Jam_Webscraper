#include<iostream>
#include<algorithm>
#include<cstdlib>
using namespace std;


string s;

void read() {
    cin >> s;
}


void work(int cases) {
    int noDecrease = true;
    for (int i = 0; i + 1 < s.size(); ++i) {
        if (s[i] > s[i + 1]) {
            noDecrease = false;
            break;
        }
        
    }
    if (noDecrease) {
        cout << "Case #" << cases << ": " << s << endl;
        return;
    }

    string ans;
    ans = string(s.size() - 1, '9');
    
    if (s[0] > '1') {
        ans = (char)(s[0] - 1) + string(s.size() - 1, '9');
    }
    
    for (int i = 0; i + 1 < s.size(); ++i) {
        if (s[i] < s[i + 1]) {
            ans = s.substr(0, i + 1) + (char)(s[i + 1] - 1) + string(s.size() - i - 2, '9');
        } else if (s[i] > s[i + 1]) {
            break;
        }
    }
    
    cout << "Case #" << cases << ": " << ans << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
