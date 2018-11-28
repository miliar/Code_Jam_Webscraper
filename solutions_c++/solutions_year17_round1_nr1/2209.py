#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin>>n;
  int a,b;
  bool done;
  char temp;
  for(int i=0;i<n;i++){
    cin>>a>>b;
    cerr<<a<<" "<<b<<endl;
    vector<string> str;
    for(int j=0;j<a;j++){
      string s;
      cin>>s;
      str.push_back(s);
    }
    for(int j=0;j<a;j++){
      for(int p=1;p<b;p++){
        if(str[j][p]=='?')str[j][p]= str[j][p-1];
      }
      for(int p=b-2;p>=0;p--){
        if(str[j][p]=='?')str[j][p]= str[j][p+1];
      }
    }
    
    for(int j=0;j<b;j++){
      for(int p=1;p<a;p++){
        if(str[p][j]=='?')str[p][j]= str[p-1][j];
      }
      for(int p=a-2;p>=0;p--){
        if(str[p][j]=='?')str[p][j]= str[p+1][j];
      }
    }
    cout<<"Case #"<<i+1<<":\n";
    for(int j=0;j<a;j++){
      for(int p=0;p<b;p++){
        cout<<str[j][p];
      }
      cout<<endl;
    }
  }
  return 0;
}