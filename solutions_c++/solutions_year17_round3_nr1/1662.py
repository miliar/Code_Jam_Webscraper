#include <stdio.h>
#include <vector>  
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring> 
#include <queue>   
#include <list>
#include <cmath>


#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin();i!=(c).end();i++)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e5 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;

int main() {
  int t,n,k,c=1;
  ll r,h;
  scanf("%d",&t);
  while(t--) {
    vector<pair<long long,long long> > v;
    scanf("%d%d",&n,&k);
    // if(c==69)printf("%d,%d\n",n,k);
    ll maxr=-1,idx=0,maxh=-1;
    ll maxans=0;
    for(int i=0;i<n;i++) {
      scanf("%lld%lld",&r,&h);
      // if(c==69) {
      //   printf("%lld,%lld\n",r,h);
      // }
      v.pb(mp(1LL*r*h,1LL*r));
    }
    sort(v.rbegin(),v.rend());
    long long ans = 0;
    for(int i=0;i<n;i++) {
      ll rr = 1LL*v[i].S,rh=v[i].F;
      int count = 1;
      ll ans = (rr*rr) + 2LL*rh;;
      // if(c==69)printf("ans=%lf\n",acos(-1)*ans);
      for(int j=0;j<n;j++) {
        if(i!=j && rr >= 1LL*v[j].S && count<k) {
          ans += 2LL*v[j].F;
          count++;
        }
        if(count==k) break;
      }
      if(count==k) {
          maxans = max(maxans,ans);
      }
    }

    double final = acos(-1)*maxans*1.0;
    printf("Case #%d: %.10lf\n",c++,final);
  }
  return 0;
}