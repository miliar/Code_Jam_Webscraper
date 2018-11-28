#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <queue>

#define fill(v,val) fill((v).begin(), (v).end(), (val))
#define fillt(tab, n, val) fill((t), (t) + (n) ,(val))
#define MAX 100005
#define INF 9999999
#define in(a,b)  ( (b).find(a) != (b).end())
#define clr(a,b) memset((a), (b), sizeof((a)))
#define pb       push_back
#define all(a)   a.begin(), a.end()  
#define mp     make_pair
#define read_fast ios_base::sync_with_stdio(false);
# define PI           3.14159265358979323846
typedef long long ll;

/**
 * @Author Mehdi Maick
 *
 **/
  
using namespace std;
const int mx = 1e5 + 10;

int maskSize(int mask){
  int ret = 0;
  while(mask != 0){
    ret ++;
    mask >>= 1;
  }
  return ret;
}

int main(int argc , char* argv[]) {
  
  int T; cin >> T; 
  for(int tc = 1; tc <= T; tc++){
    int N, K; cin >> N >> K;
    vector< pair<double, double> > P;
    for(int i = 0; i < N; i++){
      double r, h; cin >> r >> h;
      P.pb({r, h});
    }
    double ret = 0.0;
    int mask = 1 << (N);
    for(int i = 0; i < mask; i++){
      vector<pair< double , double > > pos;
      for(int j = 0; j < N; j++){
        if(i & (1 << j)) pos.pb(P[j]);
      }
      if(pos.size() == K){
        sort(all(pos));
        reverse(all(pos));
        double ans = 0.0;
        for (int ii = 0; ii < K; ii++){
          ans += 2 * pos[ii].first * PI * pos[ii].second;
          if(ii > 0){
            ans += pos[ii - 1].first * pos[ii - 1].first * PI - pos[ii].first * pos[ii].first * PI;
          }
        }
        ans += pos[K - 1].first * pos[K - 1].first * PI;
        ret = max(ret, ans);
      }
    } 

    printf("Case #%d: %.7lf\n", tc, ret);
  }


  return 0;
}

