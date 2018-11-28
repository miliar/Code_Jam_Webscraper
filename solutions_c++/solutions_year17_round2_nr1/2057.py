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

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        vector<P> V;
        int D,N;
        cin>>D>>N;
        double T = 0;
        for(int i=0;i<N;i++){
            double K,S;
            cin>>K>>S;
            T = max((D-K)/S,T);
        }
        double ans = double(D)/T;
        printf("Case #%d: %.6f\n",t,ans);
    }

    return 0;
}