#include <iostream>
#include <string>

using namespace std;

int T, TOT;

char flip(char c) {
    return c == '+' ? '-' : '+';
}

void panquequear(string &s, int i, int k) {
    for (int j = i; j < i+k; j++) {
        s[j] = flip(s[j]);
    }
}

int main() {
    cin >> T;
    TOT = T;

    int rta = 0;
    string s;
    int k;

    while (T--) {
        cin >> s;
        cin >> k;

        int n = (int)s.size();

        int panquequeadas = 0;

        for (int i = 0; i <= n-k; i++) {
            if (s[i] == '-') {
                panquequear(s, i, k);
                panquequeadas++;            
            }
        }

        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                panquequeadas = -1;
                    break;
            }
        }
        
        if (panquequeadas == -1) {
            cout << "Case #" << TOT - T << ": " << "IMPOSSIBLE" << "\n";
        } else {
            cout << "Case #" << TOT - T << ": " << panquequeadas << "\n";
        }
    }



    return 0;
}