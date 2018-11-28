#include<iostream>
#include<iomanip>
#include<cmath>
#include<vector>
using namespace std;
const double pi=atan(1.0)*4;
int main(){
    cout<<fixed<<setprecision(6);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        double D,N,pos,speed,ans=0.000000;
        cin>>D>>N;
        for(int j=0;j<N;j++){
            cin>>pos>>speed;
            double time = (D-pos)/speed;
            if(time>ans){
                ans=time;
            }
        }
        ans=D/ans;
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
return 0;}
