#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

long ones(int size) {
  long l = 1;
  for (int i = 0; i < size - 1; ++i) {
    l = l * 10l + 1l;
  }
  return l;
}

long nines (int size) {
  long l = 9;
  for (int i = 0; i < size - 1; ++i) {
    l = l * 10l + 9l;
  }
  return l;
}

int main(int argc, char* argv[]) {
  int k;
  cin >> k;
  for (int i = 0; i < k; ++i) {
    string number;
    cin >> number;
    long n = atol(number.c_str());
    int size = number.size();
    long bound = ones(size);
    if (n < bound) {
      cout << "Case #" << i + 1 << ": " << nines(size - 1) << endl;
    } else {
      int smallest = number[0] - '0';
      int run_start = 0;
      for (int j = 0; j < number.size(); ++j) {
        if (number[j] - '0' < smallest) {
          number[run_start] = number[run_start] - 1;
          for (int l = run_start + 1; l < number.size(); ++l) {
            number[l] = '9';
          }
          break;
        } else if (number[j] - '0' > smallest) {
          run_start = j;
          smallest = number[j] - '0';
        }
      }
      cout << "Case #" << i + 1 << ": " << number << endl;
    }
  }
}
