#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>

int T;
unsigned long long int N;
std::vector<int> digit;

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int i = 1; i <= T; i++) {
     std::cin >> N;
     unsigned long long int tmp = N;
     digit.clear();
     while (tmp > 0) {
        digit.insert(digit.begin(), tmp % 10);
        tmp = tmp / 10;
     }
     std::vector<int> result(digit.size());
     int prev = -1;
     for (int j = 0; j < digit.size(); ++j) {
        int cur = digit[j];
        if (prev <= cur) { 
           result[j] = cur;
           prev = cur;
        }
        else {
           int pos = j - 1;
           while ((pos > 0) && (digit[pos - 1] == prev))
              pos--;
           result[pos]--;
           for (int l = pos + 1; l < digit.size(); l++)
              result[l] = 9;
           break;
        }
     }
     std::cout << "Case #" << i << ": ";
     for (int j = 0; j < result.size(); j++)
        if (result[j] > 0)
           std::cout << result[j];
     std::cout << std::endl;
  }
  return 0;
}

