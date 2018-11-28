#include <stdio.h>
#include <algorithm>
#include <queue>
#define l first
#define r second
using namespace std;

class cmp
{
  public:
  bool operator () (const pair<int, int>&a, const pair<int, int>&b)
  {
    if(a.r - a.l == b.r - b.l)
     return a.l > b.l;
    return (a.r - a.l) < (b.r - b.l);
  }
};

int main()
{
  int T;
  FILE *in = fopen("C-small-2-attempt0.in", "r"), *out = fopen("output.txt", "w");

  fscanf(in, "%d", &T);
  for(int t=0; t<T; t++)
  {
    int N, K;
    fscanf(in, "%d%d", &N, &K);
    priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> Q;
    Q.push({0, N-1});

    for(int i=0; i<K; i++)
    {
      pair<int, int> act = Q.top();
      Q.pop();

      int mid = (act.l + act.r) / 2;

      if(i == K-1)
      {
        int ls = mid - act.l;
        int lr = act.r - mid;
        fprintf(out, "Case #%d: %d %d\n", (t+1), max(ls, lr), min(ls, lr));
      }

      if(act.l != act.r)
      {
        Q.push({act.l, mid-1});
        Q.push({mid+1, act.r});
      }
    }
  }

  fclose(in);
  fclose(out);
  return 0;
}
