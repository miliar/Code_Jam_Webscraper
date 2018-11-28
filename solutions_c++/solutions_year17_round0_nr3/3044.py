#include <fstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>
#include <string>
#include <map>

using namespace std;

map<pair<long long, long long>, pair<long long, long long>> mp;

pair<long long, long long> solve2( long long N, long long K )
{
  if (mp.find(make_pair(N, K)) != mp.end())
    return mp[make_pair(N, K)];
  if (K == 0)
    return make_pair(N, N);
  if (N == 1 || N == 0)
    return make_pair(0, 0);
  if (K == 1)
    return make_pair((N - 1) / 2, N / 2);
  if (N % 2 == 1)
    return (mp[make_pair(N, K)] = solve2((N - 1) / 2, K / 2));
  else
  {
    pair<long long, long long> r1, r2;
    r1 = solve2(N / 2, K / 2);
    r2 = solve2(N - 1 - N / 2, K - 1 - K / 2);
    if (r1.first > r2.first)
      return (mp[make_pair(N, K)] = r2);
    else if (r1.first == r2.first)
      if (r2.second > r1.second)
        return (mp[make_pair(N, K)] = r1);
      else
        return (mp[make_pair(N, K)] = r2);
    else
      return (mp[make_pair(N, K)] = r1);
  }
}

int main( void )
{
  ifstream fin("C-large.in");
  ofstream fout("output.txt");

  int T;
  fin >> T;
  
  for (int i = 0; i < T; i++)
  {
    long long N, K;
    fin >> N >> K;
    mp.clear();
    auto pr = solve2(N, K);
    fout << "Case #" << i + 1 << ": " << pr.second << " " << pr.first << endl;
  }

  return 0;
}