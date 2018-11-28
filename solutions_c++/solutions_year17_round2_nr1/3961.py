#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    long long int d,n,k,s;
    double ans;
    cin>>t;
    for(int _ = 1; _ <= t; _++)
    {
        cout<<"Case #"<<_<<": ";
        cin>>d>>n;
        ans = 0.0;
        for(int i = 0; i< n; i++)
        {
            cin>>k>>s;
            if(ans < double(d-k)/s)
                ans = double(d-k)/s;
        }
        printf("%.9lf\n",double(d)/ans);
    }
}
