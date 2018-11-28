#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
  int t;
  string s;
  cin>>t;
  for(int j=1;j<=t;j++){
    cin>>s;
    int index=0,flg=0;
    if(s.length()==1) flg=1;
    if(!flg){
      while(index<s.length()-1 && s[index]<=s[index+1]) index++;
      int decr=index;
      while(decr>0 && s[decr]==s[decr-1]) decr--;
      if(!(index==s.length()-1 && s[index-1]<=s[index])){
        s[decr]--;
        for(int i=decr+1;i<s.length();i++) s[i]='9';
      }
    }
    long long int ans=0;
    for(int i=0;i<s.length();i++){
      ans= ans*10+(s[i]-'0');
    }
    cout<<"Case #"<<j<<": "<<ans<<endl;
  }
  return 0;
}
