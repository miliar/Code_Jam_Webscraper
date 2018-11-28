#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <tuple>
#include <cmath>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int N,K;
        cin>>N>>K;
        double U;
        cin>>U;
        vector<double> P(N);
        for(int i=0;i<N;i++){
            cin>>P[i];
        }
        double lo=0,up=1;
        double mul=1.0;
        while(up-lo>1e-8){
            double u=U;
            double mid=(lo+up)/2.0;
            mul=1.0;
            for(auto p:P){
                if(p>=mid){
                    mul*=p;
                }else{
                    u-=mid-p;
                    mul*=mid;
                }
            }
            if(u<0){
                up=mid;
            }else{
                lo=mid;
            }
            if(up-lo<=1e-6){
                // cout<<mid<<' '<<mul<<endl;
            }
        }
        double ans = mul;
        if(N!=K)ans=-1;
        printf("Case #%d: %.6f\n",t,ans);
    }

    return 0;
}