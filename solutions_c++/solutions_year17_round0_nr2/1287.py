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

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( i.x > j.x ) return false;
    return i.y < j.y;
}
*/

char s[100];

bool isTidy() {
  REP(i, n-1) {
    if (s[i] > s[i+1]) {
      return false;
    }
  }
  return true;
}

bool special() {
 if (s[0] != '1') {
   return false;
 }
  FOR(i, 1, n) {
    if (s[i] != '1' && s[i] != '0') {
      return false;
    } else if (s[i] == '0') {
      return true;
    }
  }
  return false;
}

void tidy() {
  int done = 0;
  FOR(i, 1, n) {
    if (done) {
      s[i] = '9';
    } else {
      if (s[i] < s[i-1]) {
        done = 1;
        s[i] = '9';
        FORR(j, i-1) {
          if (j == 0) {
            s[j] = s[j] - 1;
          } else if (s[j] == s[j-1]) {
            s[j] = '9';
          } else {
            s[j] = s[j] - 1;
            break;
          }
        }
      }
    }
  }
}

int main() {

  si(t);
  REP(prob, t) {
    ss(s);
    n = strlen(s);
    if (isTidy()) {
      printf("Case #%d: %s\n", prob+1, s);
    } else {
      if (special()) {
        REP(i, n-1) {
          s[i] = '9';
        }
        s[n-1] = '\0';
      } else {
        tidy();
      }
      printf("Case #%d: %s\n", prob+1, s);
    }
  }

  //system("pause");
  return 0;
}
