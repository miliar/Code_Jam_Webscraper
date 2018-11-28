#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <numeric>
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

typedef pair<int,int> ii;

#include <cassert>

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      int N, K; cin >> N >> K;
      double U; cin >> U;
      vector<double> P(N);
      rep(n, N) cin >> P[n];
      sort(all(P));

      double l=0.0, h=1.0000001, p;
      rep(i, 100) {
          if (h-l < 1e-9) break;
          double m = (l+h)/2;
          double s = 0, u = 0;
          p = 1.0;
          rep(j,N) {
              if (P[j]>=m) {
                  s += P[j]; p *= P[j];
              } else {
                  s += m; p *= m;
                  u += m-P[j];
              }
          }
          if (u > U) {
              h = m;
          } else {
              l = m;
          }
      }

 answer:
    printf("Case #%d: %.7f\n",1+_t, p);
  }
}
