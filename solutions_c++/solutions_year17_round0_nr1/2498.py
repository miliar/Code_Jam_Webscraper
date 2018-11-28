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
        getline(cin, line);
        istringstream iss(line);
        int k = 0;
        string s;
        iss >> s >> k;
        int ans = 0;

        int i = 0;
        while (1) {
            while (i < s.length() && s[i] == '+') {
                i++;
            }
            if (i < s.length()) {
                if (i > s.length() - k) {
                    ans = -1;
                    break;
                } else  {
                    for (int j = 0; j < k; j++) {
                        if (s[i+j] == '+') {
                            s[i+j] = '-';
                        } else {
                            s[i+j] = '+';
                        }
                    }
                    ans++;
                }
            } else {
                break;
            }
            //cout << s << endl;
        }

        cout << "Case #" << caseNum+1 << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }
}
