#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int t;
string s;
int main() {
  ios::sync_with_stdio(false);
  cin>>t;
  for(int cislo=1;cislo<=t;cislo++){
    cin>>s;
    if(s.size()==1){cout <<"Case #"<<cislo<<": "<<s<<endl;continue;}
    int index=-1;
    for(int i=1;i<s.size();i++){
      if(s[i]<s[i-1]){index=i;break;}
    }
    if(index==-1){cout <<"Case #"<<cislo<<": "<<s<<endl;continue;}
    for(int i=index-1;i>=0;i--){
      if(i==0 || s[i-1]<=s[i]-1){
        string str=s;str[i]--;
        for(int j=i+1;j<s.size();j++)str[j]='9';
        cout <<"Case #"<<cislo<<": ";
        for(int j=0;j<str.size();j++)if(!(j==0 && str[j]=='0'))cout <<str[j];
        cout <<endl;
        break;
      }
    }
  }
  return 0;
}