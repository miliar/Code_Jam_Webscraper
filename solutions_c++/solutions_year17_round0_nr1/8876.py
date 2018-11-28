#include<string>

#include<iostream>
using namespace std;


bool isCorrect(string s)
{
        for (auto c : s) {
            if (c == '-') {
                return false;
            }
        }
        return true;
}    

int main()
{
    string s = "---+-++-";
    int n = 3;
    int t = 1 , ct = 0;

    cin >> t;
    for (int i = 0; i < t; ++i) {
        ct = 0;
        cin >> s;
        cin >> n;
        for (int j = 0; j <= s.length() - n; ++j) {
            if (s[j] == '-') {
                ct ++;
                for (int k = j; k < j + n; ++k) {
                    if (s[k] == '-') s[k] = '+';
                    else s[k] = '-';
                }
            }
        }

        if (isCorrect(s)) {
            cout << "case #" << i + 1 << ": " << ct << endl;
        } else {
            cout << "case #" << i +1 << ": " << "IMPOSSIBLE" << endl;
        }
            
    }
    return 0;
} 
    
