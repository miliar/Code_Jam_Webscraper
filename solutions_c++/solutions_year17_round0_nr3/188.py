#include <map>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x) cerr << #x << " = " << x << endl
#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=(a); i<(b); i++)
#define _ << " " <<

typedef long long ll;
typedef pair<ll, ll> P;
#define X first
#define Y second

map <ll, vector<P> > M;

vector <P> gen(ll n)
{
  if (!n) return vector<P>();
  if (M.find(n) != M.end()) return M[n];
  
  map <ll, ll> Cnt;
  Cnt[n]++;
  auto L = gen(n/2);
  for (auto it : L) Cnt[it.X] += it.Y;
  
  auto R = gen((n-1)/2);
  for (auto it : R) Cnt[it.X] += it.Y;

  vector <P> Ret;
  for (auto it = Cnt.begin(); it != Cnt.end(); it++)
    Ret.push_back(*it);

  return M[n] = Ret;
}

int main()
{
  int brt;
  scanf("%d", &brt);

  FOR(br, 1, brt+1) {
    M.clear();

    ll n, k;
    scanf("%lld%lld", &n, &k);
    
    vector <P> V = gen(n);
    ll sum = 0;
    for (auto it : V) sum += it.Y;
    assert(sum == n);

    for (int i=(int)V.size()-1; i>=0; i--) {
      auto it = V[i];
      if (it.Y >= k) {
	printf("Case #%d: %lld %lld\n", br, it.X/2, (it.X-1)/2);
	break;
      }
      k -= it.Y;
    }
  }

  return 0;
}
