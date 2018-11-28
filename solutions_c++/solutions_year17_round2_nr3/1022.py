
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
typedef pair<double, double> ii;
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
int n,q;
double dist[10005];
ii horse[10005];

double dp[1005][1005];


double func(int index, int horseIndex) {
    if(index == n-1)
        return 0;
    if(dp[index][horseIndex] != -1.0)
        return dp[index][horseIndex];

    double d = dist[index];
    int horseCovered = 0;
    if(index > horseIndex) {
        for (int i = horseIndex; i < index; ++i)
            horseCovered += dist[i];
    }
    int horseEnergyLeft = horse[horseIndex].first - horseCovered;
    double time1 = d/horse[horseIndex].second;
    double time2 = d/horse[index].second;


    double op1 = 1e15, op2 = 1e15;

    if(horseEnergyLeft >= d) {
        op1 = time1 + func(index+1, horseIndex);
        op2 = time2 + func(index+1, index);
    }
    else {
        op2 = time2 + func(index+1, index);
    }
    return dp[index][horseIndex] = min(op1, op2);
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

        for (int i = 0; i < 101; ++i)
            for (int j = 0; j < 101; ++j)
                dp[i][j] = -1.0;

        cin>>n>>q;
        for (int i = 0; i < n; ++i)
            cin>>horse[i].first>>horse[i].second;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                int x;
                cin>>x;
                if(x != -1) {
                    dist[i] = x;
                }
            }
        }
        for (int i = 0; i < q; ++i)
        {
            int x,y;
            cin>>x>>y;
        }
        double ans = func(0,0);
        cout<<"Case #"<<tt<<": "<<setprecision(8)<<fixed<<ans<<"\n";
        tt++;
    }
}













