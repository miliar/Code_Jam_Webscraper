#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

priority_queue<long long> chunks;

struct distances {
  long long minlr;
  long long maxlr;
};

distances solve(long long n, long long k) {
  chunks.push(n);
  long long last;
  while (k) {
    k--;
    last = chunks.top();
    chunks.pop();
    if (last > 1 && last % 2) {
      chunks.push(last / 2);
      chunks.push(last / 2);
    } else if (last % 2 == 0) {
      if (last == 2) {
        chunks.push(1);
      } else {
        chunks.push(last / 2);
        chunks.push(last / 2 - 1); 
      }
    }
  }

  // Compute Ls and Rs.
  long long left, right;
  if (last % 2) {
    left = right = last / 2;
  } else {
    left = last / 2 - 1;
    right = last / 2;
  }

  distances result;
  result.minlr = min(left, right);
  result.maxlr = max(left, right); 
  return result;
}

void clear() {
  while (!chunks.empty()) {
    chunks.pop();
  }
}

int main() {
  int tests;
  long long n, k;
  distances solution;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++) {
    scanf("%lld %lld", &n, &k);
    solution = solve(n, k);
    printf("Case #%d: %lld %lld\n", i, solution.maxlr, solution.minlr);
    clear();
  }
}