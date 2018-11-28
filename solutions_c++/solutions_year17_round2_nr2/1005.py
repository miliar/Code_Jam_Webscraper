
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
int n,r,o,y,g,b,v;
string s;

int func(int last) {

    if(last == -1) {
        if(r >= g && r >= b)
            return 0;
        if(g >= r && g >= b)
            return 1;
        if(b >= r && b >= g)
            return 2;
    }

    if(last == 0) {
        if(g > b)
            return 1;
        if(g == b) {
            if(s[0] == 'Y')
                return 1;
            if(s[0] == 'B')
                return 2;
            return 1;
        }
        return 2;            
    }
    if(last == 1) {
        if(b > r)
            return 2;
        if(b == r) {
            if(s[0] == 'R')
                return 0;
            if(s[0] == 'B')
                return 2;
            return 2;
        }
        return 0;
    }
    if(last == 2) {
        if(r > g)
            return 0;
        if(r == g) {
            if(s[0] == 'R')
                return 0;
            if(s[0] == 'Y')
                return 1;
            return 0;
        }
        return 1;
    }

    return -1;
}



int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin>>t;
    int tt = 1;
    while(t--) {
        cin>>n>>r>>o>>g>>y>>b>>v;
        s = "";
        int last = -1;
        int flg = 1;
        for (int i = 0; i < n; ++i)
        {   
            int x = func(last);
            if(x == -1)
                flg = 0;
            last = x;
            if(x == 0){
                if(r <= 0)
                    flg = 0;
                s += 'R';
                r--;
            }
            if(x == 1){
                if(g <= 0){
                    // cout<<"sss\n";
                    flg = 0;
                }
                s += 'Y';
                g--;
            }
            if(x == 2){
                if(b <= 0)
                    flg = 0;
                s += 'B';
                b--;
            }
        }
        // cout<<s<<" "<<flg<<endl;
        if(flg && s[0] != s[n-1]) {
            cout<<"Case #"<<tt<<": "<<s<<"\n"; 
        }   
        else {
            cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
        }
        tt++;
    }
}













