#include<bits/stdc++.h>
using namespace std;
# ifdef DEB
# define debug(...) fprintf(stderr, __VA_ARGS__)
# else
# define debug(...)
#endif
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PLL pair<LL, LL>
#define pb pop_back
#define VI vector<int> 
#define VPI vector<PII> 
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define RE(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(int)(n)-1)
#define ALL(x) (x).begin(), (x).end()
#define siz(V) ((int)V.size())

string s;

bool good()
{
  REP(i, siz(s) - 1)
  {
    if(s[i] > s[i + 1])
    {
      return false;
    }
  }
  return true;
}

void solve(int ind)
{
  cin>> s;
  while(!good())
  {
    REP(i, siz(s) - 1)
    {
      if (s[i] > s[i + 1])
      {
        s[i] = (char)((int)s[i] - 1);
        FOR(j, i + 1, siz(s) - 1)
        {
          s[j] = '9';
        }
        break;
      }
    }
  }
  int i = 0;
  while(s[i] == '0')
  {
    i++;
  }
  cout<< "Case #" << ind << ": ";
  for (; i < siz(s); i++)
  {
    cout<< s[i];
  }
  cout<< "\n";
}

int main()
{
  ios_base::sync_with_stdio(0);
  int t;
  cin>> t;
  RE(i, t)
  {
    solve(i);
  }
  return 0;
}
