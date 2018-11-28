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
  string N; cin >> N;
  
  int dec = N.size();
  for (int i=N.size()-1; i>0; i--)
    if (N[i-1] > N[i])
      dec = i;
      
  if (dec != (int)N.size())
  {
    while (dec > 1 && N[dec-1] == N[dec-2])
      dec--;
    N[dec-1]--;
  }
  
  for (int i=dec; i<(int)N.size(); i++)
    N[i] = '9';
  
  int start = 0;
  while (N[start] == '0')
    start++;
  
  for (int i=start; i<(int)N.size(); i++)
    cout << N[i];
  cout << endl;
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
