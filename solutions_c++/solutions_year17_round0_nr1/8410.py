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
typedef vector<bool> VB;
typedef vector<vector<bool> > VVB;
const ll mod = 1e9 + 7;


bool is_in_range(VB& S, int start, int K)
{
  return (int)S.size() - (start + K - 1) > 0;
}

bool is_happy(VB& S, int start, int K)
{
  REP(i, start, start + K)
    if (!S[i])
      return false;
  return true;
}

void flip(VB& S, int start, int K)
{
  REP(i, start, start + K)
    S[i] = !S[i];
}

void dprint(VB& S) 
{
  REP(i, 0, S.size())
    if (S[i])
      cout << "+";
    else
      cout << "-";
  cout << endl;
}


int main(void){
  ll T;
  cin >> T;
  VVB S(T+1);
  vector<int> K(T+1, -1);
  REP(t, 1, T+1) 
    {
      string _S;
      cin >> _S >> K[t];
      //cout << K[t] << endl;
      S[t] = vector<bool>(_S.size(), true);
      REP(i, 0, _S.size())
	{
	  if (_S[i] == '+')
	    S[t][i] = true;
	  else if (_S[i] == '-')
	    S[t][i] = false;
	}
    }
  REP(t, 1, T+1)
    {
      int step = 0;
      REP(i, 0, S[t].size())
	if (!S[t][i] && is_in_range(S[t], i, K[t]))
	  {
	    //cout << i << t << ":"<< S[t].size() << ":" << i << ":" << K[t] << endl;
	    flip(S[t], i, K[t]);
	    //dprint(S[t]);
	    step++;
	  }
      cout << "Case #" << t << ": ";
      if (is_happy(S[t], 0, S[t].size()))
	cout << step << endl;
      else
	cout << "IMPOSSIBLE" << endl;
    }
}
