#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define INF 2000000000
#define pb push_back
#define fs first
#define sc second
#define mp make_pair

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
typedef vector < int > VI;
typedef vector < unsigned int > VUI;
typedef vector < string > VS;
typedef vector < pair < int, int > > VII;


int main (int argc, char** argv) {
    
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);

    int T, k;
    string s;

    cin >> T;

    for (int t = 0; t < T; ++t) {
        cin >> s >> k;

        int l = s.length();
        int ans = 0;
        for (int i = 0; i <= l - k; ++i)
            if (s[i] == '-') {
                for (int j = 0; j < k; ++j)
                    s[i + j] = (s[i + j] == '+' ? '-' : '+');
                ++ans;
            }

        for (int i = l - k + 1; i < l; ++i)
            if (s[i] == '-') {
                ans = -1;
                break;
            }

        cout << "Case #" << t+1 << ": ";
        if (ans == -1) cout << "IMPOSSIBLE\n";
        else cout << ans << endl;

    }

    return 0;
}
