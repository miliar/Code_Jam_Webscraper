#include <cstdio>
#include <map>
#include <queue>

struct Group {
  long long count;
  long long length;

  bool operator < (const Group &other) const {
    return this->length < other.length;
  }
};

std::map<long long, long long> getCount;
std::priority_queue<long long> lengths;


void addToQueue(long long count, long long length) {
  if (getCount[length] == 0)
    lengths.push(length);
  getCount[length] += count;
}

int main(void) {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    getCount.clear();
    while(!lengths.empty())
      lengths.pop();
    long long n, k;
    scanf("%lld%lld", &n, &k);

    k--;
    addToQueue(1, n);
    while (k >= getCount[lengths.top()]) {
      long long length = lengths.top();
      long long count = getCount[lengths.top()];
      lengths.pop();
      k -= getCount[length];
      if (length % 2 == 1) {
        addToQueue(2 * count, (length - 1) / 2);
      } else {
        addToQueue(count, length / 2);
        addToQueue(count, length / 2 - 1);
      }
    }
    long long length = lengths.top();
    long long max = length / 2;
    long long min = length - 1 - max;
    printf("%lld %lld\n", max, min);
  }
  return 0;
}
