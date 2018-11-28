#include <bits/stdc++.h>

using namespace std;

int main(){
  int t;
  int k;
  string s;
  cin>>t;
  bool possible;
  int count;
  int caso=1;
  while(t--){
    cin>>s;
    cin>>k;
    count = 0;
    possible = true;
    cout<<"Case #"<<caso++<<": ";
    for(int i=0;i<s.size() && possible;i++){
      if(s[i]=='-'){
        count++;
        for(int j=i;j<i+k;j++){
          if(j==s.size()){
            possible=false;
            break;
          }
          if(s[j]=='-')
            s[j]='+';
          else
            s[j]='-';
        }
      }
    }
    if(possible)
      cout<<count;
    else
      cout<<"IMPOSSIBLE";
    cout<<endl;
  }
  return 0;
}