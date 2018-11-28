#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)

using namespace std;
typedef long long int ll;
typedef long long unsigned llu;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int, int> PI;
const ll mod = 1e9 + 7;

int main(void){
  unsigned T;
  cin >> T;
  REP(t, 1, T+1)
    {
      ll K, N;
      cin >> N >> K;
      vector<ll> n(N+1, 0);
      n[N] = 1;
      ll LS = -1, RS = -1;
      ll max_n = N;
      while (K > 0) 
	{
	  K -= n[max_n];
	  if (max_n % 2 == 1)
	    {
	      LS = max_n / 2;
	      RS = max_n / 2;
	      n[LS] += 2 * n[max_n];
	    }
	  else
	    {
	      LS = max_n / 2 - 1;
	      RS = max_n / 2;
	      n[LS] += n[max_n];
	      n[RS] += n[max_n];
	    }
	  n[max_n] = 0;
	  while (n[max_n] == 0 and max_n > 1)
	    max_n--;
	}
      cout << "Case #" << t << ": " << max(LS,RS) << " " << min(LS, RS) << endl;
    }
}
