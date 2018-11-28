#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

i64 countDigits(i64 x)
{ 
  i64 count = (x == 0) ? 1 : (int)(std::log10(std::abs((ld)(x))));
  return count+1;
}

void getTidy(i64 x)
{
  int nDigits = countDigits(x);
  vector<int> digitVec;
  digitVec.resize(nDigits);
  ford(i,nDigits)
  {
    digitVec[i] = 0;
    i64 divisor = pow((ld)10, i);
    i64 digit = x / divisor;
    x -= digit * divisor;
    digitVec[i] = digit;
  }
  for (int i = nDigits-1; i > 0; i--)
  {
    if ((digitVec[i] > digitVec[i-1]) && (nDigits > 1))
    {
      digitVec[i] -= 1;
      for (int j = i-1; j >= 0; j--)
      {
	for (int k = j+1; k < nDigits; k++)
	{
          if ((digitVec[k] < digitVec[k+1]) && (k < nDigits-1))
	  {
            digitVec[k+1] -=1;
	    digitVec[k] = 9;
	  }
	}
        digitVec[j] = 9;
      }
      break;
    }
  }

  ford(i,nDigits)
  {
    bool print = false;
    if (!print && (digitVec[i] != 0)) print = true;
    if (print) cout << digitVec[i];
  }
  cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int T;
    cin >> T;
    for1(tc, T) {
        cout << "Case #" << tc << ": ";
	i64 N = 0;
        cin >> N;
        getTidy(N);
//	cout << nDigits << endl;
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
