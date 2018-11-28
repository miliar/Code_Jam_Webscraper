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
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/largeOut.txt", "w", stdout);
//    int T = SS;
//    rep(t, T) {
//        int n, ans = 0;
//        cin>>n;
//        ifor(i, n, 1) {
//            if (isDec(i)) {
//                ans = i;
//                break;
//            }
//        }
//        printf("Case #%d: %d\n", t+1, ans);
//    
//    }
    int T = SS;
    rep(t, T) {
        S s;
        cin>>s;
        rep(i, si(s) - 1) {
            if (s[i+1] < s[i]) {
                int p = i;
                while (p >=0 && s[p] == s[i]) p--;
                s[p+1]--;
                fori(k, p+2, si(s)) {
                    s[k] = '9';
                }
                break;
            }
        }
        S ans;
        int i = 0;
        while (s[i] == '0') i++;
        while (i < si(s)) {
            ans += s[i++];
        }
        
        printf("Case #%d: %s\n", t+1, ans.c_str());
    }
}
 











