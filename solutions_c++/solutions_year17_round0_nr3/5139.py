//RamiZ
#pragma comment(linker,"/STACK:10000000000")
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <deque>
#include <map>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <bitset>
#include <queue>

using namespace std;

#define FOREACH(i, c) for(__typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for(int (i) = (a); i<(int)(n); ++(i))
#define REP(i, n) for(int (i)=0;i<(n);++i)
#define error(n) cerr << #n << " = " << n << endl
#define all(c) c.begin(), c.end()
#define pb push_back
#define mp make_pair
#define Size(n) ((int)(n).size())
#define X first
#define Y second
#define OUT( n ) cout<<fixed<<setprecision(18)<<(n)
#define endl '\n'
#define sqr( x ) ((((x))*((x))))
#define IOS() ios_base::sync_with_stdio(false)
#define Time()   cerr << "Time =  " << clock() <<"ms" << endl
#define gcd __gcd

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;
typedef pair<LL,LL>  pLL;
typedef string str;
typedef vector<int> VI;
typedef vector< pair < int , int > > Vpii;
typedef vector< long long > VLL;

const LD PI=LD(3.14159265358979);
const LD eps=1e-7;
const LL inf=1e16;
const LL maxN = 1e9;
const LL MOD = LL(1000000007);

#define prt(idx) cout << "Case #" << idx << ": "
#define quit(idx) prt(-1, idx); return

void solve(int idx)
{
  prt(idx);
  LL x, k;
  cin >> x >> k;
  set<LL> s;
  vector<LL> v;
  map<LL,LL> m;
  s.insert(x);
  while(s.size())
    {
      //FOREACH(I,s)
      //cout << *I << ' ';
      //cout << endl;
      LL y = *s.crbegin();
      v.push_back(y);
      s.erase(s.find(y));
      if(y == 1) continue;
      if(y == 2)
	{
	  s.insert(1);
	  continue;
	}
      if(y % 2 == 1)
	{
	  s.insert(y / 2);
	}
      else
	{
	  s.insert(y / 2);
	  s.insert((y / 2) - 1);
	}
    }
  //cout << 'j' << endl;
  sort(v.begin(),v.end());
  m[v[v.size() - 1]] = 1;
  for(int i = v.size() - 1; i >=0 ; i--)
    {
      if(v[i] % 2 == 1)
	{
	  m[v[i] / 2] += m[v[i]] * 2;
	}
      else
	{
	  m[v[i] / 2] += m[v[i]];
	  m[(v[i] / 2) - 1] += m[v[i]];
	}
    }
  vector<pLL> g;
  FOREACH(i, m)
    {
      g.push_back(*i); 
    }
  sort(g.begin(), g.end());
  LL cnt = 0;
  for(int i = g.size() - 1; i >= 0; i--)
    {
      cnt += g[i].second;
      if(k <= cnt)
	{
	  if(g[i].first % 2 == 1)
	    {
	      cout << g[i].first / 2 << ' ' << g[i].first / 2 << endl;
	    }
	  else
	    {
	      cout << g[i].first / 2 << ' ' << (g[i].first / 2) - 1 << endl;
	    }
	  return;
	}
    }
}

int main()
{
  int t;
  cin >> t;
  REP(i, t) solve(i + 1);
  return 0;
}
