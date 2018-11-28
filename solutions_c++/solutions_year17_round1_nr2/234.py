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
  int N, P; cin >> N >> P;
  int R[N];
  for (int i=0; i<N; i++)
    cin >> R[i];
  
  int tab[N][P];
  for (int i=0; i<N; i++)
  {
    for (int j=0; j<P; j++)
      cin >> tab[i][j];
    sort(tab[i], tab[i] + P);
  }
  
  int index[N];
  for (int i=0; i<N; i++)
    index[i] = 0;
  
  int result = 0;
  while (true)
  {
    int mini = -1000000000;
    int maxi = 1000000000;
    for (int i=0; i<N; i++)
    {
      mini = max(mini, (int)ceil(100. * tab[i][index[i]] / (110. * R[i])));
      maxi = min(maxi, (int)floor(100. * tab[i][index[i]] / (90. * R[i])));
    }
    
    //cout << mini << " " << maxi << endl;
    
    if (mini <= maxi)
    {
      result++;
      for (int i=0; i<N; i++)
        index[i]++;
    }
    else
    {
      for (int i=0; i<N; i++)
      {
        int m = floor(100. * tab[i][index[i]] / (90. * R[i]));
        if (m < mini)
          index[i]++;
      }
    }
    
    bool done = false;
    for (int i=0; i<N; i++)
      if (index[i] == P)
        done = true;
    if (done) break;
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
