#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <valarray>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> pp;

const int CMAX = 1e5 + 5;
const int INF = 2e9 + 5;

int main() {
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        string s;
        cin >> s;
        bool good = false;
        while (!good) {
            good = true;
            for (int i = 1; i < s.length(); i++) {
                if (s[i] < s[i-1]) {
                    good = false;
                    s[i-1]--;
                    for (int j = i; j < s.length(); j++) s[j] = '9';
                }
            }
        }
        int i = 0;
        while (s[i] == '0') i++;
        cout << "Case #" << t << ": ";
        for (; i < s.length(); i++) cout << s[i];
        cout << endl;
    }
    
    return 0;
}
