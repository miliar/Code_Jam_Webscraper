#include  <bits/stdc++.h>
#define FOR(i,n) for(int i=0;i<(int)n;i++)
#define ALL(v) v.begin(),v.end()
#define UNIQUE(c) (c).resize(distance((c).begin(), unique(ALL(c))))
using namespace std;

typedef long long int LL;
typedef long long unsigned int LLU;

typedef vector<int>   VI;       typedef vector<bool> VB;
typedef vector<VI>   VVI;       typedef vector<double> VD;
typedef vector<VVI> VVVI;       typedef vector<VD> VDD;

typedef pair<int,int> PI;       typedef pair<double,double> PD;
typedef pair<PI,int> PII;

void main2()
{
  int R, C; cin >> R >> C;
  string t[R];
  for(int i=0;i<R; i++)
    cin >> t[i];
  
  for (int i=0; i<R; i++)
  {
    char first = '?';
    for (int j=0; j<C; j++)
    {
      if (t[i][j] != '?')
      {
        first = t[i][j];
        break;
      }
    }
    
    if (first != '?')
    {
      t[i][0] = first;
      for (int j=1; j<C; j++)
        if (t[i][j] == '?')
          t[i][j] = t[i][j-1];
    }
  }
  
  string first = "";
  for (int i=0; i<R; i++)
  {
    if (t[i][0] != '?')
    {
      first = t[i];
      break;
    }
  }
  
  t[0] = first;
  for (int i=1; i<R; i++)
    if (t[i][0] == '?')
      t[i] = t[i-1];
    
  for (int i=0; i<R; i++)
    cout << t[i] << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ":" << endl;
    main2();
  }
}
