#include <fstream>
#include <iostream>
#define l first
#define r second
#define MAXV 1441
#define INF 9999999
using namespace std;

int dp[MAXV][MAXV][2];

int solve(int act, int diff, int actp, int*segment)
{
  if(diff > 1440 || diff < 0) return INF;
  if(act == 1440) return diff != 720 ? INF : 0;
  if(dp[act][diff][actp] == -1)
  {
    bool ina = (segment[act] == 0), inb = (segment[act] == 1);

    if(!ina && !inb)
    {
      int answ = (act == 0 ? 1 : 0) + solve(act+1, diff + (actp==0?1:-1), actp, segment);
      int answ2 = 1 + solve(act+1, diff + (actp==0?-1:1), 1 - actp, segment);
      answ = min(answ, answ2);
      dp[act][diff][actp] = answ;
    }

    if(!ina && inb)
     dp[act][diff][actp] = (actp == 0 && act != 0 ? 0 : 1) + solve(act+1, diff + 1, 0, segment);

    if(!inb && ina)
     dp[act][diff][actp] = (actp == 1 && act != 0 ? 0 : 1) + solve(act+1, diff - 1, 1, segment);
  }
  return dp[act][diff][actp];
}

int main()
{
  int T;
  FILE*in = fopen("B-large.in", "r"), *out = fopen("output.txt", "w");
  fscanf(in, "%d", &T);

  for(int t=0; t<T; t++)
  {
    int A, B;
    fscanf(in, "%d%d", &A, &B);
    int segment[MAXV];
    for(int i=0; i<MAXV; i++)
     segment[i] = -1;

    for(int i=0, a, b; i<A; i++)
    {
      fscanf(in, "%d%d", &a, &b);
      for(int j=a; j<b; j++)
       segment[j] = 0;
    }

    for(int i=0, a, b; i<B; i++)
    {
      fscanf(in, "%d%d", &a, &b);
      for(int j=a; j<b; j++)
       segment[j] = 1;
    }

    for(int i=0; i<MAXV; i++)
     for(int j=0; j<MAXV; j++)
      for(int k=0; k<2; k++)
       dp[i][j][k] = -1;

    int answ = solve(0, 720, 0, segment);
    int up = (answ%2 == 1) ? -1 : 0;
    fprintf(out, "Case #%d: %d\n", (t+1), (answ+up));
  }
  fclose(in);
  fclose(out);
  return 0;
}
