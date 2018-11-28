#include <iostream>
#include <string>

using namespace std;

string solve(string s);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    string s;
    cin>>s;
    cout<<"Case #"<<i+1<<": "<<solve(s)<<'\n';
  }
}

string solve(string s){
  for(int i=s.size()-1;i>0;i--)
    if(s[i]<s[i-1]){
      for(int j=i;j<s.size();j++)
        s[j]='9';
      s[i-1]--;
    }
  int prefix=0;
  while(prefix<s.size() && s[prefix]=='0') prefix++;
  return s.substr(prefix);
}
