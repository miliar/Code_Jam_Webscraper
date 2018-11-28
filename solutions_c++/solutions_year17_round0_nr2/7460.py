#include <stdio.h>
#include <vector>  
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring> 
#include <queue>   
#include <list>


#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin();i!=(c).end();i++)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e5 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;

string recur(string s) {
  if(s.length()==1) return s;
  int i=0;
  for(i=0;i<s.length()-1;i++) {
    if(s[i]>s[i+1]) {
      if(s[i]=='1')s[i]='0';
      else s[i]=s[i]-1;
      i++;
      while(i<s.length()) s[i++]='9';
      break;
    }
  }
  
  return s;
}

int main() {
  int t,c=1;
  scanf("%d",&t);
  while(t--) {
    string s;
    cin>>s;
    printf("Case #%d: ",c++);
    if(s.length()==1) {
      cout<<s<<"\n";
      continue;
    }
    while(1) {
      string temp = recur(s);
      if(temp==s)break;
      s=temp;
    }
    string ans="";
    int i=0;
    while(s[i]=='0' && i<s.length())i++;
    while(i<s.length())ans+=s[i++];
    cout<<ans<<"\n";
  }
  return 0;
}