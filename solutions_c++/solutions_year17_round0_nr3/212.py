#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long


int main (void) {
  int T ; cin >> T; FOR(Cas,T) {
    printf("Case #%d: ",Cas);
    LL n , k, ans; cin >> n >> k;
    priority_queue<pair<LL,LL> > pq;
    pq.push(make_pair(n,1));
    while (pq.size()) {
      pair<LL,LL> tmp = pq.top(); pq.pop();
      while (pq.size() && pq.top().first == tmp.first) {
        tmp.second += pq.top().second;
        pq.pop();
      }
      if (k <= tmp.second) {
        ans = tmp.first;
        break;
      }
      k -= tmp.second;
      pq.push(make_pair(tmp.first/2,tmp.second));
      pq.push(make_pair((tmp.first-1)/2,tmp.second));
    }
    cout << ans/2 << ' ' << (ans-1) / 2 << endl;
  }
  return 0;
}
