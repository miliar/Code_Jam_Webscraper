// Example program
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void flip(string & s, int i, int k) {
    for (int j = i; j < i + k; j++) {
        if (s[j] == '+') {
            s[j] = '-';
        }
        else {
            s[j] = '+';
        }
    }
}

int main()
{
    int t, k;
    string s;
    // cout << "Enter number of test cases: ";
    cin >> t; // T test cases
    for (int i = 0; i < t; i++) {
        // cout << "Enter test string: ";
        cin >> s;
        // cout << "Enter size of pancake flipper: " ;
        cin >> k;
        int numFlips = 0;
        // cout << "s: " << s << endl;
        for (int j = 0; j <= s.length() - k; j++) {
            if (s[j] == '-') {
                flip(s, j, k);
                // cout << "s: " << s << endl;
                numFlips++;
            }
        }
        bool happy = true;
        for (int j = 0; j < k; j++) {
            if (s[s.length() - 1 - j] == '-') {
                happy = false;
                break;
            }
        }
        if (happy) {
            cout << "Case #" << (i+1) << ": " << numFlips << endl;
        }
        else {
            cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
        }    
    }          
}
