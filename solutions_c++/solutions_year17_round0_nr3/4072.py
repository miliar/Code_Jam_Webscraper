#include <stdio.h>
#include <queue>

int main()
{
   int t, cas;
   scanf("%d", &t);
   for (cas = 1; cas <= t; cas++)
   {
      int n, k;
      int small, large;
      std::priority_queue<int> pq;
      scanf("%d %d", &n, &k);
      pq.push(n);
      while (k--)
      {
         int v = pq.top();
         pq.pop();
         small = (v - 1) / 2;
         large = v / 2;
         if (small)
            pq.push(small);
         if (large)
            pq.push(large);
      }
      printf("Case #%d: %d %d\n", cas, large, small);
   }
   return 0;
}
