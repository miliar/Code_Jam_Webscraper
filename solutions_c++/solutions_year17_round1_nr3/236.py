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
  int Hd, Ad, Hk, Ak, B, D;
  cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
  
  double nb_buff = B == 0 ? 0 : sqrt(Hk / (double) B) - Ad / (double) B;
  int attack1 = ceil(Hk / (double)(Ad + B * ceil(nb_buff)) + ceil(nb_buff));
  int attack2 = ceil(Hk / (double)(Ad + B * floor(nb_buff)) + floor(nb_buff));
  int attack = min(attack1, attack2);
  
  attack = 1000000000;
  for (int i=0; i<100; i++)
    attack = min(attack, (int)ceil(Hk / (double)(Ad + B * i)) + i);
  
  //cerr << attack << endl;
  
  int result = 1000000000;
  int max_debuff = D == 0 ? 0 : ceil(Ak / (double) D);
  for (int nb=0; nb<=max_debuff; nb++)
  {
    int turn = 0;
    int H = Hd;
    int A = Ak;
    
    for (int i=0; i<nb; i++)
    {
      if (H <= A - D)
      {
        turn++;
        H = max(0, Hd - A);
      }
      
      turn++;
      A = max(0, A-D);
      H = max(0, H-A);
      
      if (H == 0) turn = 1000000000;
    }
    
    for (int i=1; i<attack; i++)
    {
      if (H <= A)
      {
        turn++;
        H = max(0, Hd - A);
      }
      
      turn++;
      H = max(0, H-A);
      
      if (H == 0) turn = 1000000000;
    }
    
    turn++;
    
    result = min(result, turn);
  }
  
  if (result >= 1000000000)
    cout << "IMPOSSIBLE" << endl;
  else
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
