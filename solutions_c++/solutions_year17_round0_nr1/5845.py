#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

int num_flips(string &s, int start, int k) {
    if (start == int(s.size())) {
        return 0;
    }

    if (s[start] == '+') {
        return num_flips(s, start + 1, k);
    }

    // Flip next k pancakes
    for (int i = start; i < start + k; ++i) {
        if (i >= int(s.size()))
            return -1;
        s[i] = (s[i] == '+' ? '-' : '+');
    }

    int flips = num_flips(s, start + 1, k);
    if (flips != -1) {
        return flips + 1;
    }
    return -1;
}

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s; cin >> s;
        int K; cin >> K;
        int val = num_flips(s, 0, K);
        if (val != -1) {
            cout << "Case #" << t << ": " << val << endl;
        } else {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
