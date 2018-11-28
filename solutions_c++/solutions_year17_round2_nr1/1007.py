#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>

int main(){
    int T;
    scanf("%d",&T);
    for(int tc = 1; tc <= T; tc++){
        printf("Case #%d: ",tc);
        long long D, N;
        scanf("%lld%lld",&D,&N);
        std::vector<std::pair<long long, long long>> Data(N);
        for(int i= 0 ; i< N;i++) scanf("%lld%lld",&Data[i].first,&Data[i].second);

        std::sort(Data.begin(),Data.end());
        double tt = 0;
        for(int i = 0; i < N;i++){
            tt = std::max(tt,(D-Data[i].first)/(double)Data[i].second);
        }
        printf("%lf\n",D/tt);
    }
}
