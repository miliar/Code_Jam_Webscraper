// Author: Mahesh
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(auto i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

map<ll, int> hh;

int isDec(int n) {
    int last = 9;
    while (n) {
        if (n % 10 > last) return 0;
        last = n % 10;
        n = n/10;
    }
    return 1;
}

int main() {
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/inp.txt", "r", stdin);
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/CSmall3", "w", stdout);
//    int T = SS;
//    rep(t, T) {
//        int n = SS, k = SS, ansMin = 0, ansMax = 0;
//        multiset<int> s;
//        s.clear();
//        s.insert(n);
//        rep(i, k) {
//            int largest = *s.rbegin();
//            s.erase(s.find(largest));
//            s.insert((largest-1)/2);
//            s.insert(largest/2);
//            if (i == k-1) {
//                ansMin = (largest-1)/2;
//                ansMax = largest/2;
//            }
//        }
//        
//        printf("Case #%d: %d %d\n", t+1, ansMax, ansMin);
//    }
    int T = SS;
    rep(t, T) {
        ll K, N, k;
        cin>>N>>K;
        k = K;
        int x = 0;
        ll curMax = N;
        while (k - (1LL<<x) > 0) {
            k -= (1LL<<x);
            x++;
            curMax /= 2;
        }
        ll remainGaps = N - (K-k);
        ll curWidth = 1LL<<x;
        ll curMaxFreq = remainGaps - (curMax - 1) * curWidth;
        ll lastGap = k <= curMaxFreq ? curMax : (curMax - 1);
        printf("Case #%d: %lld %lld\n", t+1, lastGap / 2, (lastGap - 1) / 2);
    }
}
 











