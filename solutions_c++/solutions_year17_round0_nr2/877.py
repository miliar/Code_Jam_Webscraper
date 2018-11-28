#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

deque<int> makeArr(long long N) {
  deque<int> arr;
  while (N > 0) {
    arr.push_front(N % 10);
    N /= 10;
  }
  return arr;
}

long long makeTidy(deque<int> arr) {
  int last = 0;
  int flag = false;
  long long res = 0;
  for (auto i = arr.begin(); i != arr.end(); i++) {
    if (flag) {
      res = res * 10 + 9;
    } else {
      if (*i < last) {
        res--;
        res = res * 10 + 9;
        flag = true;
      } else {
        res = res * 10 + *i;
      }
      last = *i;
    }
  }
  return res;
}

int main() {
  int num;
  cin >> num;
  for (int i = 1; i <= num; i++) {
    long long N;
    cin >> N;
    long long res = N;
    long long prev = N;
    deque<int> arr;
    while (1) {
      prev = res;
      res = makeTidy(makeArr(res));
      if (res == prev) break;
    }
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}
