#include<iostream>
#include<vector>
#include<queue>
#include<utility>
#include<algorithm>
#include<iomanip>
#define PI 3.1415926535
using namespace std;

int main() {
  int T,N,K;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>N>>K;
    vector<double> r(N);
    vector<double> h(N);
    vector<double> ar(N);
    for (int i=0;i<N;i++) {
      cin>>r[i]>>h[i];
      /*    if (t==84) {
      cout<<r[i]<<' '<<h[i]<<endl;
      }*/
    }
    double maks = 0.0;
    for (int i=0;i<N;i++) {
      double val = r[i]*r[i] + 2.0*r[i]*h[i];
      for (int j=0;j<N;j++) {
	if (i==j) {
	  ar[j]=0;
	  continue;
	}
	ar[j] = 2*r[j]*h[j];
      }
      sort(ar.begin(),ar.end());
      reverse(ar.begin(),ar.end());
      for (int k=0;k<K-1;k++) {
	val += ar[k];
      }
      //      cout<<i<<' '<<val<<endl;
      if (val > maks) maks = val;
    }
    cout<<setprecision(12)<<"Case #"<<t<<": "<<maks*PI<<endl;
  }
}
    
