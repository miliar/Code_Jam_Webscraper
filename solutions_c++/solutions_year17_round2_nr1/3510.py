#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;


int main() {
   long int t,n,temp,num=0; long double d,max=0.0; cin>>t;
    while(t--){
        max=0.0;
        cout<<"Case #"<<++num<<": ";
        cin>>d; cin>>n; long double a,b,c;
        for(int i=0;i<n;i++){ 
            cin>>a>>b; c=(long double)(d-a)/(long double)b;
            if(max<c) max=c; 
        } 

        c=d/max;


      
        cout<<fixed<<setprecision(6)<<c<<endl;

     

    }

    
    
    
    
    
    
    
    
    return 0;
}
