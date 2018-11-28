#include <iostream>
#include <string>
std::string number;
int main() {
  int t;
  std::cin >> t;
  for(int i = 0; i < t; i++) {
    std::cin >> number;
    std::cout << "Case #" << i + 1 << ": ";
    int first_dec = -1;
    for(int j = 1; j < number.size(); j++) {
      if (number[j-1] > number[j]){
        first_dec = j;
        break;
      }
    }
    if (first_dec == -1) {
      std::cout << number << "\n";
      continue;
    }
    int first_eq = first_dec - 1;
    for(int j = first_dec - 2; j>= 0; j--) {
      if (number[j] != number[j+1]) {
        break;
      }
      first_eq--;
    }
    number[first_eq]--;
    for(int j = first_eq+1; j < number.length(); j++)
      number[j] = '9';
    if (number[0] == '0')
      number.erase(number.begin());
    std::cout << number << "\n";
  }
}
