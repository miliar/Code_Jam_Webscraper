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
        
        int n, p;
        in >>  n >> p ;
        
        vector<int> remainder(p, 0);
        for (int i = 0; i < n; ++i) {
            int tmp;
            in >> tmp;
            remainder[tmp % p]++;
        }
        int res = remainder[0];
        if (p == 2) {
                res += (remainder[1] + 1) / 2;
        }
        if (p == 3) {
                int tmp = min(remainder[1], remainder[2]);
                res += tmp;
                remainder[1] -= tmp;
                remainder[2] -= tmp;
                res += (remainder[1] + 2) / 3 + (remainder[2] + 2) / 3;
        }
        if (p == 4) {
                int tmp = min(remainder[1], remainder[2]);
                res += tmp;
                remainder[1] -= tmp;
                remainder[2] -= tmp;
                if (remainder[2]) res += 1 + (remainder[1] + 1) / 4 + (remainder[2] + 1) / 4;
                else res += (remainder[1] + 3) / 4 + (remainder[2] + 3) / 4;
        }
        out << "Case #" << i + 1 << ": " << res << endl;
    }
    
    in.close();
    out.close();
}
