#include<iostream>
#include<queue>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
main(){
      freopen("C-small-2-attempt0.in","r",stdin);
      freopen("a.out","w",stdout);
      
      int t;
      cin>>t;
      for(int u=1;u<=t;u++){
              int n,k,F=0,ma;
              cin>>n>>k;
              
              
              priority_queue<int>q;
              q.push(n);
              
              for(int i=0;i<k;i++){
                      int to=q.top();
                      ma=to;
                      q.pop();
                      
                      
                      q.push((to-1)/2);
                      q.push(to-(to-1)/2-1);
              }
             // cout<<ma<<endl;
              
              
              
              cout<<"Case #"<<u<<": ";
                    cout<<ma-(ma-1)/2-1<<" "<<(ma-1)/2<<endl;
              
      }
}
