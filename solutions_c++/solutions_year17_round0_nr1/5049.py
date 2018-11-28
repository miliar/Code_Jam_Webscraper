/*
tags: 
LANG: C++11
*/

#include<bits/stdc++.h> //g++ -std=c++11

using namespace std;

//#define DEBUG
#ifndef DEBUG
  #define din if(0) cin
  #define dout if(0) cout
#else
  #define din cin
  #define dout cout
#endif


#define inf (1 << 30)
#define pi (2*asin(1))
#define repall(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define rep(i,x,y) for (int i = x; i < y; i++)
#define irep(i,x,y) for (int i = x; i >= y; i--)
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define mp make_pair
#define MAX 100005

typedef vector < int > vi;
typedef pair < int , int > pii;
typedef vector < pii > vii;
typedef long long int i64;
typedef vector < i64 > vi64;
string s;
int k;
int ans;
bool sol()
{
  int pos = 0;
  ans = 0;
  while(pos + k <= (int)s.size())
  {
    int cnt = -1;
    rep(i, pos, pos + k)
    {
      if(s[i] == '-')
      {
        cnt = i;
        break;
      }
    }
    if(cnt>=0)
    {
      if(!(cnt + k <= (int)s.size())) return 0;
      rep(i, cnt, cnt + k)
      {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
      }
      pos++;
      ans++;
    }
    else pos+= k;
  }
  return 1;
}
int main() 
{
  int test;
  scanf("%d", &test);
  rep(te, 1, test+1)
  {
    cin>>s>>k;
    bool ok = sol();
    int pos = s.find('-');
    if(pos>= 0 && pos < (int)s.size())  ok = 0;
    
    if(ok) printf("Case #%d: %d\n", te, ans);
    else printf("Case #%d: IMPOSSIBLE\n", te);
  }
}
