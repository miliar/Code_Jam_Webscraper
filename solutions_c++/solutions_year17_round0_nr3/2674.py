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

typedef map<ll, ll>::reverse_iterator mit;

int main() {
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    map <ll, ll> m;
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        ll n, k;
        cin >> n >> k;
        cout << "Case #" << t << ": ";
        m.clear();
        m[n]++;
        while (k > 0) {
            mit it = m.rbegin();
            k -= it->second;
            if (k <= 0) {
                //found
                cout << it->first / 2 << " " << (it->first - 1) / 2 << endl;
                break;
            } else {
                m[it->first / 2] += it->second;
                m[(it->first - 1) / 2] += it->second;
                m.erase(it->first);
            }
        }
    }
    
    return 0;
}
