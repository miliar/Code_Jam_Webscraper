#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORL(v,p,k) for(int v=p;v<k;++v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

vector<pair<LL,LL> > q;

void dodaj(LL l, LL c, int i){
  int j = (int)q.size();
  j--;
  if (j > i && q[j].first == l)
    q[j].second += c;
  else 
    q.PB(make_pair(l, c));
}

int main(){
  int te;
  LL k, n;
  scanf("%d", &te);
  FOR(ii, 1, te){
    q.clear();
    scanf("%lld%lld", &n, &k);
    q.PB(make_pair(n, 1LL));
    int i = 0;
    while(k > 0LL){
      LL l = q[i].first;
      LL c = q[i].second;
      k -= c;
      if (k <= 0){
        printf("Case #%d: %lld %lld\n", ii, l/2, (l-1)/2);
        break;
      }
      if (l % 2LL == 1LL)
        dodaj(l/2, c*2LL, i);
      else{
        dodaj(l/2, c, i);
        dodaj((l-1)/2, c, i);
      }
      i++;
    }
  }
    return 0;
}
