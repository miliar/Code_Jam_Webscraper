#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>

using namespace std;
typedef pair<int,int> ii;

void bfs(int n, multiset<ii> &S) {
  int i = 0, v;
  queue<int> qq;
  qq.push(n);

  while (!qq.empty()) {
    v = qq.front() - 1;
    qq.pop();
    S.insert(ii((int) ceil(v/2.0), (int) floor(v/2.0)));
    if (((int) ceil(v/2.0)) && ((int) floor(v/2.0))) {
      qq.push((int) ceil(v/2.0));
      qq.push((int) floor(v/2.0));
    }
  }
}

int main() {
  int t, n, k;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &n, &k);

    multiset<ii> S;
    bfs(n, S);
    while (S.size() < k)
      S.insert(ii(0, 0));

    ii a;
    int i = 0;
    for (multiset<ii>::reverse_iterator it = S.rbegin(); i < k; ++it, ++i)
      a = *it; 
    printf("Case #%d: %d %d\n", cas, a.first, a.second);
  }
  return 0;
}
