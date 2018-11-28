#include<bits/stdc++.h>
using namespace std;

bool isTidy(string s){
  int len = s.length();
  for(int i=len-1; i>0; i--){
    if(s[i]<s[i-1])
      return false;
  }
  return true;
}
int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    string num = "0123456789";
    int tt;
    cin>>tt;
    for(int qq=1;qq<=tt;qq++){
        string s;
        cin>>s;
        int len = s.length();
        cout<<"Case #"<<qq<<": ";
        if(len<=1 || isTidy(s)){
          cout<<s<<endl;
          continue;
        }
        for(int i=len-1; i>0; i--){
          if(isTidy(s)){
            break;
          }
          if(s[i] <= s[i-1]){
            for(int j=i;j<len;j++)
              s[j] = '9';
            s[i-1] = (char)((int)s[i-1] - 1);
          }
        }
        if (s[0] == '0') s = s.erase(0, 1);
        cout<<s<<endl;
    }
    return 0;
}
