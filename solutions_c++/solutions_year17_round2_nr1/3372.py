#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        long long int d,n;
        cin>>d>>n;
        long long int  k[1001],s[1001];
        float max=0.0;
        for (int j=0; j<n; j++){
            cin>>k[j]>>s[j];
            float temp=(d-k[j])*1.0/s[j];
              // cout<<
            //cout<<d<<" "<<k[j]<<" "<<s[j]<<endl;
            if(temp>max)max=temp;
        }
        float ans=d/max;
        //cout<<max<<endl;
     
        cout<<"Case #"<<i+1<<": "<<std::setprecision(10)<<ans<<endl;

    }
    return 0;
}

