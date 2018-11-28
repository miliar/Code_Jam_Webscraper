#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    int t;
    int cas=0;
    cin>>t;
    while(t--){
        long long d;
        int n;
        cin>>d>>n;
        double maxHorg=-1;
        for(int i=0;i<n;i++){
            int k,s;
            cin>>k>>s;
            double h=(d-k+0.0)/(s+0.0);
            //cout<<h<<endl;
            if(h>maxHorg){
                maxHorg=h;
            }
        }

        cout<<"Case #"<<++cas<<": "<<fixed<<setprecision(6)<<d/maxHorg<<endl;
    }
}
