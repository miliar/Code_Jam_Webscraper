// Author: James W. Hegeman
#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;

class BathroomInterval {
 public:
  int64_t left_end;
  int64_t right_end;
  int64_t length;

  BathroomInterval() {
    left_end = 0;
    right_end = 0;
    length = 0;
  }

  BathroomInterval(int64_t l, int64_t r) {
    left_end = l;
    right_end = r;
    length = r - l + 1;
  }

  BathroomInterval(const BathroomInterval& other) {
    left_end = other.left_end;
    right_end = other.right_end;
    length = other.length;
  }

  BathroomInterval(BathroomInterval&& other) {
    left_end = other.left_end;
    right_end = other.right_end;
    length = other.length;
  }

  BathroomInterval& operator=(const BathroomInterval& other) {
    left_end = other.left_end;
    right_end = other.right_end;
    length = other.length;
    return *this;
  }

  BathroomInterval& operator=(BathroomInterval&& other) {
    left_end = other.left_end;
    right_end = other.right_end;
    length = other.length;
    return *this;
  }
};

class BathroomIntervalCompare {
 public:
  bool operator()(BathroomInterval lhs, BathroomInterval rhs) {
    int64_t l = lhs.length;
    int64_t r = rhs.length;
    if (l < r) {
      return true;
    } else if (l > r) {
      return false;
    } else {
      if (lhs.left_end > rhs.left_end) {
        return true;
      } else {
        return false;
      }
    }
  }
};

int main(int argc, char *argv[]) {
  int64_t T, N, K, L, R, max, min;

  cin >> T;
  for (int64_t i = 1; i <= T; ++i) {
    priority_queue<BathroomInterval, vector<BathroomInterval>, BathroomIntervalCompare> heap;
    cin >> N;
    cin >> K;

    heap.emplace(1, N);
    for (int64_t k = 1; k <= K; ++k) {
      BathroomInterval w = heap.top();
      int64_t l = w.left_end;
      int64_t r = w.right_end;
      int64_t s = (l + r) / 2;
      heap.pop();
      if (s > l) {
        heap.emplace(l, s - 1);
      }
      if (s < r) {
        heap.emplace(s + 1, r);
      }
      L = s - l;
      R = r - s;
    }

    max = (L < R) ? R : L;
    min = (L < R) ? L : R;
    cout << "Case #" << i << ": " << max << " " << min << endl;
  }

  return 0;
}
