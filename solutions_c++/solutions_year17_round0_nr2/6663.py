#include<bits/stdc++.h>
using namespace std;

void solve(){
  int index=-1;
  string s;
  cin>>s;
  
  if(s.size()==1){
    cout<<s<<endl;
    return;
  }
  
  for(int i=0;i+1<(int)s.size();i++){
    if(s[i]>s[i+1]){
      index=i;
      break;
    }
  }
  if(index==-1){
    cout<<s<<endl;
    return;
  }

  if(index==0 && s[0]=='1'){
    for(int i=0;i+1<(int)s.size();i++)cout<<'9';
    cout<<endl;
    return;
  }
  
  if(index==0 || s[index-1] < s[index] ){
    s[index]--;
    for(int i=index+1;i<(int)s.size();i++)
      s[i]='9';
    cout<<s<<endl;
    return;
  }
  int si=index;
  while(si>=0&&s[si]==s[index])si--;
  si++;

  s[si]--;
  for(int i=si+1;i<(int)s.size();i++)
    s[i]='9';
  cout<<s<<endl;

}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    cout<<"Case #"<<tc<<": ";
    solve();
  }
  return 0;
}
