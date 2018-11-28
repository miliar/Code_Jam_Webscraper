#include <iostream>
#include <string>

#define N 1001

using namespace std;

int main() {

    int t;
    cin >> t;

    string s;
    int line[N];
    int k;
    for (int l = 0; l < t; l++) {
        cin >> s >> k;
        for (int i = 0; i < s.length(); i++)
            line[i] = (s.at(i) == '+') ? 1 : -1;
        
        int moves = 0;
        for (int i = 0; i < s.length(); i++) {
            if (line[i] == -1 and i + k <= s.length()) {
                for (int j = i; j < i + k; j++)
                    line[j] *= -1;
                moves++;
            }
        }

        bool solved = true;
        for (int i = 0; i < s.length(); i++)
            if (line[i] == -1) {
                solved = false;
                break;
            }
        
        if (solved) 
            cout << "Case #" << (l+1) << ": " << moves << endl;
        else
            cout << "Case #" << (l+1) << ": IMPOSSIBLE" << endl;

    }

    return 0;
}