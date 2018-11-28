#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
main(){
      freopen("A-large.in","r",stdin);
      freopen("a.out","w",stdout);
      
      int t;
      cin>>t;
      for(int u=1;u<=t;u++){
              string s;
              int x,k=0;
              cin>>s>>x;   
              
              for(int i=0;i<s.size()-x+1;i++)
                      if(s[i]=='-'){
                            k++;
                            for(int j=i;j<i+x;j++)
                                    if(s[j]=='-')s[j]='+';else
                                                   s[j]='-';
                      }
              for(int i=0;i<s.size();i++)
                      if(s[i]=='-')k=-1;
                      
                      
              cout<<"Case #"<<u<<": ";
              
              if(k==-1)cout<<"IMPOSSIBLE"<<endl;else
                        cout<<k<<endl;
      }
}
