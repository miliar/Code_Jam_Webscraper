#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <iomanip>
 
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
int main(){
  int n_case;
  cin >> n_case;
  for( int loop = 0 ; loop < n_case ; loop++ ){
    long long N,K;
    cin >> N >> K;
    vector< pair<long long, long long> > V;
    for(int i = 0 ; i < N; i++ ){
      long long R,H;
      cin >> R >> H;
      V.push_back(make_pair(R*R, 2*R*H));
    }
    sort( V.begin(), V.end() );
    long long sum = 0;
    priority_queue<long long> side;
    long long ans = V[0].first+V[0].second;
    for( int i = 1 ; i < N ; i++ ){
      //cout << V[i].first << ", " << V[i].second << endl;
      side.push( -V[i-1].second );
      sum += V[i-1].second;
      if( side.size() >= K ){
        long long minside = side.top();
        side.pop();
        sum += minside;
      }
      if( side.size() == K-1 ){
        //cout << V[i].first << "+" << sum << "+" << V[i].second << endl;
        ans = max(ans, sum+V[i].first+V[i].second);
      }
    }
    double dans = M_PI* (double)ans;
    cout << "Case #" << loop+1 << ": "<<fixed << setprecision(15) <<dans<<endl;
  }
  return 0;
}

