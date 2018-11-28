#include <iostream>
#include <map>
#include <cmath>
#include <algorithm>
#include <utility>

using namespace std;

typedef long long ll;

struct Node {
    ll left;
    ll right;
    ll ls;
    ll rs;
    ll minS;
    ll maxS;
    ll m;
    Node(ll l, ll r): left(l), right(r) {
        m = left + (right - left)/2;
        ls = m - left;
        rs = right - m;
        minS = min(ls, rs);
        maxS = max(ls, rs);
    }
    
    bool operator < (const Node& rhs) const {
        if (minS != rhs.minS) {
            return minS < rhs.minS;
        }
        else if (maxS != rhs.maxS) {
            return maxS < rhs.maxS;
        }
        else {
            return left < rhs.left;
        }
    }
};

int main() {
    int t;
    cin >> t;

    for (int kase = 1; kase <= t; kase++) {
        ll n, k;
        cin >> n;
        cin >> k;
        map<ll, ll> counts;
        counts.insert(make_pair(n, 1));
        ll total = 0;
        while (true) {
            auto iter = counts.rbegin();
            ll range = iter->first;
            ll count = iter->second;
            
            counts.erase(range);
            
            //cout << range << " " << count << endl;
            ll m = (range - 1)/2;
            ll lrange = m;
            ll rrange = range - m - 1;
            counts[lrange] += count;
            counts[rrange] += count;
            total += count;
            if (total >= k) {
                cout << "Case #" << kase << ": " << max(lrange, rrange) 
                        << " " <<  min(lrange, rrange) << endl;
                break;
            }  
        }
        
    }
}