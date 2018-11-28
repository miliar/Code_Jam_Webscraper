#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
   int T;
   scanf("%d", &T);
   for(int _i=1; _i<=T; _i++)
   {
      long long n, k;
      scanf("%lld%lld", &n, &k);
      priority_queue<long long> q;
      q.push(n);
      for(int i=0; i<k-1; i++) {
         int t = q.top();
         q.pop();
         q.push(t/2);
         q.push((t-1)/2);
      }
      int t = q.top();
      printf("Case #%d: %d %d \n",_i, t/2, (t-1)/2);
   }
   return 0;
}
