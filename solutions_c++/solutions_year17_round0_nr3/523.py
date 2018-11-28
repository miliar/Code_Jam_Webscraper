#include <cstdio>
#include <map>
using namespace std;
typedef long long int huge;

void add_to(map<huge, huge>& stall, huge value, huge count) {
  if (stall.find(value)==stall.end()) {
    stall.insert(make_pair(value, count));
  }
  else {
    stall[value]+=count;
  }
}

int main() {
  int tests;
  map<huge, huge> stall;
  huge n, k;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:", test_number);
    scanf(" %lld %lld", &n, &k);
    stall.clear();
    stall.insert(make_pair(n, 1));
    while(k>0) {
      huge size = stall.rbegin()->first;
      huge count = stall.rbegin()->second;
      stall.erase(--stall.end());

      if (count >= k) {
	printf(" %lld %lld\n", size/2, (size-1)/2);
	break;
      }
      add_to(stall, size/2, count);
      add_to(stall, (size-1)/2, count);
      k-=count;
    }
  }
  return 0;
}
