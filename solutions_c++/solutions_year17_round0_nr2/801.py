#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

typedef long long ll;

#include <cassert>


inline ll vec2ll(vector<int>& v) {
    int k = v.size();
    ll n = 0LL;
    rep(i, k) {
        n = n * 10LL + v[i];
    }
    return n;
}


vector<int> s;
int k;

ll sub(vector<int>& abc, int i) {
    if (i == k) {
        assert(abc <= s);
        return vec2ll(abc);
    }

    ll best = -1;

    int si = s[i];
    for (int j=i; j<k; ++j) abc[j] = si;
    if (abc <= s) {
        best = max(best, sub(abc, i+1));
    }

    if (si > 0) {
        abc[i] = si-1;
        for (int j=i+1; j<k; ++j) abc[j] = 9;
        best = max(best, vec2ll(abc));
    }

    return best;
}

ll solve_l(ll N) {
    assert(1 <= N && N <= 1e18);

    s.clear();
    while (N) {
        s.push_back((int)(N % 10LL));
        N /= 10LL;
    }
    reverse(all(s));
    k = s.size();
    int first = s[0];
    assert(1 <= first && first <= 9);

    {
        vector<int> aaa(k, s[0]);
        if (s < aaa) {
            vector<int> nines(k, 9);
            nines[0] = s[0]-1;
            return vec2ll(nines);
        }
    }

    vector<int> abc(k, s[0]);
    return sub(abc, 1);
}

int main(){
  int _T; cin>>_T;


  rep(_t,_T){
      ll N; cin >> N;

 answer:
    cout << "Case #" << (1+_t) << ": ";
    cout << solve_l(N) << endl;
  }
}
