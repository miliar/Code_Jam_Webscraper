#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin>>n;
  for(int i=0;i<n;i++){
    string str;
    int a;
    int res=0;
    cin>>str;
    cin>>a;
    for(int j=0;j<str.length();j++){
      if(str[j]=='-' && j+a>str.length()){
        res=-1;
        break;
      }
      if(str[j]=='-'){
        res++;
        //cout<<"j = "<<j<<endl;
        for(int k=j;k<j+a;k++){
          str[k]=(str[k]=='-'?'+':'-');
        }
      }
    }
    cout<<"Case #"<<i+1<<": ";
    if(res==-1)cout<<"IMPOSSIBLE";
    else cout<<res;
    cout<<endl;
  }
  return 0;
}