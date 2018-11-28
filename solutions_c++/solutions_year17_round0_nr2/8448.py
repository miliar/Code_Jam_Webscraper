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

llu RegExp(string& N, char s, llu start) 
{
  llu index = start;
  while (N[index] == s and index < N.size())
    index++;
  return index;
}

llu RegExpFromStart(string& N, llu start)
{
  llu index = start;
  vector<char> ss = {'1','2','3','4','5','6','7','8','9'};
  REP(i,0,9)
    index = RegExp(N, ss[i], index);
  return index;
}

bool ShouldBeFromNine(string& N)
{
  llu index = 0;
  REP(i, 0, N.size())
    index = RegExp(N, '1', index);
  if (N[index] == '0')
    return true;
  else
    return false;
}

int main(void){
  ll T;
  cin >> T;
  REP(i, 1, T+1) 
    {
      string N;
      cin >> N;
      llu index = 0;
      if (ShouldBeFromNine(N)) 
	{
	  N = string(N.size() - 1, '9');
	}
      else
	{
	  llu i_end = RegExpFromStart(N, index);
	  if (i_end < N.size())
	    N[i_end - 1]--;
	  REP(j, i_end, N.size())
	    N[j] = '9';
	}
      cout << "Case #" << i << ": " << N << endl;
    }
}
