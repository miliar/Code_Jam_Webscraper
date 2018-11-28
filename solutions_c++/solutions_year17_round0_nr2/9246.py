#include<iostream>
#include<string.h>
using namespace std;

int main(){
  int t=0,l=0,n=0;
  bool flg=true;
  string num="";
  cin>>t;
  while(n<t){
    cin>>num;
    while(num>"0"){
      l=num.length();
      flg=true;
      for(int i=0;i<l-1;i++){
        if(!(num[i]<=num[i+1])){
          num[i]=num[i]-1;
          for(int j=i;j<l-1;j++)
            num[j+1]='9';
          flg=false;
        }
      }
      if(flg){
        cout<<"Case #"<<n+1<<": ";
        for(int i=0;i<l;i++){
          if(num[i]>'0'){
            cout<<num[i];
          }
        }
        cout<<endl;
        break;
      }
    }
    n++;
  }
}
