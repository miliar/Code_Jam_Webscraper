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

#define prt_case(idx) cout << "Case #" << idx << ": ";

int t = 0;
int main()
{
  IOS();
  cin >> t;
  REP(i,t)
    {
      prt_case(i + 1);
      int x;
      cin >> x;
      int ans = 1;
      FOR(j, 1, x + 1)
	{
	  bool b = false;
	  string s = to_string(j);
	  REP(rep,s.size() - 1)
	    if(s[rep] > s[rep + 1])
	      {
		b = true;
		break;
	      }
	  if(b == false)
	    ans = j;
	}
      cout << ans << endl;
    }
  return 0;
}
