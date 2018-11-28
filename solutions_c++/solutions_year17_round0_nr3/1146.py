typedef long long ll;

#include <map>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }
inline ll getLL(){ ll s; scanf("%lld", &s); return s; }

#include <set>

using namespace std;


int main(){
  const int t = getInt();
  REP(c,t){
    const ll n = getLL();
    const ll k = getLL();

    map<ll, ll> stalls;
    stalls[n] = 1;

    ll cnt = 0;
    while(true){
      const auto largest = stalls.rbegin();

      const ll size = largest->first;
      const ll count = largest->second;

      stalls.erase(size);

      cnt += count;
      const ll lsize = (size - 1) / 2;
      const ll rsize = size - 1 - lsize;

      stalls[lsize] += count;
      stalls[rsize] += count;

      if(cnt >= k){
	printf("Case #%d: %lld %lld\n", c + 1, rsize, lsize);
	break;
      }
    }

  }
  return 0;
}
