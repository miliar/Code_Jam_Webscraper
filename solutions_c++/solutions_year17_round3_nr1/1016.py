#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <unordered_map>
#include <unordered_set>
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define fillv(v,a) fill(v.begin(),v.end(),a)
#define EPS 1e-9
typedef long long ll;
typedef std::pair<int,int>pii;
typedef std::vector<int> vi;

using namespace std;

int N,K;
int R[1000],H[1000];
bool cmp(pair<ll,ll> a,pair<ll,ll> b){return a.first>b.first;}
bool cmp2(pair<ll,ll> a, pair<ll,ll> b){return a.second>b.second;}
ll boxSize(ll r,ll h){return (r*2)*h;}
vector<pair<ll,ll>>pankake;
class Solution{
public:
  void solve(int t){
    ll m=0;
    for(int i=0;i<=N-K;i++){
      sort(pankake.begin(),pankake.end(),cmp);
      ll r=pankake[i].first,bsz=pankake[i].second;
      ll ar=area(r)+bsz;
      sort(pankake.begin()+i+1,pankake.end(),cmp2);
      for(int j=1;j<K;j++)ar+=pankake[i+j].second;
      m=max(m,ar);
    }
    printf("Case #%d: %.9f\n",t,(double)m*M_PI);
  }
  ll area(ll r){return r*r;}
  
};

int main(int argc, const char * argv[]) {
  int t;
  cin>>t;
  Solution sol;
  forn(i,t){
    pankake.clear();
    cin>>N>>K;
    forn(i,N){
      cin>>R[i]>>H[i];
      pankake.push_back({R[i],boxSize(R[i],H[i])});
    }
    sol.solve(i+1);
    // fprintf(stderr, "Case #%d:\n", t + 1);
  }
}

