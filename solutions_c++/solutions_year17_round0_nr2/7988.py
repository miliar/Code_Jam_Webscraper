#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int isDesc(string number) {
  for (int i = 1; i < number.size(); i++) {
    if (number[i - 1] > number[i]) {
      return i - 1;
    }
  }
  return -1;
}

int main () {
  long long t;
  cin >> t;
  string number;
  for (int j = 0; j < t; j++) {
    cin >> number;
    while (isDesc(number) > -1) {
      int wrongDigit = isDesc(number);
      number[wrongDigit] = number[wrongDigit] - 1;
      for (int k = wrongDigit + 1; k < number.size(); k++) {
	number[k] = '9';
      }
    }
    int begining = 0;
    while (number[begining] == '0') {
      begining ++;
    }
    cout << "Case #" << j + 1 << ": ";
    for (int i = begining; i < number.size(); i++) {
      cout << number[i];
    }
    cout << endl;
  }
}