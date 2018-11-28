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
typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int, int> PI;
const ll mod = 1e9 + 7;

int main(void){
  ll T;
  cin >> T;
  REP(t, 1, T+1)
    {
      ll D, N;
      cin >> D >> N;
      double max_reach = 0;
      REP(n, 0, N)
	{
	  ll K, S;
	  cin >> K >> S;
	  double time_to_reach = 1.0 * (D - K) / S;
	  if (max_reach < time_to_reach)
	    max_reach = time_to_reach;
	}
      double speed = 1.0 * D / max_reach;
      cout << "Case #"<<t<<": "
	   << fixed
	   << setprecision(6)<<speed<<endl;
    }
}
