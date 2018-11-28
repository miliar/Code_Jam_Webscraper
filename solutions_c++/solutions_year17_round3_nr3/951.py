#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <assert.h>

using namespace std;
double P[100];

int main(){
   int T;
   cin >> T;
   for(int t=1;t<=T;t++){
      int N, K;
      double U;
      cin >> N >> K;
      cin >> U;
	  for(int i=0;i<N;i++) cin >> P[i];
	  
	  sort(P, P+N);
	  int breaki = -1;
	  double total;
	  for(int i=0; i<N;i++){
	     double level = P[i];
	     total = 0;
	     for(int j=0;j<i;j++) total += level-P[j];
	     if(total > U) {
		    breaki = i;
		    break;
		 }
	  }
	  if(breaki == -1){
	     breaki = N;
	  }
	  //cout << "breaki=" << breaki << endl;
	  assert(breaki>=1);
	  total = 0;
	  for(int j=0;j<breaki-1;j++) total+=P[breaki-1]-P[j];
	  //cout << "total=" << total << endl;
	  double extra = U-total;
	  //cout << "extra=" << extra << endl;
	  double P_final = P[breaki-1] + (extra)/(breaki);
	  //cout << "Pfinal=" << P_final << endl;
	  if(P_final > 1) P_final=1;
	  double ans = pow(P_final, breaki);
	  for(int j=breaki; j<N;j++)
	     ans*=P[j];
	  
	  cout << "Case #" << t << ": " << ans << endl;
   }

}
