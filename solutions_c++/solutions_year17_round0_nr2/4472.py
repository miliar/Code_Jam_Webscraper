#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <bitset>
#include <iomanip>

using namespace std;

typedef long long int LLI;

#define _ ios_base::sync_with_stdio(0);

const int inf = 0x3f3f3f3f;
const double eps = 1e-8; 

char str[20];

int main() { _
    int t;
    string n;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
        cout << "Case #" << kase << ": ";
        cin >> n;
        str[0] = n[0];
        while (1) {
            bool change = 0;
            for (int i = 1; i < n.length(); ++i) {
                if (n[i-1] > n[i]) {
                    n[i-1] -= 1;
                    for (int j = i; j < n.length(); ++j) {
                        n[j] = '9';
                    }
                    change = 1;
                    break;
                }
            }
            if (!change) break;
        }
        if (n[0] != '0') cout << n[0];
        for (int i = 1; i < n.length(); ++i) {
            cout << n[i];
        }
        cout << "\n";
    }

    return 0;
}
