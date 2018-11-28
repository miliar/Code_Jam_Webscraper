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
    
    queue<int> Q;
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        string s;
        int k;
        int moves = 0;
        int plus = 0;
        while (!Q.empty()) Q.pop();
        cin >> s >> k;
        for (int i = 0; i <= s.length() - k; i++) {
            if (!Q.empty() && Q.front() == i) { plus--; Q.pop(); }
            if ((s[i] == '+' && plus % 2 == 1) || (s[i] == '-' && plus % 2 == 0)) {
                //flip
                moves++;
                plus++;
                Q.push(i+k);
            }
        }
        for (int i = s.length() - k + 1; i < s.length(); i++) {
            if (!Q.empty() && Q.front() == i) { plus--; Q.pop(); }
            if ((s[i] == '+' && plus % 2 == 1) || (s[i] == '-' && plus % 2 == 0)) {
                moves = -1;
                break;
            }
        }
        if (moves == -1) cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << t << ": " << moves << endl;
    }
    
    return 0;
}
