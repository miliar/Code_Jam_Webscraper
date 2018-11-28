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

int tab[100][100];
int tab2[100][100];

struct matching
{
  int A, B;
  vector<bool> seen;
  vector<int> otherA, otherB;
  vector<vector<bool>> edge, fixed;
  
  matching(int _A, int _B) :
    A(_A), B(_B), seen(A, false),
    otherA(A, -1), otherB(B, -1),
    edge(A, vector<bool>(B, false)),
    fixed(A, vector<bool>(B, false)) {}
  
  bool dfs(int act)
  {
    if (seen[act])
      return false;
    seen[act] = true;
    for (int i=0; i<B; i++)
    if (edge[act][i] && i != otherA[act])
    {
      if (otherB[i] == -1 || (!fixed[otherB[i]][i] && dfs(otherB[i])))
      {
        //cerr << otherA[act] << " " << otherB[i] << " ";
        otherB[i] = act;
        otherA[act] = i;
        //cerr << otherA[act] << " " << otherB[i] << endl;
        return true;
      }
    }
    return false;
  }
  
  void solve()
  {
    bool finished = false;
    while (!finished)
    {
      //cerr << "try" << endl;
      finished = true;
      fill(seen.begin(), seen.end(), false);
      for (int i=0; i<A; i++)
        if (otherA[i] == -1)
          if (dfs(i))
            finished = false;
    }
  }
};

void main2()
{
  int N, M; cin >> N >> M;
  for (int l=0; l<N; l++)
    for (int c=0; c<N; c++)
      tab2[l][c] = tab[l][c] = 0;
  for (int i=0; i<M; i++)
  {
    string s; cin >> s;
    int l, c; cin >> l >> c;
    if (s == "+" || s == "o") tab[l-1][c-1] |= 1;
    if (s == "+" || s == "o") tab2[l-1][c-1] |= 1;
    if (s == "x" || s == "o") tab[l-1][c-1] |= 2;
    if (s == "x" || s == "o") tab2[l-1][c-1] |= 2;
  }
  
  for (int l=0; l<N; l++)
  for (int c=0; c<N; c++)
  {
    bool ok = true;
    for (int i=0; i<N; i++)
      if (tab[l][i] & 2 || tab[i][c] & 2)
        ok = false;
    if (ok) tab[l][c] |= 2;
  }
  
  //  indices :  l+c   N-1+l-c 
  matching match(2*N-1, 2*N-1);
  for (int l=0; l<N; l++)
  for (int c=0; c<N; c++)
  {
    match.edge[l+c][N-1+l-c] = true;
    if (tab[l][c] & 1)
    {
      match.fixed[l+c][N-1+l-c] = true;
      match.otherA[l+c] = N-1+l-c;
      match.otherB[N-1+l-c] = l+c;
    }
  }
  
  match.solve();
  for (int i=0; i<2*N-1; i++)
  {
    if (match.otherA[i] != -1)
    {
      int l = (i + match.otherA[i] - N + 1) / 2;
      int c = (i - match.otherA[i] + N - 1) / 2;
      //cerr << i << " " << match.otherA[i] << " " << l << " " << c << endl;
      tab[l][c] |= 1;
    }
  }
  
  int y = 0, z = 0;
  for (int l=0; l<N; l++)
  for (int c=0; c<N; c++)
  {
    if (tab[l][c] != tab2[l][c]) z++;
    y += (tab[l][c] & 1) + (tab[l][c] >> 1);
  }
  
  cout << y << " " << z << endl;
  
  for (int l=0; l<N; l++)
  for (int c=0; c<N; c++)
  if (tab[l][c] != tab2[l][c])
  {
    if (tab[l][c] == 3)
      cout << "o " << l+1 << " " << c+1 << endl;
    else if (tab[l][c] == 2)
      cout << "x " << l+1 << " " << c+1 << endl;
    else if (tab[l][c] == 1)
      cout << "+ " << l+1 << " " << c+1 << endl;
    else
      cout << "error" << endl;
  }
  
  /*for (int l=0; l<N; l++)
  {
    for (int c=0; c<N; c++)
      if (tab[l][c] == 3)
        cerr << "o ";
      else if (tab[l][c] == 2)
        cerr << "x ";
      else if (tab[l][c] == 1)
        cerr << "+ ";
      else
        cerr << ". ";
    cerr << endl;
  }*/
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
