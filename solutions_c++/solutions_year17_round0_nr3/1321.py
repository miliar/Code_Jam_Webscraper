#include<iostream>
#include <assert.h>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define sss(n, size) fgets(n, size, stdin)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

ll gcd(ll r0, ll r1)
{
    if(r0==0 || r1==0)
    return 1;

    if(r0<r1)
    return gcd(r1,r0);

    if(r0%r1==0)
    return r1;

    return gcd(r1,r0%r1);
}
ll findInverse(ll a, ll b)
{
    ll x[3];
    ll y[3];
    ll quotient  = a / b;
    ll remainder = a % b;
    x[0] = 0;
    y[0] = 1;
    x[1] = 1;
    y[1] = quotient * -1;

    int l=2, m=1, n=0;
    for (; (b % (a%b)) != 0;)
    {
        a = b;
        b = remainder;
        quotient = a / b;
        remainder = a % b;
        x[l] = (quotient * -1 * x[m]) + x[n];
        y[l] = (quotient * -1 * y[m]) + y[n];
        int tt = l;l=n;n=m;m=tt;
    }
    //x[i — 1 % 3] is inverse of a
    //y[i — 1 % 3] is inverse of b
    return x[m];
}

int t;
ll n;

struct data {
  ll v, cnt;
  data() {}
  data(ll v_, ll cnt_) {
    v = v_;
    cnt = cnt_;
  }
};

bool myfunction(data i,data j)    //use it to sort vectors
{
    return i.v > j.v;
}

data h[62][10000000];
int hi[62];

int main() {

  si(t);
  ll k;
  REP(prob, t) {
    sl(n);
    sl(k);
    memset(hi, 0, sizeof(hi));
    h[0][0] = data(n, 1);
    hi[0] = 1;
    ll al, ar;
    int lat = 0;
    while(k > 0) {
      sort(h[lat], h[lat]+hi[lat], myfunction);
      for (int i = 0; i < hi[lat] && k>0; i++) {
        data dat = h[lat][i];
        al = (dat.v-1)/2;
        ar = dat.v-1-al;
        k -= dat.cnt;
        if (al > 0) {
          int found = 0;
          REP(j, hi[lat+1]) {
            if (h[lat+1][j].v == al) {
              found = 1;
              h[lat+1][j].cnt += dat.cnt;
              break;
            }
          }
          if (!found) {
            h[lat+1][hi[lat+1]] = data(al, dat.cnt);
            hi[lat+1]++;
          }
        }
        if (ar > 0) {
          int found = 0;
          REP(j, hi[lat+1]) {
            if (h[lat+1][j].v == ar) {
              found = 1;
              h[lat+1][j].cnt += dat.cnt;
              break;
            }
          }
          if (!found) {
            h[lat+1][hi[lat+1]] = data(ar, dat.cnt);
            hi[lat+1]++;
          }
        }
      }
      lat++;
    }
    printf("Case #%d: %lld %lld\n", prob+1, ar, al);
  }

  //system("pause");
  return 0;
}
