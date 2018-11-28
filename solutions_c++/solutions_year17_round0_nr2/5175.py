#include <bits/stdc++.h>

using namespace std;

bool isTidy(long long num, int lastDigit = 10) {
  return (num == 0 || num % 10 <= lastDigit && isTidy(num / 10, num % 10));
}

int naive(int num) {
  while (!isTidy(num)) {
    num--;
  }
  return num;  
}

int main() {
  int t;
  cin >> t;  
  for (int i = 0; i < t; i++) {
    long long n;
    cin >> n;    
    long long num = n;
    long long res = -1;
    if (isTidy(num)) {
      res = num;
    } else {
      while (num > 0) {
        num--; 
        long long number = num;
        while (number < double(n - 9) / 10) {
          number = number * 10 + 9;
        }        
        if (isTidy(number)) {
          res = number;
          break;
        }
        num++;
        num /= 10;
      }      
    }        
    cout << "Case #" << i + 1 << ": " << res << endl;
  }
  return 0;
}
