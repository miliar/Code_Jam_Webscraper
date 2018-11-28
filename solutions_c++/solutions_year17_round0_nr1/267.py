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
  string s; cin >> s;
  int K; cin >> K;
  
  int result = 0;
  for (int i=0; i+K-1<(int)s.size(); i++)
  if (s[i] == '-')
  {
    result++;
    for (int j=0; j<K; j++)
      s[i+j] = '-' + '+' - s[i+j];
  }
  
  for (int i=0; i<(int)s.size(); i++)
  if (s[i] == '-')
  {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  
  cout << result << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
