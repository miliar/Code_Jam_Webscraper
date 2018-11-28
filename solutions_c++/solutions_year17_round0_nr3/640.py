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

ll t, n, k;
map<ll, ll> m;
map<ll, ll>::iterator it;

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    cin >> t;
    for(int cas = 1; cas <= t; ++cas) {
        cin >> n >> k;
        m.clear();
        m[n] = 1;
        while(true) {
            it = m.end();
            --it;
            if (it->second < k) {
                k -= it->second;
                if (it->first % 2 == 0) {
                    if (it->first != 2) m[it->first / 2 - 1] += it->second;
                    m[it->first / 2] += it->second;
                } else {
                    m[it->first / 2] += (2 * it->second);
                }
                m.erase(it);
            } else {
                if (it->first % 2 == 0) {
                    cout << "Case #" << cas << ": " << it->first / 2 << " " << it->first / 2 - 1 << endl;
                } else {
                    cout << "Case #" << cas << ": " << it->first / 2 << " " << it->first / 2 << endl;
                }
                break;
            }
        }
    }
    return 0;
}
