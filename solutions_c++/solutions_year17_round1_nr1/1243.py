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
const LL inf=1e18;
const LL maxN = 1e9;
const LL MOD = LL(1000000007);

#define prt_case(idx) cout << "Case #" << idx << ":\n";

void solve(int t)
{
  prt_case(t);
  string s[30];
  int x,y;
  cin >> x >> y;
  REP(i,x)
    {
      cin >> s[i];
    }
  REP(i,x)
    {
      char c = '?';
      REP(j,y)
	{
	  
	  if(s[i][j] == '?') s[i][j] = c;
	  else c = s[i][j];
	}
    }
  for(int i = 0; i < x; i++)
    {
      char c = '?';
      for(int j = y - 1; j >= 0; j--)
	{
	  if(s[i][j] == '?') s[i][j] = c;
	  else c = s[i][j];
      }
    }
  
  for(int j = 0; j < y; j++)
    {
      char c = '?';
      for(int i = 0; i < x; i++)
      {
	if(s[i][j] == '?') s[i][j] = c;
	else c = s[i][j];
      }
  }

    for(int j = 0; j < y; j++)
    {
      char c = '?';
      for(int i = x - 1; i >= 0; i--)
      {
	if(s[i][j] == '?') s[i][j] = c;
	else c = s[i][j];
      }
  }
  
  REP(i,x)
    {
      REP(j,y) cout << s[i][j];
      cout << endl;
    }
}


int t = 0;

int main()
{
  IOS();
  cin >> t;
  REP(i,t)
    solve(i + 1);
  return 0;
}
