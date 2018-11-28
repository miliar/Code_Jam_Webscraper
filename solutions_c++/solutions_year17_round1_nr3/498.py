#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

#define INF 320000
#define MAXQ 80
int  ad, ak, b, d, ohd;

int PD[102][102][MAXQ+1][MAXQ+1];

int solve(int hd, int hk, int qb, int qd) {
  if(hk<=0) return 0;
  if(hd<=0) return INF;
  if(PD[hd][hk][qb][qd]==-2)
    return INF;
  if(PD[hd][hk][qb][qd]!=-1)
    return PD[hd][hk][qb][qd];
  PD[hd][hk][qb][qd] = - 2;
  int cd = ad + qb*b;
  int ck = max(0, ak - qd*d);
  int r = solve(hd - ck, hk - cd, qb, qd) + 1;
  if(b>0 && qb < MAXQ) {
    r = min(r, solve(hd - ck, hk, qb+1,qd) +1);
  }
  if(d>0 && qd < MAXQ ) {
    int ck2 = max(0, ak - (qd+1)*d);
    r = min(r, solve(hd - ck2, hk, qb, qd+1) + 1); 
  }
  if(hd != ohd) {
    r = min(r, solve(ohd - ck, hk, qb, qd) + 1);
  }
  return PD[hd][hk][qb][qd] = r;
}


int main() {
  int t;
  cin >> t;
  for(int caso = 1; caso<=t;caso++) {
    int  hk;
    cin >> ohd >> ad >> hk >> ak >> b >> d;
    memset(PD,-1,sizeof(PD));
    int ret = solve(ohd,hk,0,0);
    if(ret < INF)
      printf("Case #%d: %d\n", caso, ret);
    else printf("Case #%d: IMPOSSIBLE\n", caso);
  }

  return 0;
}
