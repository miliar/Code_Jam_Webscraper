#include "bits/stdc++.h"

using namespace std;

map <long long, map <long long, long long> > dp;

void go(long long x)
{
  if(x < 1)
    return;
  if(dp.find(x) != dp.end())
    return;
  map <long long, long long> y;
  dp[x][x] += 1;
  go((x-1)/2);
  for(auto it = dp[(x-1)/2].begin(); it != dp[(x-1)/2].end(); it++)
    dp[x][(*it).first] += (*it).second;
  go(x/2);
  for(auto it = dp[x/2].begin(); it != dp[x/2].end(); it++)
    dp[x][(*it).first] += (*it).second;
}

long long findHelper(long long x, long long v, long long k)
{
  if(x == v)
    return v;
  if(dp[(x-1)/2][v] >= k)
    return findHelper((x-1)/2, v, k);
  else
    return (x+1)/2 + findHelper(x/2, v, k - dp[(x-1)/2][v]);
}

long long find(long long x, long long k)
{
  for(auto it = dp[x].rbegin(); it != dp[x].rend(); it++)
  {
    if((*it).second >= k)
    {
      //cerr << "Y" << x << " " << (*it).first << " " << k << "\n";
      //return findHelper(x, (*it).first, k);
      return (*it).first;
    }
    k -= (*it).second;
  }
  return -1;
}

void test()
{
  long long n, k;
  cin >> n >> k;
  go(n);
  long long f = find(n,k);
  cout << f/2 << " " << (f-1)/2;
}

int main()
{
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  for(int i=1; i<=t; i++)
  {
    cout << "Case #" << i << ": ";
    test();
    cout << "\n";
  }
  return 0;
}
