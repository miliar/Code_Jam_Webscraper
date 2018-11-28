
/*

 'Tiocfaidh ár lá'

 */

#include <bits/stdc++.h>

using namespace std;

bool tidy(string s) {
    for(int i = 0; i < s.size() - 1; i++) {
        if(s[i] > s[i + 1]) return false;
    }
    return true;
}

int main() {

    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        string n;
        cin >> n;
        bool valid = true;
        while(!tidy(n)) {
            for(int i = 0; i < n.size() - 1; i++) {
                if(n[i] > n[i + 1]) {
                    n[i]--;
                    for(int j = i + 1; j < n.size(); j++) {
                        n[j] = '9';
                    }
                }
                if(n[i] == '0' && i == 0) {
                    string answer = "";
                    for(int j = 0; j < n.size() - 1; j++) answer += "9";
                    cout << "Case #" << t << ": " << answer << endl;
                    valid = false;
                    break;
                }
            }
            if(!valid) break;
        }
        if(valid) cout << "Case #" << t << ": " << n << endl;
    }

    return 0;
}