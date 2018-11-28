#include <bits/stdc++.h>
using namespace std;

string change(string str){
  for(int i=1;i<str.size();i++){
    if(str[i]<str[i-1]) {
      str[i-1]--;
      for(int j=i;j<str.size();j++)str[j] = '9';
      break;
    }
  }
  return str;
}

int main(){
  int q,cnt=0;
  cin>>q;
  while(q--){
    string str;
    cin>>str;

    while(1){
      string res=change(str);
      if(res==str)break;
      str=res;
    }

    while(str.size()&&str[0]=='0') str.erase(str.begin());
    if(str.size()==0) str=="0";
    cout<<"Case #"<<++cnt<<": "<<str<<endl;
  }
  return 0;
}
