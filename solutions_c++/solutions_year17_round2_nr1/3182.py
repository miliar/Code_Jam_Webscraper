#include <bits/stdc++.h>

using namespace std;
int main()
{
    int t;
    long long d,n,k,s;
    double max=0, tim=0,ans=0;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        max=0;
        cin>>d>>n;
        for(int i=0; i<n; i++){
            cin>>k>>s;
            tim = 1.0*(d - k)/s;
            if(tim>max){
                max = tim;
            }
        }
        ans = d*1.0/max;
        cout<<"Case #"<<tc<<": ";
        printf("%.6lf \n",ans);
    }
    return 0;
}
