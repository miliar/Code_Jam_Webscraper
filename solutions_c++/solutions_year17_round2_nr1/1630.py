#include<bits/stdc++.h>
using namespace std;

int main(){

  int T;
  cin>>T;

  for(int t=1;t<=T;t++){

    int d,n;
    cin>>d>>n;
    
    double hmax=0;

    int k,s;
    for(int i=0;i<n;i++){
      
      cin>>k>>s;
      hmax=max(hmax,(1.0*d-k)/s);
      
    }

    cout<<"Case #"<<t<<": ";
    printf("%.8f\n",1.0*d/hmax);
  }
  
  return 0;
}
