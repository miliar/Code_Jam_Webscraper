#include <iostream> 
#include <cmath>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <limits>
#include <sstream>
#include <queue>
#include <cstring>
#include <stack>
#include <cstdio>
#include <map>
#include <bitset>
#include <iomanip> 
using namespace std;

 typedef long long ll;
 typedef vector<int> vi;
#define MOD 1000000007
// #define MAX 10000000
 
#define gc getchar_unlocked
void scanll(long long &x)
{
    register long long c = gc();
    x = 0;
    long long neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

void solve(int t)
{
  string s;
  cin>>s;
  ll k;
  scanll(k);
  ll count=0;
  ll len = s.size();
  vector<bool> v(len);
  for(ll i=0;i<len;i++)
  {
    if(s[i]=='+') v[i]=1;
    else v[i]=0;
  }
  for(ll i=0;i<=len-k;i++)
  {
    if(!v[i])
    {
      for(ll j=0;j<k;j++) v[i+j] = 1-v[i+j];
      count++;
    } 
  }
  for(ll i=0;i<len;i++)
  {
    if(!v[i])
    {
      cout<<"Case #"<<t<<": IMPOSSIBLE\n";
      return;
    }
  }
  cout<<"Case #"<<t<<": "<<count<<endl;
}
	
int main()
{
  int t;
  scanint(t);
for(int i=1;i<=t;i++) solve(i);
}