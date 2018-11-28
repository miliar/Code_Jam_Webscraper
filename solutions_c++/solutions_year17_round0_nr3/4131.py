#include<bits/stdc++.h>
using namespace std;
int main()
{
  ios_base::sync_with_stdio(false);
  int t , T , k , n , i ;
  int l , r , x;
  cin >> T;
  for(t=1;t<=T;t++)
  {
    cin >> n >> k;
    priority_queue < int > pq;
    pq.push(n);
    for(i=1;i<=k;i++)
    {
      x = pq.top();
      pq.pop();
      l = x/2 - 1;
      r = x/2;
      l = l + x%2;
      pq.push(l);
      pq.push(r);
    }
    cout << "Case #" << t << ": " << r << " " << l << "\n";
  }
  return 0;
}
