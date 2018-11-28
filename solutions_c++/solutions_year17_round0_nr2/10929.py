#include <iostream>
#include <math.h>  
using namespace std;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w" , stdout);
  int t, n, temp, res, cur, count, prev, digits;
  cin >> t;
  t++;
  for (int i = 1; i < t; i++) {
    cin >> n;
    temp = n;
    res = 0;
    cur = n % 10;
    temp = n / 10;
    count = 0;
    digits = 1;
    
    
    while (temp > 0) {
      prev = cur;
      cur = temp % 10;
      temp = temp / 10;
      if (cur > prev) {
        count = digits;
        cur--;
      }
      digits++;
    }
    
    
    temp = n;
    for (int k = 0; k < count; k++) {
      res = res * 10 + 9;
      temp /= 10;
    }

    if (count != 0) res = (temp - 1) * pow(10, count) + res;
    else res = n;
    
    cout << "Case #" << i << ": " << res << "\n";
  }
  
  return 0;
}