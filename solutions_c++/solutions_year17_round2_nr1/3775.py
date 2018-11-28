#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(ll i=0;i<n;i++)
#define F1(i,n) for(ll i=1;i<=n;i++)
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

ll i, j, k, n,r,c,s,d;
long double m,l;

int main() {
  //freopen("A-small-attempt1.in", "r", stdin);
  //freopen("A-small-attempt1.out", "w", stdout);
  

  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  ll tt, tn;
  long double ans;
  cin >> tn;
  F1(tt,tn) {
    cin>>d>>n;
    m=0.000001;
    l=0;
    ans=0.0;
    F1(i,n){
      cin.ignore();
      cin>>k>>s;
      l=((long double)(d-k))/s;
      //cout.precision(6);
      //cout<<fixed<<l<<endl;
      if(l>m){
        m=l;
      }
    }
    ans=(long double)d/m;
    cout.precision(6);
    printf("Case #%llu: ", tt);
    cout<<fixed<<ans<<endl;
  }
  return 0;
}
