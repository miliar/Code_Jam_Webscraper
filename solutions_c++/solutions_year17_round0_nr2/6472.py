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
  ll len = s.size();
  vector<ll> v(len);
  for(ll i=0;i<len;i++)
  {
    v[i] = s[i]-'0';
  }
  for(ll i=0;i<len-1;i++)
  {
    if(v[i]>v[i+1])
    {
      v[i]--;
      ll j=i;
      while(j>0)
      {
        if(v[j]<v[j-1])
        {
          j--;
          v[j]--;
        }
        else break;
      }
      for(ll k=j+1;k<len;k++) v[k] = 9;
      break; 
    }
  }
  cout<<"Case #"<<t<<": ";
  ll a = 0;
  while(v[a]==0) a++;
  for(ll i=a;i<len;i++)
  {
    cout<<v[i];
  }
  cout<<endl;
}
	
int main()
{
  int t;
  scanint(t);
for(int i=1;i<=t;i++) solve(i);
}