#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

sortme(long double* heigh, int * pos,int n){
    
    long double temp; int posi;
    for(int i=n-1;i>0;i--){
        for(int j=i-1;j>=0;j--){
            if(heigh[i]>heigh[j]){
                temp=heigh[i];
                heigh[i]=heigh[j];
                heigh[j]=temp;
                posi=pos[i];
                pos[i]=pos[j];
                pos[j]=posi;
            }
        }
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,num=0; cin>>t;
    while(t--){
        cout<<"Case #"<<++num<<": ";
        int n,k,posi,flag=0; cin>>n>>k;  int rad[n],pos[n]; long double heigh[n],unsortHeigh[n]; long double ans=0,sum=0,val=0;
        
        for(int i=0;i<n;i++) pos[i]=i;
        for(int i=0;i<n;i++){
            cin>>rad[i]>>unsortHeigh[i];
            heigh[i]=(long double)2*((long double)138230.076757951/(long double)44000)*(long double)unsortHeigh[i]*(long double)rad[i]; 
            unsortHeigh[i]=heigh[i];
        }
        
        sortme(heigh,pos,n);
        ans=sum;
        for(int i=0;i<k;i++) sum+=heigh[i];
        //cout<<"hey sum "<<sum<<endl;
        for(int i=0;i<n;i++){
            val=sum; flag=0;
            for(int j=0;j<k;j++){
                if(pos[j]==i){ flag=1; }
            }
            
            if(flag==0){ val-=heigh[k-1]; val+=unsortHeigh[i]; }
            val+=((long double)138230.076757951/(long double)44000)*(long double)rad[i]*(long double)rad[i];
            if(val>ans) ans=val;
        }
        
         cout<<fixed<<setprecision(9)<<ans<<endl;
        //long long double  
       // for(int i=0;i<n;i++) { cout<<heigh[i]<<" "<<pos[i]<<endl; }
        
    }
    return 0;
}
