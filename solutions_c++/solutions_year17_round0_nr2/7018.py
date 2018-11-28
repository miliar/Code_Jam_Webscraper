#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

long long n;
vector<long long> all;

void trY(int index, long long number) {
  all.push_back(number);

  if(index == 18)
    return;

  int mod = number % 10;

  for(int i = mod; i <= 9; i++)
    trY(index + 1, number * 10 + i);
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, index;
  scanf("%d", &t);

  trY(0, 0);
  sort(all.begin(), all.end());
  all.resize(unique(all.begin(), all.end()) - all.begin());

  for(int c = 1; t--; c++) {
    scanf("%lld", &n);
    index = lower_bound(all.begin(), all.end(), n) - all.begin();

    if(all[index] != n)
      index--;

    printf("Case #%d: %lld\n", c, all[index]);
  }

  return 0;
}
