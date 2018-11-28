#include <bits/stdc++.h>
using namespace std;

bool check(string str){
  for(int i=0;i<str.size();i++)if(str[i]=='-') return 0;
  return 1;
}

int main(){
  int q,cnt=0;
  cin>>q;

  while(q--){
    string str;
    cin>>str;
    int K;
    cin>>K;
    int ans = 0;
    for(int i=0;i<str.size();i++){
      if(str[i]=='+'||i+K>str.size())continue;
      ans++;
      for(int j=i;j<i+K;j++)str[j] = str[j]=='+'? '-':'+';
    }
    if(check(str))cout<<"Case #"<<++cnt<<": "<<ans<<endl;
    else cout<<"Case #"<<++cnt<<": IMPOSSIBLE"<<endl;
  }
  return 0;
}
