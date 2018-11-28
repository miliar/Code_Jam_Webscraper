#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <tuple>
#include <cmath>
using namespace std;
typedef pair<int,int> P;
typedef tuple<int,int,int> T;
const double pi = M_PI;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int N,K;
        cin>>N>>K;
        vector<P> V1;
        vector<double> V2;
        for(int i=0;i<N;i++){
            int R,H;
            cin>>R>>H;
            V1.emplace_back(R,H);
        }
        sort(V1.begin(), V1.end(),greater<P>());
        double ans=0;
        for(int b=0;b<N;b++){
            int Rk,Hk;
            tie(Rk,Hk)=V1[b];
            double sur = pow(Rk,2)*pi+2.0*Hk*Rk*pi;
            V2.clear();
            for(int i=0;i<N;i++){
                int R,H;
                if(b!=i){
                    tie(R,H)=V1[i];
                    if(R<=Rk) V2.emplace_back(2.0*R*H*pi);
                }
            } 
            sort(V2.begin(), V2.end(),greater<double>());
            if(K-1>V2.size()) continue;
            for(int i=0;i<K-1;i++){
                sur+=V2[i];
            }
            ans=max(ans,sur);
        }
        printf("Case #%d: %.9f\n",t,ans);
    }

    return 0;
}