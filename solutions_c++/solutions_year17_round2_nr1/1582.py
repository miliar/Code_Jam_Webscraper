#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
main(){
      freopen("a.in","r",stdin);
      freopen("a.out","w",stdout);
      
      int t;
      cin>>t;
      for(int u=1;u<=t;u++){
              int n;
              double a,b,d,ans=0;
              cin>>d>>n;
              
              for(int i=0;i<n;i++){
                      cin>>a>>b;
                      double dist=d-a;
                      double time=dist/b;
                      if(!i)ans=d/time;else
                      ans=min(ans,d/time);        
              }
                      
              cout<<"Case #"<<u<<": ";
              cout<<fixed<<setprecision(6)<<ans<<endl;
      }
}
