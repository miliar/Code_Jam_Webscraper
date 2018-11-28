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
typedef vector<vector<char> > VVC;

VVC yoko(VVC cake, int i, int j, int R, int C)
{
  char c = cake[i][j];
  if (c == '?')
    return cake;
  int jj = j - 1;
  while (jj >= 0 && cake[i][jj] == '?')
    {
      cake[i][jj] = c;
      jj--;
    }
  jj = j + 1;
  while (jj < C && cake[i][jj] == '?')
    {
    cake[i][jj] = c;
    jj++;
    }
  return cake;
}

VVC tate(VVC cake, int i, int j, int R, int C)
{
  char c = cake[i][j];
  if (c == '?')
    return cake;
  int ii = i - 1;
  while (ii >= 0 && cake[ii][j] == '?')
    {
      cake[ii][j] = c;
      ii--;
    }
  ii = i + 1;
  while (ii < R && cake[ii][j] == '?')
    {
      cake[ii][j] = c;
      ii++;
    }
  return cake;
}

bool check_naname(VVC cake, int i_start, int i_target, int j_start, int j_target, int R, int C)
{
  //yoko
  REP(i, i_start, i_target+1)
    if (cake[i][j_target] != '?' && cake[i][j_target] != cake[i_start][j_start])
      return false;
  //tate
  REP(j, j_start, j_target+1)
    if (cake[i_target][j] != '?' && cake[i_target][j] != cake[i_start][j_start])
      return false;
  //yoko
  REP(i, i_target, i_start+1)
    if (cake[i][j_target] != '?' && cake[i][j_target] != cake[i_start][j_start])
      return false;
  //tate
  REP(j, j_target, j_start+1)
    if (cake[i_target][j] != '?' && cake[i_target][j] != cake[i_start][j_start])
      return false;
  return true;
}

VVC naname(VVC cake, int i, int j, int R, int C)
{
  char c = cake[i][j];
  if (c == '?')
    return cake;
  int ii = i - 1;
  int jj = j - 1;
  while (ii >= 0 && jj >= 0 && check_naname(cake, i, ii, j, jj, R, C))
    {
      REP(iii, ii, i+1)
	cake[iii][jj] = c;
      REP(jjj, jj, j+1)
	cake[ii][jjj] = c;
      if (ii == 0 &&  jj == 0)
	break;
      if (ii > 0)
	ii--;
      if (jj > 0)
	jj--;
    }
  ii = i - 1;
  jj = j + 1;
  while (ii >= 0 && jj < C && check_naname(cake, i, ii, j, jj, R, C))
    {
      REP(iii, ii, i+1)
	cake[iii][jj] = c;
      REP(jjj, j, jj+1)
	cake[ii][jjj] = c;
      if (ii == 0 &&  jj == C-1)
	break;
      if (ii > 0)
	ii--;
      if (jj < C-1)
	jj++;
    }
  ii = i + 1;
  jj = j - 1;
  while (ii < R && jj >= 0 && check_naname(cake, i, ii, j, jj, R, C))
    {
      REP(iii, i, ii+1)
	cake[iii][jj] = c;
      REP(jjj, jj, j+1)
	cake[ii][jjj] = c;
      if (ii == R-1 &&  jj == 0)
	break;
      if (ii < R-1)
	ii++;
      if (jj > 0)
	jj--;
    }
  ii = i + 1;
  jj = j + 1;
  while (ii < R && jj < C && check_naname(cake, i, ii, j, jj, R, C))
    {
      REP(iii, i, ii+1)
	cake[iii][jj] = c;
      REP(jjj, j, jj+1)
	cake[ii][jjj] = c;
      if (ii == R-1 &&  jj == C-1)
	break;
      if (ii < R-1)
	ii++;
      if (jj < C-1)
	jj++;
    }

  ii = i + 1;
  jj = j + 1;
  while (ii < R && jj < C && check_naname(cake, i, ii, j, jj, R, C))
    {
      REP(iii, i, ii+1)
	cake[iii][jj] = c;
      REP(jjj, j, jj+1)
	cake[ii][jjj] = c;
      if (ii == R-1 &&  jj == C-1)
	break;
      if (ii < R-1)
	ii++;
      if (jj < C-1)
	jj++;
    }
  return cake;
}

bool check_cake(VVC cake, int R, int C)
{
  REP(i,0,R)
    {
    REP(j,0,C)
      if (cake[i][j] == '?')
	return false;
    }
  return true;
}


vector<vector<char> > solve(vector<vector<char> > cake, set<char> used, int i, int j, int R, int C)
{
  if (check_cake(cake, R, C))
    return cake;
  VVC new_cake = cake;
  if (used.find(cake[i][j])!= used.end())
    {
    if (j < C-1)
      {
	return solve(cake, used, i, j+1, R, C);
      }
    else if (i < R-1)
      {
	return solve(cake, used, i+1, 0, R, C);
      }
    return cake;
    }
  used.insert(cake[i][j]);
  new_cake = tate(cake, i, j, R, C);
  if (j < C-1)
      {
	new_cake = solve(new_cake, used, i, j+1, R, C);
      }
  else if (i < R-1)
      {
	new_cake = solve(new_cake, used, i+1, 0, R, C);
      }
  if (check_cake(new_cake, R, C))
    return new_cake;
  new_cake = yoko(cake, i, j, R, C);
  if (j < C-1)
    {
      new_cake = solve(new_cake, used, i, j+1, R, C);
    }
  else if (i < R-1)
    {
      new_cake = solve(new_cake, used, i+1, 0, R, C);
    }
  if (check_cake(new_cake, R, C))
    return new_cake;
  new_cake = naname(cake, i, j, R, C);
  
  if (j < C-1)
      {
	new_cake = solve(new_cake, used, i, j+1, R, C);
      }
    else if (i < R-1)
      {
	new_cake = solve(new_cake, used, i+1, 0, R, C);
      }
  if (check_cake(new_cake, R, C))
    return new_cake;
  return cake;
}


int main(void){
  int T;
  cin >> T;
  REP(t, 1, T+1)
    {
      int R, C;
      cin >> R >> C;
      vector<vector<char> > cake(R, vector<char>(C));
      set<char> used;
      REP(r, 0, R)
	REP(c, 0, C)
	  cin >> cake[r][c];
      vector<vector<char> > result = solve(cake, used, 0, 0, R, C);
      cout << "Case #" << t << ":" << endl;
      REP(r, 0, R)
	{
	  REP(c, 0, C)
	    {
	      cout << result[r][c];
	    }
	  cout << endl;
	}
      
      
      
    }
}
