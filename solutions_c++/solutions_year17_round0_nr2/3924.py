#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
typedef int64_t i64;

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    i64 N;
    scanf("%lld", &N);
    vector<int> digits;
    while (N > 0) {
      digits.insert(digits.begin(), N % 10);
      N /= 10;
    }

    i64 ans = 1;
    for (i64 i = 0; i <= digits.size(); i++) {
      vector<int> t;
      int highest = 0;
      bool valid = true;
      for (i64 j = 0; j < i; j++) {
        if (digits[j] < highest) {
          valid = false;
        }
        highest = max(highest, digits[j]);
        t.push_back(digits[j]);
      }
      for (i64 j = i; j < digits.size(); j++) {
        if (digits[i]-1 < highest) {
          valid = false;
        }
        if (j == i) {
          t.push_back(digits[i] - 1);
        } else {
          t.push_back(9);
        }
      }
      if (valid) {
        i64 val = 0;
        i64 p10 = 1;
        for (i64 j = t.size() - 1; j >= 0; j--) {
          val += p10 * t[j];
          p10 *= 10;
        }
        ans = max(ans, val);
      }
    }
    i64 val = 0;
    i64 p10 = 1;
    for (i64 i = 0; i < digits.size()-1; i++) {
      val += 9 * p10;
    }
    ans = max(ans, val);

    printf("Case #%lld: %lld\n", zz, ans);
  }
}
