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
typedef pair<ll, ll> ll_ll;

#include <cassert>


ll_ll solve_s3(ll N, ll K) {
    priority_queue<ll_ll> pq;

    pq.push(ll_ll(N, 1));

    ll k = 0;
    while (true) {
        ll L = pq.top().first, M = pq.top().second; pq.pop();
        if (!pq.empty()) {
            ll next_L = pq.top().first;
            if (next_L == L) {
                ll next_M = pq.top().second;
                pq.pop();
                pq.push(ll_ll(L, M+next_M));
                continue;
            }
        }
        ll m = (L-1)/2, r = (L-1) - m;
        assert(m <= r && r <= m+1);
        pq.push(ll_ll(m, M));
        pq.push(ll_ll(r, M));

        if (K <= M) {
            return ll_ll(r, m);
        }
        K -= M;
    }

    return ll_ll(0, 0);
}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      ll N, K; cin >> N >> K;


      ll_ll ans = solve_s3(N, K);
      ll maxl = ans.first, minl = ans.second;
 answer:
    cout << "Case #" << (1+_t) << ": ";
    cout << maxl << " " << minl;
    cout << endl;
  }
}
