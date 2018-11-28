#include<bits/stdc++.h>
using namespace std;

long long int solve(long long int n){
    long long int ans=n;
    long long int minE=11,minP=-1;
    long long int t=0;
    if(n<10){
        return n;
    }
    while(n>0){
       long long int x= n%10;
        if(x<=minE){
            minE=x;
            n=n/10;
            t++;
            minP=t;
            // ans=n;
        }
        else if(x>minE){
            // cout<<"ansB -->"<<ans<<endl;
            // cout<<"nnB___>"<<n<<endl;
            // cout<<"mineB=--->"<<minE<<minP<<" "<<(n*pow(10,minP))-1<<endl;
            // long long int diff=ans-(n*pow(10,minP));
            // cout<<"DIff -->"<<diff<<endl;
            ans=(n*pow(10,minP));
            ans=ans-1;
            // cout<<"ans -->"<<ans<<endl;
            // cout<<"DIff -->"<<diff<<endl;
            n=ans/pow(10,minP);
            // cout<<"nn___>"<<n<<endl;
            t=minP;
            minE=x-1;
            // cout<<"mine=--->"<<minE<<minP<<endl;
        }
        // else{
        //     n=n/10;
        // }
    }
    return ans;
}
int main(){
    int tCase;
    cin>>tCase;
    for(int t=1;t<=tCase;t++){
        long long int n;
        cin>>n;
        cout<<"Case #"<<t<<": "<<solve(n)<<endl;

    }
    return 0;
}