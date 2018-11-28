#include <cstdio>
#include <utility>
#include <vector>
#include <algorithm>

struct Triple {
  int idx, left, right;
};

bool operator<(Triple a, Triple b) {
  int minA = std::min(a.left, a.right);
  int minB = std::min(b.left, b.right);
  int maxA = std::max(a.left, a.right);
  int maxB = std::max(b.left, b.right);
  if (minA == minB) {
    if (maxA == maxB) {
      return a.idx < b.idx;
    }
    return maxA > maxB;
  }
  return minA > minB;
}

const int MX = 1007;

bool used[MX];
int n, k;

std::pair<int, int> compute(int idx) {
  int left = 0;
  int right = 0;

  //printf("kostka jest w idx = %d\n", idx);
  
  for (int i = idx - 1; i >= 0; --i) {
    if (used[i] == true) 
      break;
    ++left;
  }

  for (int i = idx + 1; i <= n + 1; ++i) {
    if (used[i] == true)
      break;
    ++right;
  }

  //printf("kostka znalazł %d %d\n", left, right);
  
  return std::make_pair(left, right);
}

std::pair<int, int> mark() {
  std::vector<Triple> vec;

  for (int i = 1; i <= n; ++i) {
    if (used[i] == false) {
      auto var = compute(i);
      Triple a;
      a.idx = i;
      a.left = var.first;
      a.right = var.second;
      vec.push_back(a);
    }
  }

  std::sort(vec.begin(), vec.end());

  //puts("---");

  //for (auto it : vec) {
  //  printf("{%d %d %d} ", it.idx, it.left, it.right);
  //}

  //puts("---");
  
  used[vec[0].idx] = true;
  return std::make_pair(std::max(vec[0].left, vec[0].right),
      std::min(vec[0].left, vec[0].right));
}

void solve() {
  for (int i = 0; i < MX; ++i) 
    used[i] = false;
  scanf("%d%d", &n, &k);
  used[0] = true;
  used[n + 1] = true;

  for (int i = 1; i < k; ++i)
    mark();

  auto ret = mark();
  printf("%d %d\n", ret.first, ret.second);
}


int main() {
  int q;
  scanf("%d", &q);
  for (int i = 1; i <= q; ++i) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
