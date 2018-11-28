
#include <iostream>
#include <map>

#define INF ((long long)(2e18))
#define N 1000
#define K 1000

using namespace std;

pair<long long, long long> compute(long long n, long long k, map<pair<long long, long long>, pair<long long, long long> > &m){
  if(k > n)
    return make_pair(INF, INF);
  if(k == 0)
    return make_pair(INF, INF);

  map<pair<long long, long long>, pair<long long, long long> >::const_iterator it = m.find(make_pair(n, k));
  if(it != m.end()){
    return it->second;
  }

  pair<long long, long long> p = make_pair((n - 1)/ 2, n / 2);

  if(k == 1){
    m[make_pair(n, k)] = p;
    return p;
  }

  p = min(p, compute((n - 1) / 2, (k - 1) / 2, m));
  p = min(p, compute(n / 2, (k - 1) / 2 + (k - 1) % 2, m));

  m[make_pair(n, k)] = p;

  return p;
}

int main(){
  ios::sync_with_stdio(false);

  map<pair<long long, long long>, pair<long long, long long> > m;

  int t;
  cin >> t;

  for(int x = 1; x <= t; x++){
    long long n, k;
    cin >> n >> k;

    pair<long long, long long> p;
    p = compute(n, k, m);

    cout << "Case #" << x << ": " << p.second << " " << p.first << endl;
  }

  return 0;
}
