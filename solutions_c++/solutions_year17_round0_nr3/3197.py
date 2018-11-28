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
        
        ll n, k;
        in >> n >> k;
        
        map<ll, ll> m;  // # of successive space --> # of such intervals
        m[n] = 1;
        ll space = 0;
        while (k > 0) {
            map<ll, ll>::iterator it = m.end();
            it--;
            if (it->second >= k) {
                space = it->first;
                break;
            }
            else {
                k -= it->second;
                ll tmp = it->first / 2;
                m[tmp] += it->second;
                m[it->first - 1 - tmp] += it->second;
                m.erase(it);
            }
        }
        ll max = space / 2;
        ll min = space - 1 - max;
        
        out << "Case #" << i + 1 << ": "  << max << " " << min << endl;
    }
    
    in.close();
    out.close();
}
