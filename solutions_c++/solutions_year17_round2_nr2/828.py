#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const double eps = 1e-6;

int N, R, O, Y, G, B, V;
int *c = &R;

void init()
{
  cin >> N >> R >> O >> Y >> G >> B >> V;
}

bool ok()
{
  int pair = 0;
  if (B > 0 || O > 0) ++pair;
  if (R > 0 || G > 0) ++pair;
  if (Y > 0 || V > 0) ++pair;
  if (pair == 1)
    return true;
  if (B <= O && O > 0)
    return false;
  if (R <= G && G > 0)
    return false;
  if (Y <= V && V > 0)
    return false;
  return true;
}

const char *CH = "ROYGBV";

bool compa(char a, char b)
{
  if (a == 'R')
    return b == 'G' || b == 'Y' || b == 'B';
  if (a == 'Y')
    return b == 'V' || b == 'R' || b == 'B';
  if (a == 'B')
    return b == 'O' || b == 'R' || b == 'Y';
  if (a == 'O')
    return b == 'B';
  if (a == 'V')
    return b == 'Y';
  if (a == 'G')
    return b == 'R';
}

bool ok(string s)
{
  for (int i=1; i<s.length(); ++i)
    if (!compa(s[i], s[i-1]))
      return false;
  return compa(s.front(), s.back());
}

void sub(string &result)
{
  for (int k = 0; k < 5; k+=2)
  {
    int j = -1;
    for (int i=0; i<result.length(); ++i)
      if (result[i] == CH[k])
      {
        j = i;
        break;
      }
    if (j == -1)
      continue;
    string add = "";
    int p = (k+3)%6;
    for (int i=0; i<c[p]; ++i)
    {
      add += CH[p];
      add += CH[k];
    }
    result.insert(j+1, add);
    c[p] = 0;
  }
}

void single()
{
  string result;
  for (int k = 1; k < 6; k+=2)
  {
    int p = (k+3)%6;
    for (int i=0; i<c[k]; ++i)
    {
      result += CH[p];
      result += CH[k];
    }
  }
  if (ok(result))
    cout << result << endl;
  else
    cout << "IMPOSSIBLE" << endl;
}

void work()
{
  /*
  int total = 0;
  for (int i=0; i<6; ++i)
    if (c[i] > 0)
      ++total;
  if (!ok())
  {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  */
  B -= O;
  Y -= V;
  R -= G;
  int sum = R + Y + B;
  if (sum == 0)
  {
    single();
    return;
  }
  int last = -1;
  string result;
  bool pos = true;
  while (sum > 0)
  {
    int mc = 0, mi = -1;
    for (int i=0; i<5; i+=2)
      if (i != last && c[i]>mc)
      {
        mc = c[i];
        mi = i;
      }
    if (mi == -1)
    {
      mi = last;
    }
    last = mi;
    --c[mi];
    --sum;
    result += CH[mi];
  }
  if (!pos)
  {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  if (result.length() >= 3)
  {
    int n = result.length();
    vector<int> perm{0,1,2};
    for (int i=0; i<6; ++i)
    {
      string tmp = result;
      for (int j=0; j<3; ++j)
        tmp[n-3+j] = result[n-3+perm[j]];
      if (ok(tmp))
      {
        result = tmp;
        break;
      }
      next_permutation(perm.begin(), perm.end());
    }
  }
  sub(result);
  sum = 0;
  for (int i=0; i<6; ++i)
    sum += c[i];
  if (sum == 0 && ok(result))
    cout << result << endl;
  else
    cout << "IMPOSSIBLE" << endl;
}

int main()
{
  //freopen("B-small-attempt1.in", "r", stdin);
  freopen("B-large.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": ";
    init();
    work();
  }
}
