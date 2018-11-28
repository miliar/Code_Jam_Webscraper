#include<iostream>
using namespace std;
int main(){
   int n,t;
   cin>>t;
   for(int x=0;x<t;++x) {
      cin>>n;
      for(int i=n;i>=0;--i){
         int b,flag=1,j=i;
         int prev=j%10;
         j=j/10;
         while(j!=0){
               
               
            b=j%10;
            if(b>prev){
               flag=0;
               break;
            }
            prev=b;
            j=j/10;
            
         }
            if(flag==1) {
               cout<<"Case #"<<(x+1)<<": "<<i<<endl;
               break;
            }
      }
      
   }
   return 0;
}
