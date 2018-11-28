#include<iostream>
using namespace std;
int main(){
  int t,count;
  string pan;
  cin>>t;
  int i=1,limit,length;
  while(i<=t){
    cin>>pan;
    cin>>limit;
    length=pan.length();
    count=0;
    for(int j=0;j<=length-limit;j++){
      if(pan[j]=='-'){
        count++;
        for(int k=0;k<limit;k++){
          if(pan[k+j]=='-')
            pan[k+j]='+';
          else
            pan[k+j]='-';
        }
      }
    }
    bool fl=false;
    for(int j=length-limit+1;j<length;j++){
      if(pan[j]=='-'){
          fl=true;
          break;
      }
    }
    if(fl){
      cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }
    else{
      cout<<"Case #"<<i<<": "<<count<<endl;
    }
    i++;
  }
  return 0;
}
