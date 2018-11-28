#include<iostream>
using namespace std;
int main(){
  int t,count;
  string pancakes;
  cin>>t;
  int i=1,limit,length;
  while(i<=t){
    cin>>pancakes;
    cin>>limit;
    length=pancakes.length();
    count=0;
    for(int j=0;j<=length-limit;j++){
      if(pancakes[j]=='-'){
        count++;
        for(int k=0;k<limit;k++){
          if(pancakes[k+j]=='-')
            pancakes[k+j]='+';
          else
            pancakes[k+j]='-';
        }
      }
    }
    bool flag=false;
    for(int j=length-limit+1;j<length;j++){
      if(pancakes[j]=='-'){
          flag=true;
          break;
      }
    }
    if(flag){
      cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }
    else{
      cout<<"Case #"<<i<<": "<<count<<endl;
    }
    i++;
  }
  return 0;
}
