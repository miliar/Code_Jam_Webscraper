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
ll right(ll num){
	return num/2;
}
ll left(ll num){
	if(num%2==0){
		return (num/2)-1;
	}
	else{
		return num/2;
	}
}
vl v;
int build(long n){
	if(n==1){
		v.pb(n);
		return 0;
	}
	if(n==0){
		return 0;
	}
	v.pb(n);
	long x=right(n);
	long y=left(n);
	//v.pb(x);
	//v.pb(y);
	build(x);build(y);
	return 0;
}
bool comp(long a,long b){
	return a>b;
}
int solve(){
	long long n,k;
	cin>>n>>k;
	build(n);
	sort(all(v),comp);
	long ans=v[k-1];
	if(ans<=0){
		ans=1;
	}
	v.clear();
	cout<<right(ans)<<" "<<left(ans)<<endl;
	return 0;
}

int main(){
	
	freopen("C-small-2-attempt0.txt","r",stdin);
	freopen("code3b.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	long t=1;
	cin>>t;
	//cout<<t<<endl;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		solve();
	}
		
	return 0;
}
