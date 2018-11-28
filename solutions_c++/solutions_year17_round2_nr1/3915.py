#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int T,i,ak,as,tmp;
    cin>>T;
    for(int k=1;k<=T;k++) {
        double D,N,ans,mTime=0;
        cin>>D>>N;
        for (i=0; i<N;i++)
        {
          cin>>ak>>as;
          mTime= max(mTime,(D-ak)/as);
        }
    ans=D/mTime;
    cout<<"Case #"<<k<<": "<<fixed<<setprecision(9)<<ans<<endl;
    }
}
