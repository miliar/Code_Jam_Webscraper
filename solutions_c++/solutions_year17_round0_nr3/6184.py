#include<iostream>
#include<queue>

using namespace std;

priority_queue<int> inp;

int main(){
  int a,b,t,i,j;
  int n,k;
  cin>>t;
  for(int zz=1;zz<=t;zz++){
    cin>>n;
    cin>>k;
    k--;
    inp.push(n);
    for(i=1;i<=k;i++){
      if(inp.top()>2){
        a=(inp.top()-1)/2;
        b=inp.top()-1-a;
        inp.pop();
        inp.push(a);
        inp.push(b);
      }
      else if(inp.top()==2){
        inp.pop();
        inp.push(1);
      }
      else{
        inp.pop();
        inp.push(0);
      }
    }
    cout<<"Case #"<<zz<<": ";
    if(inp.top()<=1){
      cout<<"0 0";
    }
    else if(inp.top()==2){
      cout<<"1 0";
    }
    else{
      a=(inp.top()-1)/2;
      b=inp.top()-1-a;
      cout<<b<<" "<<a;
    }
    cout<<endl;
    while(inp.size()){
      //cout<<inp.top()<<" ";
      inp.pop();
    }
  }
  return 0;
}
