#include <iostream>
#include <string>
#include <cstdio>
#include <map>
using namespace std;

int main()
{
  int tc;
  cin >> tc;
  for (int tt=1; tt<=tc; tt++)
  {
    long long n, k;
    cin >> n >> k;
    map<long long,long long> mp;
    mp[n] = 1;
    while (1)
    {
      map<long long,long long> :: iterator j = mp.end();
      j--;
      long long f=j->first, s=j->second;
      if (k>s)
      {
        k -= s;
        mp[(f-1)/2] += s;
        mp[f-1-(f-1)/2] += s;
        mp.erase(j);
      }
      else
      {
        cout << "Case #" << tt << ": " << f-1-(f-1)/2 << " " << (f-1)/2 << endl;
        break;
      }
    }
  }
}
