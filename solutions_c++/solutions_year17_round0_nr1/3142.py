#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>

using namespace std;

#define ll long long
#define N (ll)(1e6+5)
#define INF (ll)(1e18+3)
#define EPS (1e-9)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    int t;
    in >> t;
    
    for (int i = 0; i < t; i++) {
        
        string s;
        int k;
        in >> s >> k;
        int len = (int) s.size();
        int a[len + k + 100];
        memset(a,0,sizeof(a));
        int sum = 0, x = 0, j;
        for (j = 0; j <= len - k; ++j) {
            x += a[j];
            if ((s[j] == '-' && x % 2 == 0) || (s[j] == '+' && x % 2 == 1)) {
                sum++;
                x++;
                a[j + k]--;
            }
        }
        bool good = true;
        for (; j < len; ++j) {
            x += a[j];
            if ((s[j] == '-' && x % 2 == 0) || (s[j] == '+' && x % 2 == 1)) {
                out << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
                good = false;
                break;
            }
        }
        if (good)
            out << "Case #" << i + 1 << ": " << sum << endl;
    }
    
    in.close();
    out.close();
}
