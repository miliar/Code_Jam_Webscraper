/*Against all odds .......*/
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <queue>
#include <cmath>
#include <algorithm>
#include <functional>
#include <list>
#include <deque>
#include <bitset>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <numeric>
#include <cassert>
#include <climits>
#include <utility>
#include <ctime>
#include <tuple>
#include <fstream>
#define T int test_case; scanf("%d",&test_case); while(test_case--)
#define FOR(i,a,n) for(i=a;i<n;i++)
#define FORD(i,a,n) for(i=a;i>=n;i--)
#define FORS(i,a) for(i=0;a[i];i++)
#define si(x) scanf("%d",&x)
#define sc(x) cin>>x
#define sd(x) scanf("%lf",&x)
#define sll(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define prs(x) printf("%d ",x)
#define pls(x) printf("%lld ",x)
#define pc(x) printf("%c",x)
#define pi(x) printf("%d\n",x)
#define pd(x) cout.precision(10),cout<<fixed<<x<<endl;
#define pll(x) printf("%lld\n",x)
#define ps(x) printf("%s\n",x)
#define M 1000000007
#define ll long long
#define mp make_pair
#define all(x) x.begin(),x.end()
#define pb push_back
#define fr first
#define se second
#define in insert
#define er erase
#define pii pair<int, int>
#define plll pair<long long, long long>
#define tr(x,it) for(auto it : x)
#define INF 1ll<<60
#define PI 3.14159265358979323846264338327950288419716939937510582097494459230
#define bs(x,lo,hi,mid) cout<<x<<" "<<lo<<" "<<hi<<" "<<mid<<endl;
using namespace std;
ll gcd (ll a, ll b) {return ( a ? gcd(b%a, a) : b );}
ll power(ll a, ll n) {ll p = 1;while (n > 0) {if(n&1) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n, ll mod) {ll p = 1;while (n > 0) {if(n&1) {p = p * a; p %= mod;} n >>= 1; a *= a; a %= mod;} return p % mod;}
vector<int> prime;
bool primee[10000000];
void primegen(ll x) { for(ll i=2;i*i<=x;i++) if(!primee[i]) for(ll j=i*i;j<=x;j+=i) primee[j]=true; for(ll i=2;i<=x;i++) if(!primee[i]) prime.push_back(i);}

double a[1005];

int main()
{
   int i,j;
   int test_case;
   si(test_case);
   for(int test=1;test<=test_case;test++)
   {
   	double d,n;
   	sd(d);
   	sd(n);
   	double t=-1,sp,pos;
   	while(n--)
   	{
   		sd(pos);
   		sd(sp);
   		t=max(t,(d-pos)/sp);
   	}
   	double ans=d/t;
   	printf("Case #%d: ",test);
   	pd(ans);
   }
   return 0;
}
