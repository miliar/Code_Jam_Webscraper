#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define sc(x) scanf("%d",&x)
#define scll(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)

#define EPS 1e-8

#define N 1123
int t,n,d;
int K[N], S[N];
double ans;

bool can(double v){
  double t;

  fr(i,0,n){
    if (S[i] >= v) continue;
    t = K[i]/(v-S[i]);
    //printf("v1:%lf and d2:%d v2:%d meet at:%lf\n",v,K[i],S[i],t*v);
    if (t*v < d) return 0;
  }

  return 1;
}

double go(){
  double st = EPS, en = 1e18;
  double mid;
  fr(i,0,10000){
    mid = (st+en)/2;

    //printf("can(%lf):%d\n",mid,can(mid));

    if (can(mid)) st = mid;
    else en = mid;
  }
  return mid;
}

int main(){
    sc(t);
    fre(ca,1,t){
      printf("Case #%d: ",ca);
      sc(d), sc(n);
      fr(i,0,n){
        sc(K[i]), sc(S[i]);
      }
      ans = go();
      printf("%.6lf\n",ans);

    }
    return 0;
}
