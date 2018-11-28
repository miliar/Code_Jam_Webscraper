/**********************
 #  By lintao [Hudi]  #
 **********************/

#define _MULTI_TC_
// #define _DEBUG_

// =========================================== //
//    
// =========================================== //
#include <bits/stdc++.h>
using namespace std;

#define RESET(c,v) memset(c,v,sizeof(c))
#define REP(a,b,c) for (int a=b, _c=c; a<_c; ++a)
#define RED(a,b,c) for (int a=b, _c=c; a>=_c; --a)

#define PB push_back
#define MP make_pair
#define fi first
#define sc second
#define PI acos(-1.0) //alternative #define PI (2.0 * acos(0.0))

typedef long long ll;
typedef pair<ll,ll> puu;
typedef pair<int,int> pii;

const double INF = 1e9;
const double EPS = 1e-9;


// =========================================== //
//     DEBUG Template                          //
// =========================================== //
#ifdef _DEBUG_
	#define DEBUG(a) __Debug_Print__(#a, a)
	#define Dprintf printf
	#define Dcout cout
	#define DREP REP
	#define DRED RED
 #else
	#define DEBUG(a) if (0) __Debug_Print__(#a, a)
	#define Dprintf if (0) printf
	#define Dcout if (0) cout
	#define DREP if (0) REP
	#define DRED if (0) RED
#endif

// Debug Function //
  template<typename T>
  void __Debug_Print__(const string &varname, T &a) {
    Dcout << endl << "<== ### DEBUG (" << varname << ") ### ==> : " << a << endl;
  }
  template<typename T1, typename T2>
  void __Debug_Print__(const string &varname, pair<T1,T2> &a) {
    Dcout << endl << "<== ### DEBUG (" << varname << ") ### ==> : " << a.fi << "," << a.sc << endl;
  }

  template<typename T, size_t N>
  void __Debug_Print__(const string &varname, T (&a)[N]) {
    Dcout << endl << "<== ### DEBUG array (" << varname << ") ### ==>" << endl;
    DREP(x,0,N) cout << " " << a[x];
    Dcout << endl << "<== *** ==>" << endl;
  }
  template<typename T1, typename T2, size_t N>
  void __Debug_Print__(const string &varname, pair<T1,T2> (&a)[N]) {
    Dcout << endl << "<== ### DEBUG array (" << varname << ") ### ==>" << endl;
    DREP(x,0,N) cout << " " << a[x].fi << "," << a[x].sc;
    Dcout << endl << "<== *** ==>" << endl;
  }
  template<typename T1, typename T2>
  void __Debug_Print__(const string &varname, vector<T1,T2> &a) {
    Dcout << endl << "<== ### DEBUG array (" << varname << ") ### ==>" << endl;
    DREP(x,0,a.size()) cout << " " << a[x];
    Dcout << endl << "<== *** ==>" << endl;
  }

  template<typename T, size_t M, size_t N>
  void __Debug_Print__(const string &varname, T (&a)[M][N]) {
    Dcout << endl << "<== ### DEBUG array 2D (" << varname << ") ### ==>" << endl;
    DREP(y,0,M) {
      REP(x,0,N) cout << "  " << a[y][x];
      cout << endl;
    }
    Dcout << "<== *** ==>" << endl;
  }
  template<typename T1, typename T2, size_t M, size_t N>
  void __Debug_Print__(const string &varname, pair<T1,T2> (&a)[M][N]) {
    Dcout << endl << "<== ### DEBUG array 2D (" << varname << ") ### ==>" << endl;
    DREP(y,0,M) {
      REP(x,0,N) cout << "  " << a[y][x].fi << "," << a[y][x].sc;
      cout << endl;
    }
    Dcout << "<== *** ==>" << endl;
  }
// *** //

// =========================================== //
void solve(int);
int main()
{
	#ifdef _MULTI_TC_
		int TC;
		scanf("%d", &TC);
		REP(tc,1,TC+1) solve(tc);
	#else
		solve(-1);
	#endif
	return 0;
}
// =========================================== //

int N, P;
int G[102];

void solve(int tc)
{
  cin >> N >> P;
  REP(x,0,N) cin >> G[x];

  int ans = 0;
  if (P==2) {
    bool tmp = true;
    REP(x,0,N) if (G[x]%2) {
      if (tmp) ++ans;
      tmp = !tmp;
    } else {
      ++ans;
    }
  } else if (P==3) {
    int sisa[3];
    RESET(sisa,0);
    int lft=0;
    REP(x,0,N) ++sisa[G[x]%3];
    ans = sisa[0];
    if (sisa[1] < sisa[2]) {
      ans += sisa[1];
      lft = sisa[2]-sisa[1];
    } else {
      ans += sisa[2];
      lft = sisa[1]-sisa[2];
    }
    ans += ((lft+2)/3);
  } else if (P==4) {
    int sisa[4];
    RESET(sisa,0);

    REP(x,0,N) ++sisa[G[x]%4];
    ans = sisa[0];
    DEBUG(ans);

    int wow = min(sisa[1], sisa[3]);
    ans += wow;
    sisa[1] -= wow;
    sisa[3] -= wow;
    DEBUG(ans);
    DEBUG(wow);

    wow = sisa[1]/2 + sisa[3]/2; // one of these should be zero
    sisa[2] += wow;
    ans += sisa[2]/2;
    DEBUG(ans);
    DEBUG(wow);

    if ((sisa[1]&1) || (sisa[2]&1) || (sisa[3]&1)) ++ans;
    DEBUG(ans);
  }

  printf("Case #%d: %d\n", tc, ans);
}