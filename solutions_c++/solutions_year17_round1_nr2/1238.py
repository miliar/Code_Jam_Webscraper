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
const LL roof = 2e6 + 1;
#define prt(idx) cout << "Case #" << idx << ": "
#define quit(idx) prt(-1, idx); return

LD a[100][100];
int in[100];
LD ind[100];
void solve(int idx)
{
  prt(idx);
  int n,p;
  cin >> n >> p;
  REP(i,n) cin >> in[i];
  REP(i,n)
    REP(j,p) cin >> a[i][j];

  REP(i,n) sort(a[i], a[i]+p);
  REP(i,n) ind[i] = 0;
  int ans = 0;
  REP(i,p)
    {
      int mx = -1, mi = roof * 100;
      REP(rep,roof) {
	if(in[0] * ((LD)rep * 0.9) <= (LD)a[0][i] + eps and (LD)a[0][i] - eps <= in[0] * ((LD)rep * 1.1))
	  {
	    //	    cout << rep << endl;
	    mx = max(mx, rep), mi=min(mi, rep);
	  }
	if(in[0] * ((LD)rep * 0.9) > (LD)a[0][i] - eps)
	  break;
      }
      if(mx == -1) continue;
      for(int rep = mi; rep <= mx; rep++)
	{
	  bool b2 = true;
	  FOR(j,1,n)
	    {
	      bool b1 = false;
	      FOR(len, ind[j], p)
		{
		  if(in[j] * rep * 0.9 <= a[j][len] and a[j][len] <= in[j] * rep * 1.1)
		    {
		      
		      ind[j] = len + 1;
		      b1 = true;
		      break;
		    }
		}
	      if(b1 == false)
		{
		  b2 = false;
		  break;
		}
	    }
	  if(b2 == true)
	    {
	      ans++;
	      break;
	    }
	}
    }
  // cout << "YOLO" << endl;
  cout << ans << endl;
  
}

int main()
{
  int t;
  cin >> t;
  REP(i, t) solve(i + 1);
  return 0;
}
