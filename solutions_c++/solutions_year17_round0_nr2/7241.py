#include<iostream>

using namespace std;

string inp;

void strip(){
  while(inp[0]=='0'){
    inp.erase(inp.begin());
  }
}

void ans(){
  if(inp.size()==1){
    return;
  }
  int i,j;
  for(i=(int)inp.size()-1;i>=0;i--){
    if(inp[i]<inp[i-1]){
      inp[i-1]--;
      for(j=i;j<(int)inp.size();j++){
        inp[j]='9';
      }
    }
  }
}

int main(){
  int t;
  cin>>t;
  for(int zz=1;zz<=t;zz++){
    cin>>inp;
    ans();
    strip();
    cout<<"Case #"<<zz<<": "<<inp<<endl;
  }
  return 0;
}
