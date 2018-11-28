#include <iostream>
#include <string>
using namespace std;

string doit(string x){
  int m = x.length();
  int j = 0;
  while(j<m-1){
    if (int(x[j]) > int(x[j+1])){
      x[j] = char(int(x[j]) - 1);
      for(int a = j+1; a<m; a++){x[a] = '9';}
    }
    j += 1;
  }
  return x;
}

bool order(string x){
  bool found = true;
  for(int i = 0;i<x.length()-1; i++){
    if (int(x[i]) <= int(x[i+1])) {
      continue;
    }
    else{
      found = false;
      break;
    }
  }
  return found;
}

int main(){
  int t,s;
  string x;
  cin>>t;
  for(int i = 1; i<= t; i++ ){
    cin>>x;
    bool found = false;
    while(!found){
      if (order(x)) {found = true;}
      else {x = doit(x);}
    }
    unsigned long long xx = stoul(x);
    cout<<"Case #"<<i<<": "<<xx<<endl;
  }
}
