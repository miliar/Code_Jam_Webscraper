#include<bits/stdc++.h>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define pll         pair<long,long>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define loop(i,a,b)	for(long i=a;i<b;i++)
#define PI 			3.141592653589793l
#define vl          vector<long>
#define inf         1000000000000000000
using namespace std;
long max(long a,long b){
	if(a>b)
	 return a;
	 else
	 return b;
}
static long gcd(long a, long b) {
  long r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}
int lcm(int a, int b)
{
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}
/*typedef unsigned long long uint64;

uint64 PowMod(uint64 x, uint64 e, uint64 mod)
{
  uint64 res;

  if (e == 0)
  {
    res = 1;
  }
  else if (e == 1)
  {
    res = x;
  }
  else
  {
    res = PowMod(x, e / 2, mod);
    res = res * res % mod;
    if (e % 2)
      res = res * x % mod;
  }

  return res;
}*/
//long long fact[]={1,1,2,6,24.120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,6227020800*14,6227020800*14*15,6227020800*14*15*16,6227020800*14*15*16*17,6227020800*14*15*16*17*18,6227020800*14*15*16*17*18*19};
bool comp(pair<long,long> a , pair<long,long> b ){
	return a.first>b.first;
}
int solve(){
	long n,d;
	cin>>d>>n;
	vector<pair<long,long> > v(n);
	for(int i=0;i<n;i++){
		long k,s;
		cin>>k>>s;
		v[i].first=k;
		v[i].second=s;
	}
	sort(v.begin(),v.end(),comp);
	double a[n];
	double last=-1;
	for(int i=0;i<n;i++){
		double t1;
		t1=double(double(d)-double(v[i].first))/double(v[i].second);
		if(t1<last){
			a[i]=last;
		}
		else{
			a[i]=t1;
			last=t1;
		}
	}
	cout<<fixed<<setprecision(7)<<double(d)/double(last)<<endl;
	
}
int main(){
	
	freopen("A-large1b.txt","r",stdin);
	freopen("code111.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	long t=1;
	cin>>t;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		solve();
	}
		
	return 0;
}
