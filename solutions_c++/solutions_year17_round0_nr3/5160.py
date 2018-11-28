#include<iostream>
#include<set>
#include<map>
using namespace std;
set<long long> S;
map<long long, long long> mp;
int main()
{
  int T;
  cin >> T;

  for(int t = 1;t <= T;t ++)
  {
    long long N , K;
    cin >> N >> K;

    S.clear();
    mp.clear();

    S.insert(N);
    mp[N] = 1;
    long long ans1 , ans2;

    while(K)
    {
      long long t = (*S.rbegin());
      if(mp[t] >= K)
      {
        ans1 = (t) / 2 , ans2 = (t - 1) / 2;
        break;
      }
      K -= mp[t];
      mp[(t - 1) / 2] += mp[t];
      mp[(t) / 2] += mp[t];
      mp[t] = 0;
      S.erase(t);
      S.insert((t - 1) / 2);
      S.insert(t / 2);
    }
    cout << "Case #" << t << ": " << ans1 << " " << ans2<< endl;
  }
}
