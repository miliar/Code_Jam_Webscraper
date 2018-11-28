#include<cstdio>
#include<cstring>
#include<queue>

using namespace std;

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int ncase = 0; ncase < ncases; ncase++) {
    int n, k;
    scanf("%d%d", &n, &k);
    priority_queue<int> Q;
    Q.push(n);
    for (int i = 0; i < k-1; i++) {
      int v = Q.top();
      Q.pop();
      int v1 = (v - 1) / 2;
      int v2 = v1;
      if (v1 + v2 < v-1)
        v2++;
      Q.push(v1);
      Q.push(v2);
    }
    int v = Q.top();
    printf("Case #%d: %d %d\n", ncase+1, v/2, (v-1)/2);
  }
  return 0;
}

