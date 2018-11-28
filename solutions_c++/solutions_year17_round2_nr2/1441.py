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
 int n,r,o,y,g,b,v;
    cin>>n>>r>>o>>y>>g>>b>>v;
    vector<pair<int,int>> vp;
      vp.push_back(make_pair(r,1));
      vp.push_back(make_pair(y,2));
      vp.push_back(make_pair(b,3));
    //  r=1  y=2  b=3 ; 
    sort(vp.begin(),vp.end());
   int max=vp[2].first;
        if( max > vp[1].first + vp[0].first ){
            cout<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        int rem=vp[2].first-vp[1].first;
        vp[0].first-=rem;
        vp[2].first-=rem;
        
        string s,vp0,vp1,vp2;
         if(vp[2].second==1){
                 
             vp2="R";   
                }
        if(vp[2].second==2){
                  vp2="Y";   
                }
        if(vp[2].second==3){
                  vp2="B";   
                }
        if(vp[1].second==1){
                  vp1="R";   
                }
         if(vp[1].second==2){
                 vp1="Y";   
                }
         if(vp[1].second==3){
                 vp1="B";   
                }
         if(vp[0].second==1){
                  vp0="R";   
                }
         if(vp[0].second==2){
                  vp0="Y";   
                }
         if(vp[0].second==3){
                  vp0="B";   
                }
        for(int i=0;i<n;i++){
            if(vp[2].first>0){
               s+=vp2;
                vp[2].first--;
            }
            if(vp[1].first>0){
               s+=vp1;
                vp[1].first--;
            }
            if(vp[0].first>0){
               s+=vp0;
                vp[0].first--;
            }
           
            
        }
         for(int i=0;i<rem;i++){
                s+=vp2;
                s+=vp0;
            }
       
     
     cout<<"Case #"<<c<<": "<<s<<endl;
   
    }
    return 0;
}
