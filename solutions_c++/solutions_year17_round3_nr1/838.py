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
struct str{
	double r,h,a,a2;
};
bool comp(str a,str b){
	if(a.r>b.r){
		return true;
	}
	else{
		if(a.r==b.r){
			if(a.h>b.h){
				return true;
			}
			else{
				return false;
			}
		}
		else{
			return false;
		}
	}
}
bool comp1(double a,double b){
	return a>b;
}
int solve(){
	int n,k;
	cin>>n>>k;
	str s[n];
	for(int i=0;i<n;i++){
		double x,y;
		cin>>x>>y;
		s[i].r=x;
		s[i].h=y;
		s[i].a=(2*(PI)*s[i].r*s[i].h);
		s[i].a2=((PI)*s[i].r*s[i].r);
	}
	//sort(s,s+n,comp)
	double max=0;
	for(int i=0;i<n;i++){
		double ans=s[i].a+s[i].a2;
		vector<double> v;
		for(int j=0;j<n;j++){
			if(j!=i && s[j].r<=s[i].r){
				v.pb(s[j].a);
			}
		}
		sort(all(v),comp1);
		if(v.size()>=(k-1)){
		for(int i=0;i<(k-1);i++){
			ans+=v[i];
		}
		if(ans>max){
			max=ans;
		}
	   }
		
	}
	cout<<fixed<<setprecision(7)<<max<<endl;
	/*for(int i=0;i<k;++){
		ans+=((PI)*s[i].r*s[i].r)+(2*(PI)*s[i].r*s[i].h)
	}*/
	
   return 0;
}
int main(){
	freopen("bbbsak.txt","r",stdin);
	freopen("answerfirstbbb.txt","w",stdout);
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
