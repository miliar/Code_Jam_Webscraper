#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <algorithm> // sort
#include <utility>
#include <cmath>

typedef long long ll;
using namespace std;

struct seg{
  int s,t;
  bool c;
  seg(int s,int t,bool c): s(s), t(t), c(c){}
  bool operator<(const seg& rhs) const {
    return s < rhs.s;
  }
};

int main(){
  ll T;
  cin >> T;

  for(int t=0; t<T; t++){
    ll N,K;
    double U;
    cin >> N >> K >> U;

    vector<double> Ps(N+1);
    for(int i=0; i<N; i++){
      cin >> Ps[i];
    } Ps[N] = 1.0;
    sort(Ps.begin(), Ps.end());

    // small : K=N
    // maximize min pi.
    for(int i=0; i<N; i++){
      double tmp = (Ps[i+1]-Ps[i]) * (i+1);
      if(tmp <= U){
        for(int j=0; j<i+1; j++){
          Ps[j] = Ps[i+1];
        }
        U -= tmp;
      } else {
        for(int j=0; j<=i; j++){
          Ps[j] += U / (i+1);
        }
        break;
      }
    }

    double ans = 1.0;
    for(int i=0; i<N; i++){
      ans *= Ps[i];
    }
    cout << "Case #" << t+1 << ": " << setprecision(8) << ans << endl;;
  }

  return 0;
}
