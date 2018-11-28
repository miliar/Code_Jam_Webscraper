/*   ARSHEYA RAJ   */

#include <iostream>
#include <bits/c++io.h>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <exception>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iterator>
#include <climits>
 
#define ll long long int
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a>b)?b:a
#define FOR(i,n) for(int i=1;i<=n;i++)
#define FOR_X(i,x,n) for(i=x;i<n;i++)
#define BACK(i,n) for(i=n;i>0;i--)
#define BACK_X(i,n,x) for(i=n;i>=x;i--)
#define fill(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define pp pair<int,int>
#define mod 1000000007
#define MAX_N 1000005
#define MAXVAL 100000000
#define MINVAL -100000000

template< class T > T sq(T &x) { return x * x; }
template< class T > T abs(T &n) { return (n < 0 ? -n : n); }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T &a, T &b, T &c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }

const double EPS = 1e-10;
const int INF = 0x3f3f3f3f;

using namespace std;
ll n;
double d,k[1005],s[1005];

bool check (double x)
{
	for (int i = 0; i < n; ++i)
	{
		double t1 = d/x;
		double t2 = (d-k[i])/s[i];
		if(t1<(t2+EPS))
			return 0;
	}
	return 1;
}

double binary_search(double low,double high)
{
	double mid;
	int x = 1000;
	while(x--)
	{
		mid = (low+high)/2.0;
		if(check(mid))
			low = mid;
		else
			high = mid;
	}
	return low;
}

int main(){
	freopen("in.txt","r",stdin);
	 freopen("out.txt","w",stdout);
	ll t;
	cin>>t;
	for(ll T=1; T<=t; T++)
	{
		cin>>d>>n;
		for (int i = 0; i < n; ++i)
		{	
			cin>>k[i]>>s[i];
			// cout<<k[i];
		}
		cout<<"Case #"<<T<<": "<<setprecision(9)<<fixed<<binary_search(1.0,1000000000000000000.0)<<endl;
	}
return 0;
}