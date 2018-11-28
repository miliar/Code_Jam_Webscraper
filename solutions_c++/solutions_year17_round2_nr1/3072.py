#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <math.h>
#include <utility>
#include <algorithm>
#include <vector>
using namespace std;
#define eps 1e-8;

int main () {
    long long int T,D,N;
    cin>>T;
    for (int t=1;t<=T;t++) {
        pair<long long int,long long int> H[1100];
        cin>>D>>N;
        for (int i=0;i<N;i++)
            cin>>H[i].first>>H[i].second;
        sort(H,H+N);
        double sspo,ssp,longesttime=-99;
        for (int i=0;i<=N-1;i++) {
            sspo=H[i].first;
            ssp=H[i].second;
            //double sst=(N-sspo)/ssp;
            /*for (int i=0;i<N-1;i++) {
             double kdiff=H[i+1].first-H[i].first;
             double sdiff=H[i].second-S[i+1].second;
             if (sdiff<=eps) {
             
             ssp=min(H[i].second,ssp);
             
             }
             else {
             double time=kdiff/sdiff;
             
             }
             }*/
            longesttime=max(longesttime,(D-sspo)/ssp);
        }
        double ans=(double)D/(double)longesttime;
        printf("Case #%d: %.6lf\n",t,ans);
        //cout<<setprecision(6)<<ans<<endl;
        //cout<<setprecision(6)<<ans<<endl;
    }
}
