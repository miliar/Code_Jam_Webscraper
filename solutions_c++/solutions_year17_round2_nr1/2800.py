#include <limits>
#include <iostream>
#include <string>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=0; t<T; ++t){
    double D; cin >> D;
    double N; cin >> N;
    double maxTime = 0;
    for(int n=0; n<N; ++n){
      double K, S;
      cin >> K;
      cin >> S;

      double v = (double)(D-K)/(double)S;
      if(maxTime < v){
	maxTime = v;
      }
    }
    
    double ans = D/maxTime;
    cout.precision(17);
    cout << "Case #" << t+1 << ": " << ans << endl;
  }
  
  return 0;
}
