#include <bits/stdc++.h>
using namespace std;

vector<long long int> nonDecreasingNums;

void generateNonDecreasing(long long int num, long long int depth) {
  if (depth == 0) {
    nonDecreasingNums.push_back(num);
    return;
  }
  int lastNum = num % 10;
  for (int i = lastNum; i <= 9; i++) {
    generateNonDecreasing(num * 10 + i, depth - 1);
  }
}

int main() {
  for (int i = 0; i < 18; i++) {
    for (int j = 1; j <= 9; j++) {
      generateNonDecreasing(j, i);
    }
  }
  sort(nonDecreasingNums.begin(), nonDecreasingNums.end());
  // for (int i = 0; i < nonDecreasingNums.size(); i++) {
  //   cout << nonDecreasingNums[i] << endl;
  // }
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    long long int n;
    cin >> n;
    long long int left = 0, right = nonDecreasingNums.size() - 1, ans = 0;
    while (left <= right) {
      long long int mid = left + (right - left) / 2;
      // cout << "mid " << nonDecreasingNums[mid] << " n " << n << " compare " << (nonDecreasingNums[mid] <= n) << endl;
      if (nonDecreasingNums[mid] <= n) {
        left = mid + 1;
        ans = nonDecreasingNums[mid];
      } else {
        right = mid - 1;
      }
    }
    cout << "Case #" << i << ": " << ans << endl;
  }
}