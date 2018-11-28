#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> vs;

void gen(int d, long long v){
  if(d == 18){ vs.push_back(v); return ; }
  int x = v % 10;
  for(int i = x; i <= 9; i++) gen(d + 1, v * 10 + i);
}

int main(){
  gen(0, 0);

  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    printf("Case #%d: ", tt);

    long long N; scanf("%lld", &N);

    auto it = upper_bound(vs.begin(), vs.end(), N); it--;
    printf("%lld\n", *it);
  }
  return 0;
}
