#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn=64;
int ingredient[maxn];

int ceil_div(int a, int b) {
  return (a+b-1)/b;
}
int floor_div(int a, int b) {
  return a/b;
}

struct packet {
  int min_servings, max_servings;
  bool operator<(const packet o) const {
    if (min_servings != o.min_servings)
      return min_servings < o.min_servings;
    return max_servings < o.max_servings;
  }
  packet operator&(const packet o) const {
    return packet{max(min_servings, o.min_servings), min(max_servings, o.max_servings)};
  }
  bool valid() {
    return min_servings<=max_servings;
  }
};
packet setup(int contents, int serving) {
  return packet{ceil_div(contents*10, serving*11),
      floor_div(contents*10, serving*9)};    
}

int n, m;
packet mtx[maxn][maxn];
int size[maxn];
bool can_do() {
  packet current{0, 100100100};
  for(int i=0; i<n; ++i) {
    if (size[i]<=0)
      return false;
    current = current & mtx[i][size[i]-1];
    if (!current.valid())
      return false;
  }
  return true;
}
void remove_greatest(){
  int g = 0;
  for(int i=1; i<n; ++i) {
    if (size[i]>0)
      if (mtx[g][size[g]-1] < mtx[i][size[i]-1])
	g=i;
  }
  size[g]--;
}
int main() {
  int tests;
  int total, answer;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:", test_number);
    scanf(" %d %d", &n, &m);
    for(int i=0; i<n; ++i)
      scanf(" %d", &ingredient[i]);
    for(int i=0; i<n; ++i) {
      for(int j=0; j<m; ++j) {
	int tmp;
	scanf(" %d", &tmp);
	mtx[i][j] = setup(tmp, ingredient[i]);
      }
      sort(mtx[i], mtx[i]+m);
      size[i]=m;
    }
    total=n*m;
    answer = 0;
    while(total>0) {
      if (can_do()) {
	total-=n;
	answer++;
	for(int i=0; i<n; ++i)
	  size[i]--;
      }
      else {
	remove_greatest();
	total--;
      }
    }
    printf(" %d\n", answer);
  }
  return 0;
}
