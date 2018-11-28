#include <iostream>
#include <string>

using namespace std;
int T;

void decrement(string &s) {
    for(int i = s.size()-1; i >= 0; i--) {
        if(s[i] > '0') {
            s[i]--;
            break;
        } else {
            s[i] = '9';
        }
    }
    while(s[0] == '0') {
        s.erase(s.begin());
    }
}

string solve(string s) {
    //cerr << "Solving " << s << "\n";
    if(!s.size()) {
        return "";
    }
    // Is there a zero?
    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '0') {
            // There is a zero, need to do some weird stuff
            string remains = s.substr(0, i);
            //cerr << "Decrementing remains " << remains << "\n";
            decrement(remains);
            //cerr << "Decremented remains " << remains << "\n";
            string ans = solve(remains);
            for(int j = i; j < s.size(); j++) {
                ans += '9';
            }
            while(ans.size() && ans[0] == '0') {
                ans.erase(ans.begin());
            }
            return ans;
        }
    }
    // Phew! No zeroes
    // Find the first deviant digit
    int deviant = s.size()+1;
    for(int i = 0; i < s.size()-1; i++) {
        int who = i+1;
        while(who < s.size()-1 && s[i] == s[who]) {
            who++;
        }
        if(s[i] > s[who]) {
            deviant = i;
            break;
        }
    }

    string ans;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '0') {
            break;
        }
        if(i < deviant) {
            ans += s[i];
        } else if(i == deviant) {
            ans += char(s[i]-1);
        } else {
            ans += '9';
        }
    }
    while(ans.size() && ans[0] == '0') {
        ans.erase(ans.begin());
    }
    return ans;
}

int main() {
    cin >> T;
    string s;
    for(int t = 1; t <= T; t++) {
        cin >> s;
        cout << "Case #" << t << ": ";
        string ans = solve(s);
        cout << ans << "\n";
    }
}
