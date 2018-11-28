#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;

void solve(string s, int i, int r) {
  if(i < 0) {
    int j=0;
    while (s[j]=='0') {
      s.erase(j, 1);
      j++;
    }
    std::cout << s << std::endl;
    return;
  }
  if(r){
    if(s[i]>'0') s[i]-=1,solve(s,i,0);
    else {
      for(int j = i; j<s.length(); j++){
        s[j]='9';
      }
      solve(s,i-1,1);
    }
  }
  else if(s[i]>=s[i-1])
   solve(s, i-1, 0);
  else{
    for(int j = i; j<s.length(); j++){
      s[j]='9';
    };
    solve(s,i-1,1);
  }
}

int t,c=1;
std::string s;
int main(){
  std::cin >> t;
  while (t--) {
    std::cin >> s;
    printf("Case #%d: ", c++);
    solve(s,s.length()-1,0);
  }
}
