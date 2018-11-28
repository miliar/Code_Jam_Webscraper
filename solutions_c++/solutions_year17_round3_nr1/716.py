#include <fstream>
#include <algorithm>
#include <iomanip>
#define r first
#define h second
#define ll long long
#define PI 3.141592653589793
#define MAXN 1001
#define ld long double
using namespace std;

ld dp[MAXN][MAXN];

ld solve(pair<ll, ll>*crc, int act, int N, int tk, int K)
{
  if(tk == K) return 0;
  if(act == N) return 0;

  if(dp[act][tk] == -1)
  {
    ld answ = solve(crc, act+1, N, tk, K); //leave
    ld A = (ld)2.0 * (ld)crc[act].h * (ld)crc[act].r * PI + (tk == 0 ? PI * (ld)crc[act].r * (ld)crc[act].r : 0);
    answ = max(answ, A + solve(crc, act+1, N, tk+1, K));
    dp[act][tk] = answ;
  }
  return dp[act][tk];
}

bool cmp(const pair<ll, ll> &a, const pair<ll, ll>&b)
{
  return a.r > b.r;
}

int main()
{
  int T;
  ifstream in("A-large.in");
  ofstream out("output.txt");
  in>>T;
  for(int t=0; t<T; t++)
  {
    int N, K;
    in>>N>>K;
    pair<ll, ll> crc[N];
    for(int i=0; i<N; i++)
     in>>crc[i].r>>crc[i].h;
    for(int i=0; i<=N; i++)
     for(int j=0; j<=N; j++)
      dp[i][j] = -1;
    sort(crc, crc+N, cmp);

    out<<"Case #"<<(t+1)<<": ";
    out<<std::fixed<<std::setprecision(9)<<solve(crc, 0, N, 0, K)<<"\n";
  }
  in.close();
  out.close();
  return 0;
}
