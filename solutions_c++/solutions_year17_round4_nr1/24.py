#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <iomanip>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {
    int T;
    cin >> T;
    for (int caseno = 1; caseno <= T; ++caseno) {
        int no = 0;
        int n, p;
        cin >> n >> p;
        vector<int> g(p);
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            x %= p;
            g[x]+=1;
        }
        if (p == 2) {
            no = g[0] + (g[1] + 1) / 2;
        } else if (p == 3) {
            no = g[0] + min(g[1], g[2]) + (max(g[1], g[2]) - min(g[1], g[2]) + 2) / 3;
        } else if (p == 4) {
            cerr << g[0] << ' ' << g[1] << ' ' << g[2] << ' ' << g[3] << endl;
            no = g[0];
            no += g[2] / 2;
            g[2] %= 2;
            no += min(g[1], g[3]);
            int remain = max(g[1], g[3]) - min(g[1], g[3]);
            if (g[2]) remain += 2;
            no += (remain + 3) / 4;
        }
        printf("Case #%d: %d\n", caseno, no);
    }
}
