#include <iostream>
#include <string>

void print (std::string s) {
  int z = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] != '0') {
      z = i;
      break;
    }
  }
  for (int i = z; i < s.length(); i++) {
    std::cout << s[i] ;
  }
  std::cout << std::endl;
}

void solve (std::string s) {
  int rmi = -1;
  for (int i = s.length()-2; i >= 0; i--) {
    for (int j = i + 1; j < s.length(); j++) {
      if (s[i] > s[j]) {
        rmi = i;
      }
    }
    if (rmi != -1) break;
  }
  if (rmi == -1) {
    print(s);
  } else { 
    s[rmi] -= 1;
    for (int i = rmi + 1; i < s.length(); i++) {
      s[i] = '9';
    }
    solve(s);
  }
}

int main () {
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    std::string s;
    std::cin >> s;
    std::cout << "Case #" << i+1 <<": ";
    solve(s);
  }
}
