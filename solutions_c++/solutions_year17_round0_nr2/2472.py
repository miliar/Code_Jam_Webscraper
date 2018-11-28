#include <vector>
#include <map>
#include <unordered_map>
#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string line;
    getline(cin, line);
    int inputCount = stoi(line);
    for (int caseNum = 0; caseNum < inputCount; caseNum++) {
        string s;
        getline(cin, s);
        int t = -1;

        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1) {
                int next = s[i+1];
                int cur = s[i];
                if (next < cur) {
                    t = i;
                    break;
                }
            }
        }

        if (t != -1) {
            int max = s[t];

            int peak = 0;
            while (s[peak] != max) {
                peak++;
            }

            s[peak] = s[peak] - 1;

            for (int i = peak+1; i < s.length(); i++) {
                s[i] = '9';
            }

            if (s[0] == '0') {
                s = s.substr(1);
            }
        }

        cout << "Case #" << caseNum+1 << ": " << s << endl;
    }
}
