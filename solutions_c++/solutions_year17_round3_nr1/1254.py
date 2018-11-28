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

int t,n;

struct data {
  ll r, h;
};

bool myfunction(data i,data j)    //use it to sort vectors
{
    return i.h*i.r > j.h*j.r;
}

data a[1000];

int main() {

  si(t);
  int k;
  REP(prob, t) {
    si(n);
    si(k);
    REP(i, n) {
      sl(a[i].r);
      sl(a[i].h);
    }
    ll maxi = 0;
    REP(i, n) {
      vector<data> v;
      REP(j, n) {
        if (i == j || a[i].r < a[j].r){
          continue;
        }
        v.push_back(a[j]);
      }
      if (v.size()+1 < k) {
        continue;
      }
      sort(v.begin(), v.end(), myfunction);
      ll sum = 0;
      REP(j, k-1) {
        sum += v[j].r*v[j].h*2;
      }
      sum += 2*a[i].h*a[i].r + a[i].r*a[i].r;
      if (sum > maxi) {
        maxi = sum;
      }
    }
    double ans = maxi;
    ans *= M_PI;
    printf("Case #%d: %.8lf\n", prob+1, ans);
  }

  //system("pause");
  return 0;
}
