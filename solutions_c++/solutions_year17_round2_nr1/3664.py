#include<iostream>
#include<iomanip>
#include<vector>
#include<map>
#include<cmath>

using namespace std;

int main() {
  int T; cin>>T; cerr<<"Total case: "<<T<<endl;
  for(int z=0;z<T;++z) {
    cerr<<"case "<<z<<endl;
    double D,N;cin>>D>>N;
    cerr<<" "<<D<<","<<N<<endl;
    vector<long long> K(N),S(N);
    double ans;
    for(int i=0;i<N;++i) {
      cin>>K[i]>>S[i];
      cerr<<" "<<K[i]<<","<<S[i]<<endl;
      double t = (D-K[i])/(double)S[i];
      double s = D/t;
      if(i==0 or ans>s) ans=s;
    }
    //for(int i=0;i<N;++i) {
    //  for(int j=i+1;j<N;++j) {
    //    double t = (K[i]-K[j])/(double)(S[j]-S[i]);
    //    if(t<0) t+=-1;
    //    double k = K[i]+S[i]*t;
    //    double s = k/t;
    //    if(ans>s) ans=s;
    //  }
    //}
    cout << "Case #" << z+1 << ": " << fixed<<setprecision(6) << ans << endl;
    cerr << " Ans: "<< fixed<<setprecision(6) << ans << endl;
  }
  return 0;
}


