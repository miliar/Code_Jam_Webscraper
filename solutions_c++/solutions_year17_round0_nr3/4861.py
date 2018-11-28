#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;


int main() {
    
    int t,n,k,val,temp,spac,tot,a,b; cin>>t; int num=0;
    
    while(t--){
        cin>>n>>k; val=n;
        
        a=log(k)/log(2); temp=a; 
        tot=pow(2,a)-1; 
        spac=n-tot; tot++; 
        while(temp--) val=val/2;  
        
        b=tot*val-spac;  
        a=tot-b; 
        if(k-tot+1 > a) val--; 
        a=val/2;
        b=a;
        if(val%2==0) b--;
        cout<<"Case #"<<++num<<": ";
        cout<<a<<" "<<b<<endl;
    }
    
    return 0;
        
}

