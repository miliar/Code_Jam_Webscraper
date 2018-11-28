#include<bits/stdc++.h>
using namespace std;


int main(){
    long long int test;
    cin>>test;
    long long int j=1;
    for(j=1;j<=test;j++){
        int d,n;
        cin>>d>>n;
        long double tim=-1.000;
        int k,s;
        for(int i=0;i<n;i++){
            cin>>k>>s;
            k=d-k;
            tim=max(tim,(long double)k/(long double)s);
        }
        printf("Case #%lld: %Lf\n",j,(long double)d/tim);
    }
}
