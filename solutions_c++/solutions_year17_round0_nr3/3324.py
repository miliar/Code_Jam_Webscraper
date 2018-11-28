#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <string>
#include <cassert>
using namespace std;

class level {
public:
  unsigned long long num;
  unsigned long long count;
  level(): num(0), count(0) {}
  level(unsigned long long n, unsigned long long c) : num(n), count(c) {}
};

void solution(unsigned long long &N, unsigned long long &K, unsigned long long &max, unsigned long long &min) {
  level big(N, 1);
  level small;
  int carry = 0;
  unsigned long long minCount = 0, maxCount = 0, temp;
  while(K > big.count + small.count) {
      K = (K - big.count - small.count);
      // bigger grow first
      carry = ((big.num - 1) % 2);
      min = ((big.num - 1) / 2);
      max = min + carry;
      if (min == max) {
        maxCount += (big.count * 2);
      } else {
        maxCount += big.count;
        if (min > 0)
          minCount += big.count;
      }
      // then smaller grow
      if (small.num > 0) {
        carry = ((small.num - 1) % 2);
        //assert (min == ((small.num - 1) / 2));
        min = ((small.num - 1) / 2);
        temp = min + carry;
        assert (min == temp || temp == max);
        if (min == temp) {
          minCount += (small.count * 2);
        } else {
          maxCount += small.count;
          if (min > 0)
          minCount += small.count;
        }
      }
      // assign new values
      big.num = max;
      big.count = maxCount;
      small.num = min;
      small.count = minCount;
      maxCount = 0;
      minCount = 0;
  }

  // update result
  if (K <= big.count) {
    carry = ((big.num - 1) % 2);
    min = ((big.num - 1) / 2);
    max = min + carry;
  } else {
    carry = ((small.num - 1) % 2);
    min = ((small.num - 1) / 2);
    max = min + carry;
  }
}

int main() {
    int T;
    unsigned long long N, K, max, min;
    cin >> T;
    for ( int i = 0; i < T; i++) {
        cin >> N;
        cin >> K;
        solution(N, K, max, min);
        cout << "Case #" << i+1 <<": " << max << " " << min << endl;
    }
    return 0;
}
