#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
typedef long long lli;

void PrintAns(int n, string ans){
  std::cout << "Case #" << n + 1 << ": " << ans << std::endl;
}

bool isOk(string s){
  if(s[0] <= '0')return false;
  string tmp = s;
  sort(s.begin(), s.end());
  return s == tmp;
}

int main(){
  int t;
  std::cin >> t;
  for (int r = 0; r < t; r++) {
    lli n;
    std::cin >> n;
    while(n > 0){
      if(isOk(to_string(n)))break;
      n--;
    }
    PrintAns(r, to_string(n));
  }
  return 0;
}
