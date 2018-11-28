
#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define pi(x) printf("%d\n",x)
#define F first
#define S second
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;

const LL inf = 1e15;
const double fINF = 1e15;

LL E[100]; int S[100];

LL D[100][100];

double fD[100][100];

int main()
{int t; cin >> t; int T = t; while(t--){

int N, Q; cin >> N >> Q;

for (int i = 0; i < N; i++) cin >> E[i] >> S[i];

for (int i = 0; i < N; i++)
for (int j = 0; j < N; j++)
  cin >> D[i][j];

for (int i = 0; i < N; i++) D[i][i] = 0;

for (int i = 0; i < N; i++)
for (int j = 0; j < N; j++)
  if (D[i][j] == -1) D[i][j] = inf;

for (int k = 0; k < N; k++)
for (int i = 0; i < N; i++)
for (int j = 0; j < N; j++)
  D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

for (int i = 0; i < N; i++)
{
  for (int j = 0; j < N; j++)
    if (D[i][j] <= E[i])
    {
      fD[i][j] = D[i][j]; fD[i][j] /= S[i];
    }
    else
    {
      fD[i][j] = fINF;
    }
  fD[i][i] = 0;
}

for (int k = 0; k < N; k++)
for (int i = 0; i < N; i++)
for (int j = 0; j < N; j++)
  fD[i][j] = min(fD[i][j], fD[i][k] + fD[k][j]);
cout << "Case #" << T-t << ":";
while(Q--) {
  int sr, dt; cin >> sr >> dt; sr--; dt--;
  printf(" %.7lf", fD[sr][dt]);
}
cout << endl;

}return 0;}
