#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <bitset>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int t, k, ans, v[1010];
string s;

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    cin >> t;
    for(int cas = 1; cas <= t; ++cas) {
        ans = 0;
        cin >> s >> k;
        for(int i = 0; i < s.size(); ++i) v[i] = s[i] == '-' ? 0 : 1;
        for(int i = 0; i < s.size() - k + 1; ++i) {
            if (!v[i]) {
                ++ans;
                for(int j = i; j < i + k; ++j) v[j] = 1 - v[j];
            }
        }
        bool can = true;
        for(int i = 0; i < s.size(); ++i)
            if (v[i] == 0) {
                can = false;
                break;
            }

        if (can) cout << "Case #" << cas << ": " << ans << endl;
        else cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
