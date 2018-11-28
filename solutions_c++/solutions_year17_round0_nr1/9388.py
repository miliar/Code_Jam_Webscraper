#include<iostream>
#include<string>
using namespace std;

void PrintAns(int n, string ans){
  std::cout << "Case #" << n + 1 << ": " << ans << std::endl;
}

int main(){
  int t, k;
  std::cin >> t;
  for (int r = 0; r < t; r++) {
    string s;
    std::cin >> s >> k;
    int n = s.length();
    int ans = 0;
    for (int i = 0; i <= n - k; i++) {
      if(s[i] != '-') continue;
      ans++;
      for (int j = 0; j < k; j++) {
        if(s[i + j] == '-')s[i + j] = '+';
        else s[i + j] = '-';
      }
    }
    bool f = true;
    for (int i = n - k; i < n; i++) {
      if(s[i] == '+')continue;
      PrintAns(r, "IMPOSSIBLE");
      f = false;
      break;
    }
    if(f)PrintAns(r, to_string(ans));
  }
  return 0;
}

