#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
string s;
int n;
int go(int a,int b,int c,char A,char B,char C){
   string s1;  
   for(int i=0;i<n;i++)s1+=' ';
   
   
   for(int i=0;i<n;i+=2){
           if(!a)break;
           s1[i]=A;
           a--;
   }
   
   for(int j=n-1;j>=0;j--){
           if(!b)break;
           
           if(s1[j]!=' ')continue;
           s1[j]=B;
           b--;
           j--;        
   }
   for(int i=0;i<n;i++){
           if(!c)break;
           if(s1[i]!=' ')continue;
           
           s1[i]=C;
           c--;
           i++;
   }
   if(a+b+c>0)return 0;
   s=s1;
   return 1;
}
main(){
      freopen("a.in","r",stdin);
      freopen("a.out","w",stdout);
      
      int t;
      cin>>t;
      for(int u=1;u<=t;u++){
              
              int r,o,y,g,b,v;
              cin>>n>>r>>o>>y>>g>>b>>v;
              
              if(max(r,max(y,b))>n/2){
                                          cout<<"Case #"<<u<<": ";
                                          cout<<"IMPOSSIBLE"<<endl;
                                          continue;
              }
              
              
              
              if(y>=max(r,b) && r>=b && go(y,r,b,'Y','R','B'));else
              if(y>=max(b,r) && b>=r && go(y,b,r,'Y','B','R'));else
              
              if(r>=max(y,b) && y>=b && go(r,y,b,'R','Y','B'));else
              if(r>=max(b,y) && b>=y && go(r,b,y,'R','B','Y'));else
              
              if(b>=max(r,y) && r>=y && go(b,r,y,'B','R','Y'));else
              if(b>=max(y,r) && y>=r && go(b,y,r,'B','Y','R'));else{
                             
                                          cout<<"Case #"<<u<<": ";
                                          cout<<"IMPOSSIBLE"<<endl;
                                          continue;               
              }
              
              
              
                      
              cout<<"Case #"<<u<<": ";
              cout<<s<<endl;
      }
}
