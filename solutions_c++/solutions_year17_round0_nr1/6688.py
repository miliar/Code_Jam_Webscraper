#include<bits/stdc++.h>
using namespace std;

char change(char ch){
  if(ch=='+')return '-';
  return '+';
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    int K,ans=0;
    string s;
    cin>>s>>K;
    for(int i=0;i+K<=(int)s.size();i++){
      if(s[i]=='-'){
        ans++;
        for(int j=i;j<i+K;j++)s[j]=change(s[j]);
      }
    }

    cout<<"Case #"<<tc<<": ";
    if(s.find('-')==string::npos){
      cout<<ans<<endl;
    }else{
      cout<<"IMPOSSIBLE"<<endl;
    }
  }
  return 0;
}

