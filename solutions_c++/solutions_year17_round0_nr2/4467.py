#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <map>
#include <math.h>
#include <queue>
#include <climits>
#include <iomanip>

using namespace std;

void solution(string& s)
{
    if (s.size() <= 1) {
        cout << s << endl;
        return;
    }

    for (int i = 1; i < s.size(); ++i) {
        if (s[i] < s[i-1]) {
            if (i-1 == 0 && s[i-1] == '1') {
                string res(s.size() - 1, '9');
                cout << res << endl;
                return;
            }

            int j = i - 1;
            while (j > 0 && s[j] == s[j-1]) {
                --j;
            }

            if (j == 0 && s[j] == '1') {
                string res(s.size() - 1, '9');
                cout << res << endl;
                return;
            }

           s[j++] -= 1;
           while (j < s.size()) {
               s[j] = '9';
               ++j;
           } 

           cout << s << endl;
           return;
        }
    }
    cout << s << endl;
}

int main()
{
    int T;
    cin >> T;

    for (size_t i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        string input;
        cin >> input;
        solution(input );
    }
    return 0;
}
