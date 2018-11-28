#include<bits/stdc++.h>

using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int d,n;
        cin>>d>>n;
        vector<pair<double,double> > arr(n);
        for(int cnt=0;cnt<n;cnt++)
            scanf("%lf%lf",&arr[cnt].first, &arr[cnt].second);
        double time=0;
        for(int cnt=0;cnt<arr.size();cnt++){
            time = max(time, (double)(d-arr[cnt].first)/arr[cnt].second);
        }
        printf("Case #%d: %.6f\n",t,(double)d/time);

    }

    return 0;
}
