#include <stdio.h>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;
const int N=1010;

struct Node {
  double r, h;
}nodes[N];

bool cmp1(const Node &a, const Node &b) {
  if(a.r!=b.r) return a.r>b.r;
  return a.h > b.h;
}

bool cmp2(const Node &a, const Node &b) {
  return a.h * a.r > b.h * b.r;
}


double get(int id, int n, int k) {
  vector<Node> tmp;
  double PI = acos(-1);
  double sum = nodes[id].r * nodes[id].h * 2 * PI+PI*nodes[id].r*nodes[id].r;
  for (int i = id + 1; i < n; i++) {
    tmp.push_back(nodes[i]);
  }
  if (tmp.size() < k - 1) return 0;
  sort(tmp.begin(), tmp.end(), cmp2);
  for (int i = 0; i < k - 1; i++) {
    sum += tmp[i].r * tmp[i].h * 2 * PI;
  }
  return sum;
}

double solve(int n, int k)
{
  sort(nodes, nodes+n, cmp1);
  double ans(0.0);
  for (int i = 0; i < n; i++) {
    ans = max(ans, get(i, n, k));
  }
  return ans;
}

int main() 
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int test,cas(1);
  scanf("%d",&test);
  while (test--) {
    int n,k;
    scanf("%d%d",&n,&k);
    for (int i = 0; i < n; i++) {
      scanf("%lf%lf",&nodes[i].r,&nodes[i].h);
    }
    printf("Case #%d: %.10f\n", cas++,solve(n,k));
  }
  return 0;
}

/* sw=2;ts=2;sts=2;expandtab */
