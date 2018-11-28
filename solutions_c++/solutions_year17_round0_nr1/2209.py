#include <iostream>
#include <string>

using namespace std;

char flip(char c) {
    if (c == '+') {
        return '-';
    }

    return '+';
}

int main() {
    int T;

    cin >> T;

    for (int t = 1; t <= T; t++) {   
        string s;
        int k;
        int num_flips = 0;
        bool possible = true;

        cin >> s >> k;

        for (int i = 0; i <= s.size() - k; i++) {
            if (s[i] == '-') {
                num_flips++;
                for (int j = 0; j < k; j++) {
                   s[i + j] = flip(s[i + j]);
                } 
            }
        }

        for (int i = s.size() - k + 1; i < s.size(); i++) {
            if (s[i] == '-') {
                possible = false;
                break;
            }
        }
    
        cout << "Case #" << t << ": ";
        
        if (possible) {
            cout << num_flips;
        }
        else {
            cout << "IMPOSSIBLE";
        }

        cout << endl;
    }

    return 0;
}
