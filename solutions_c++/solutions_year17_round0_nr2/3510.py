#include <iostream>

int checkTidy(unsigned long long int n) {
  int n1 = n%10;
  n /= 10;
  int n2 = n%10;
  while (n) {
    if(n1 < n2){
      return 0;
    }
    n1 = n2;
    n /= 10;
    n2 = n%10;
  }
  return 1;
}

void findTidy(unsigned long long int n, int i) {
  while (n>9) {
    if(checkTidy(n)){
      std::cout << "Case #" << i << ": " << n << '\n';
      return;
    }
    n--;
  }

  std::cout << "Case #" << i << ": " << n << '\n';
}

int main() {

  int t;
  unsigned long long int n;
  std::cin >> t;

  for (size_t i = 0; i < t; i++) {
    std::cin >> n;
    findTidy(n,i+1);
  }

  return 0;
}
