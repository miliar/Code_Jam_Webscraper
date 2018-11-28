#include <iostream>
#include <iomanip>
#include <string>
#include <limits.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <numeric>
#include <cfloat>

using namespace std;

struct pancake{
  double R;
  double H;
  double S;
};

int main(int argc, char* argv[]){
  int T;
  cin >> T;

  for(int i=0; i<T; i++){
    int K, N;
    cin >> N >> K;
    // vector<double> R(1000);
    // vector<double> H(1000);
    // vector<double> S(1000);
    vector<pancake> P(1000);
    for(int j=0; j<N; j++){
      // cin >> R[j] >> H[j];
      // S[j] = R[j]*2*M_PI*H[j];
      cin >> P[j].R >> P[j].H;
      P[j].S = P[j].R*2*M_PI*P[j].H;      
    }

    // sort(H.begin(), H.end(),
    // 	 [&R](size_t i1, size_t i2) {return R[i1] > R[i2];});
    // sort(S.begin(), S.end(),
    // 	 [&R](size_t i1, size_t i2) {return R[i1] > R[i2];});
    // sort(R.begin(), R.end(), std::greater<double>());
    sort(P.begin(), P.end(), [](const pancake& a, const pancake& b){return a.S > b.S;});

    double max = 0;
    for(int j=0; j<N; j++){
      double tmp = 0;
      tmp += P[j].R*P[j].R*M_PI;
      if(j < K){
	for(int k=0; k<K; k++){
	  tmp += P[k].S;
	}
      }
      else{
	for(int k=0; k<K-1; k++){
	  tmp += P[k].S;
	}
	tmp += P[j].S;
      }
      if(tmp > max){
	max = tmp;
      }
    }
    cout << setprecision(15);
    cout << "Case #" << i+1 << ": " << max << endl; 

  }

  return 0;
}


