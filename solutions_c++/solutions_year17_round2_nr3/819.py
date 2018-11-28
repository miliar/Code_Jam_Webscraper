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
  ll e, s;
};

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( i.x > j.x ) return false;
    return i.y < j.y;
}
*/

ll a[100][100];
data d[1000];
double ans[1000];

int main() {

  si(t);
  int q;
  REP(prob, t) {
    si(n);
    si(q);
    REP(i, n) {
      sl(d[i].e);
      sl(d[i].s);
    }
    REP(i, n) {
      REP(j, n) {
        sl(a[i][j]);
      }
    }
    REP(i, n) {
      ans[i] = 10000000000000000LL;
    }
    ans[0] = 0;
    REP(i, n-1) {
      ll dt = d[i].e;
      int at = i;
      double last = ans[i];
      while (at < n-1 && dt >= a[at][at+1]) {
        double temp = a[at][at+1];
        temp/=d[i].s;
        ans[at+1] = min(ans[at+1], last+temp);
        last += temp;
        dt -= a[at][at+1];
        at++;
      }
    }
    int x,y;
    REP(i, q) {
      si(x);
      si(y);
      printf("Case #%d: %.6lf\n", prob+1, ans[n-1]);
    }
  }

  //system("pause");
  return 0;
}
