#include <iostream>
#include <set>
using namespace std;

int main() {
  int T;
  int N, K, answer;
  scanf("%d", &T);
  multiset<int> s;
  multiset<int>::iterator it;
  for (int i = 0; i < T; i++) {
    scanf("%d%d", &N, &K);
    s.clear();
    s.insert(N);
    int currentVal;
    while (K--) {
      it = s.end();
      it--;
      currentVal = *it;
      s.erase(it);
      if (currentVal % 2 == 0) {
        s.insert(currentVal / 2 - 1);
        if (s.size() > K) s.erase(s.begin());
        s.insert(currentVal / 2);
        if (s.size() > K) s.erase(s.begin());
      } else {
        s.insert(currentVal / 2);
        if (s.size() > K) s.erase(s.begin());
        s.insert(currentVal / 2);
        if (s.size() > K) s.erase(s.begin());
      }
    }
    printf("Case #%d: %d %d\n", i + 1, currentVal / 2, (currentVal % 2 == 0 && currentVal > 0)? (currentVal/2 - 1): currentVal/2);
  }
  return 0;
}