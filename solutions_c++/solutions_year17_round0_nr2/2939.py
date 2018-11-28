#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

int main() {
    freopen("B-large.in" , "r" , stdin);
    freopen("bb.out" , "w" , stdout);

    int T;
    cin >> T;

    for (int kase = 0; kase < T; kase++) {
        string s;
        cin >> s;

        bool modify = false;
        while (true) {
            for (int i = 0; i < s.length() - 1; i++) {
                if (s[i] > s[i+1]) {
                    modify = true;
                    s[i] = s[i] - 1;
                    for (int j = i + 1; j < s.length(); j++) {
                        s[j] = '9';
                    }
                }
            }
            if (!modify) {
                break;
            }
            modify = false;
        }

        while (s.length() > 1 && s[0] == '0') {
            s = s.substr(1);
        }
        cout << "Case #" << kase + 1 << ": " << s << endl;
    }
    return 0;
}
