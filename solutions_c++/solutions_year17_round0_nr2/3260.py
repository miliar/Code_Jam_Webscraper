#include <algorithm>
#include <bitset>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main() {
    int NC;
    cin >> NC;
    for (int nc = 1; nc <= NC; nc++) {
        string str;
        cin >> str;
        bool solved = false;
        while (!solved) {
            solved = true;
            char highest = '0';
            int badi = -1;
            for (int i = 0; i < str.size(); i++) {
                if (str[i] > highest) highest = str[i];
                else if (str[i] < highest) {
                    solved = false;
                    badi = i-1;
                }
            }
            if (badi >= 0) {
                str[badi]--;
                for (int i = badi+1; i<str.size(); i++) {
                    str[i] = '9';
                }
            }
            if (badi == 0 && str[badi] == '0') {
                string str2 = "";
                for (int i = 0; i < str.size() - 1; i++) {
                    str2.push_back('9');
                }
                str = str2;
            }

        }
        cout << "Case #" << nc << ": ";
        cout << str;
        cout << endl;
    }
}
