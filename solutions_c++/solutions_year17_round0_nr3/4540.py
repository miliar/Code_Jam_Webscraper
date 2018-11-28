#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t; scanf("%d", &t);
  for(int i = 1; i <= t; i++)
  {
        priority_queue <pair <int, int> > Q; 
        long long n,k;
        scanf("%lld %lld", &n,&k);
        
        Q.push( make_pair(n,0));
        int mini, maxi;
        for(int j = 0; j < k; j++)
        {
                pair <int, int> top = Q.top();
                Q.pop();
                
                int pos = -top.second;
                int len = top.first;
  
                
                int off = (len-1)/2;
                
                Q.push(make_pair(off, -pos));
                Q.push(make_pair((len-off-1), -(pos+off+1)));
                
                mini = min(off, len-off-1);
                maxi = max(off, len-off-1);
                
             
        }
           printf("Case #%d: %d %d\n", i, maxi, mini);
  }

return 0;
}