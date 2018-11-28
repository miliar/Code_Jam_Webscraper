
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdlib>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>


using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
 
#define INF                         (int)1e9
#define EPS                         1e-9
int mod = 1000000007;
 
long long pwr(long long a,long long b,long long mod)
{
  if(b==0)
    return 1;
  long long temp=pwr(a,b/2,mod);
  temp=(temp*temp)%mod;
  if(b&1)
    temp=(temp*a)%mod;
  return temp;
}
long long pwr(long long a,long long b)
{
  if(b==0)
    return 1;
  long long temp=pwr(a,b/2);
  temp=(temp*temp);
  if(b&1)
    temp=(temp*a);
  return temp;
}
bool* isPrime;
void generatePrimeSieve(const int lim)
{
  isPrime=(bool *)malloc(lim+1);
  memset(isPrime,true,lim+1);
  isPrime[0]=false;
  isPrime[1]=false;
  for(int i=2;i<=lim;++i)
    if(isPrime[i])
      for(int j=i+i;j<=lim;j+=i)
        isPrime[j]=false;
}

long long modularInverse(long long a,long long m)
{
      return pwr(a,m-2,m);
}
int n,k;
string s;
int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int q, t = 0;
    cin>>q;
    while(q--) {
        t++;
        cin>>s>>k;
        n = s.length();
        int ans = 0;
        for (int i = 0; i <= n-k; ++i)
        {
            if(s[i] == '+')
                continue;
            for (int j = i; j < i + k; ++j)
            {
                if(s[j] == '+')
                    s[j] = '-';
                else
                    s[j] = '+';
            }
            ans++;
        }
        int flg = 1;
        for (int i = 0; i < n; ++i)
            if(s[i] == '-')
                flg = 0;
        if(flg)
            cout<<"Case #"<<t<<": "<<ans<<"\n";
        else
            cout<<"Case #"<<t<<": IMPOSSIBLE\n";
    }
}



