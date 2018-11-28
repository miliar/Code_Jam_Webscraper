#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;
int main() {
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t;
    fin >> t;
    for (int q = 1; q <= t; q++) {
        string s;
        fin >> s;
        char cur = s[0];
        for (int j = 0; j < s.length(); j++) {
            if (cur <= s[j]) {
                cur = s[j];
            }
            else {
                int k = j - 1;
                while (s[k] == '0' && k > 0) {
                    s[k] = '9';
                    k--;
                }
                if (k != 0 && s[k] == '1') {
                    s[k] = '0';
                }
                else {
                    if (k == 0 && s[k] == '1') {
                        s.erase(0, 1);
                        j--;
                    } else {
                        s[k] -= 1;
                    }
                }
                for (int m = j; m < s.length(); m++) {
                    s[m] = '9';
                }
                j = 0;
                cur = s[0];
            }
        }
        fout << "Case #" << q << ": " << s << endl;

    }
    return 0;
}
