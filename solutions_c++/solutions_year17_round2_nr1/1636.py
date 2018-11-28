#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>  
using namespace std;



int main() {
int t;
cin>>t;
    int c=0;
 while(t--){
     c++;
    double d;
     int n;
    
    cin>>d>>n;
    double p[n],s[n];
    for(int i=0;i<n;i++){
       // int a,b;
        cin>>p[i]>>s[i];
    }
    double ans=0;
    
    for(int i=0;i<n;i++){
        double tans=(d-p[i])/s[i];
        if(tans>ans) ans=tans;
    }
     double fans=d/ans;
     
     cout<<"Case #"<<c<<": ";
     std::cout << std::fixed;
     std::cout << std::setprecision(6) << fans<<endl; 
    
    }
    return 0;
}
