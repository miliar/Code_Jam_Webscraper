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
string sol(int pos, bool free, char last)
{
  if(pos == (int)s.size()) return "";
  string ans = "";
  bool first = 0;
  char beg = s[pos];
  if(free) beg = '9';
  //cout<<pos<<"  "<<free<<" "<<last<<" "<<beg<<endl;
  for(char i = beg; i >= last ; i--)
  {
    string next;
    if(i == s[pos])
      next = sol(pos + 1, 0, (char)(i));
    else
      next = sol(pos + 1, 1, (char)(i));
      
    if(next == "error") continue;
    
    if(first)
      ans = (char)(i) + next;
    else
      ans = max(ans, (char)(i) + next);
    
    first = 1;
    if(ans != "") break;
  }
  if(!first) return "error";
  return ans;
}
int main() 
{
  int test;
  scanf("%d", &test);
  rep(te, 1, test+1)
  {
    cin>>s;
    string ans  = sol(0, 0, '0');
    int pos = 0;
    while(ans[pos] == '0') pos++;
    ans = ans.substr(pos);
    printf("Case #%d: ", te);
    cout<<ans<<endl;
  }
}
