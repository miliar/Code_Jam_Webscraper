#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
main(){
      freopen("B-large.in","r",stdin);
      freopen("a.out","w",stdout);
      
      int t;
      cin>>t;
      for(int u=1;u<=t;u++){
              string s,ans;
              cin>>s;
              for(int i=0;i<s.size();i++)
                      s[i]-='0';
                      
              
              
              for(int i=s.size()-2;i>=0;i--){
                      if(s[i]>s[i+1]){
                           s[i]--;
                           for(int j=i+1;j<s.size();j++)s[j]=9;                
                      }
              }
              for(int i=0;i<s.size();i++){
                      if(s[i]>0 || ans.size())ans+=char(s[i]+'0');
              }
              
              
              
              cout<<"Case #"<<u<<": "<<ans<<endl;
              
      }
}
