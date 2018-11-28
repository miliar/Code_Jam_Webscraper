
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

int cl(int x, int y)
{
  return (x+y-1) / y;
}

int DP[101][101][101][4];

int C[4];

const int inf = 100000000;

int f4(int c1 , int c2, int c3, int md)
{
  if (c1<0 or c2<0 or c3<0) return -inf;
  if (c1 + c2 + c3 == 0) return 0;
  int & ans = DP[c1][c2][c3][md];
  if (ans == -1)
  {
    ans = 0;
    if (c1>0) ans = max(ans, f4(c1-1, c2, c3, (md-1+4) % 4));
    if (c2>0) ans = max(ans, f4(c1, c2-1, c3, (md-2+4) % 4));
    if (c3>0) ans = max(ans, f4(c1, c2, c3-1, (md-3+4) % 4));
    if (md == 0) ans++;
  }
  return ans;
}


int f3(int c1 , int c2, int md)
{
  if (c1<0 or c2<0) return -inf;
  if (c1 + c2 == 0) return 0;
  int & ans = DP[c1][c2][md][0];
  if (ans == -1)
  {
    ans = 0;
    if (c1>0) ans = max(ans, f3(c1-1, c2, (md-1+3) % 3));
    if (c2>0) ans = max(ans, f3(c1, c2-1, (md-2+3) % 3));
    if (md == 0) ans++;
  }
  return ans;
}


int main()
{
  int t; 
  cin >> t; 
  int T = t; 
  while(t--)
  {
    int N, P;
    cin >> N >> P;
    memset(C,0,sizeof(C));
    for (int i = 0; i < N; i++)
    {
      int x; cin >> x;
      C[x%P]++;
    }
    cout << "Case #" << T-t << ": ";
    if (P == 2)
      cout << C[0] + cl(C[1],P);
    else if (P==3)
    {
      memset(DP, -1, sizeof(DP));
      cout << C[0] + f3(C[1], C[2], 0);
    }
    else
    {
      memset(DP, -1, sizeof(DP));
      cout << C[0] + f4(C[1], C[2], C[3], 0);
    }
    cout << endl;
  }
  return 0;	
}
