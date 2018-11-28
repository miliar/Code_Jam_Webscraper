#include<iostream>
using namespace std;


int main(){

int t,k,count,j,flag;
cin>>t;
string s;

for(int i=0;i<t;i++){
    
      cin>>s>>k; 
      count = 0;
      flag = 1;

  
    for(j=0;j<s.length()-k+1;j++){

         if(s[j]=='-'){
             count+=1;
             for(int m=0;m<k;m++){
                  if(s[j+m]=='-')
                      s[j+m]='+';
                 else
                     s[j+m]='-';
             }
         }
         
    }
     for(int m=0;m<k-1;m++){
                  if(s[j+m]=='-'){
                      flag=0;
                      cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
                      break;
                  }
                     
             }
    if(flag==1)
    cout<<"Case #"<<i+1<<": "<<count<<endl;
   

 }








return 0;
}
