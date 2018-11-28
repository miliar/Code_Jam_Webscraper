#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(k,a,b) for(int k=(a); k<(b); k++)

void solve_case(int T){
  int N;
  double D, K, S, max = 0;
  cin >> D >> N;
  FOR(i,0,N){
  	cin >> K >> S;
  	if ((D - K)/S >= max){
  		max = (D - K)/S;
  	}
  }

  printf("Case #%d: %.6f \n", T, D/max);
  //cout << "Case #" << T << ": " << D/max << endl;
}

int main(){
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}