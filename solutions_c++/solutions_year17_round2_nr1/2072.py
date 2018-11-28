#include <iostream>
#include<algorithm>
#include<cmath>
#include<iomanip>
using namespace std;

int main() {
    int n,t,i,j;
    double d;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>d>>n;
        double ti;
        ti=0;
        double k[n],s[n];
        for(j=0;j<n;j++){
            cin>>k[j]>>s[j];
        }
        for(j=0;j<n;j++){
            if((d-k[j])/s[j]>ti)
                ti=(d-k[j])/s[j];
        }
        cout<<"Case #"<<i<<": "<<setprecision(10)<<d/ti<<endl;
    } 
 
	return 0;
}
