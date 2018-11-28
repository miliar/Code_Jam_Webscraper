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
typedef pair<double,double> dd;

#include <cassert>

#define PI 3.14159265358979323846

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      int N, K; cin >> N >> K;
      vector<dd> q;
      rep(n,N){
          int r, h;
          cin >> r >> h;
          double s = PI*2*r*h;
          double t = PI*r*r;
          q.push_back(dd(s,t));
      }

      double ans = 0.0;

      for (int i=0; i<N; ++i) {
          double top = q[i].second;
          priority_queue<double> pq;
          for (int j=0; j<N; ++j) {
              if (j == i) continue;
              if (q[j].second > top) continue;
              pq.push(q[j].first);
          }

          double side = q[i].first;
          for (int k=1; k<K; ++k) {
              if (pq.empty()) break;
              double s = pq.top(); pq.pop();
              side += s;
          }

          ans = max(ans, top + side);
      }

 answer:
    printf("Case #%d: %.7f\n", 1+_t, ans);
  }
}
