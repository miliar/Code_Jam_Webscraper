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
  LL N, K; cin >> N >> K;
  
  map<LL, LL> tab;
  tab[N] = 1;
  
  while (true)
  {
    auto x = tab.rbegin();
    LL a = x->first / 2;
    LL b = (x->first - 1) / 2;
    
    if (K <= x->second)
    {
      cout << a << " " << b << endl;
      return;
    }
    
    K -= x->second;
    tab[a] += x->second;
    tab[b] += x->second;
    tab.erase(x->first);
  }
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
