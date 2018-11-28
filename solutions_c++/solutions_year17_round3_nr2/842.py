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
	int i,f;
};

bool comp1(double a,double b){
	return a>b;
}
int solve(){
	int a,b;
	cin>>a>>b;
	str m[a],p[b];
	for(int i=0;i<a;i++){
		int x,y;
		cin>>x>>y;
		m[i].i=x;
		m[i].f=y;
	}	
	for(int i=0;i<b;i++){
		int x,y;
		cin>>x>>y;
		p[i].i=x;
		p[i].f=y;
	}
	if(a!=2 && b!=2){
		cout<<2<<endl;
	}
	else{
		if(a==2){
			if(m[0].i<m[1].i){
				if((m[1].f-m[0].i)<=720 || ((1440-m[1].i)+(m[0].f))<=720){
					cout<<2<<endl;
				}
				else{
					cout<<4<<endl;
				}
			}
			else{
					if((m[0].f-m[1].i)<=720 || ((1440-m[0].i)+(m[1].f))<=720){
					cout<<2<<endl;
				}
				else{
					cout<<4<<endl;
				}
				}
			
		}
		else{
			if(b==2){
			if(p[0].i<p[1].i){
				if((p[1].f-p[0].i)<=720 || ((1440-p[1].i)+(p[0].f))<=720){
					cout<<2<<endl;
				}
				else{
					cout<<4<<endl;
				}
			}
				else{
					if((p[0].f-p[1].i)<=720 || ((1440-p[0].i)+(p[1].f))<=720){
					cout<<2<<endl;
				}
				else{
					cout<<4<<endl;
				}
				}
			
		}
		}
	}
   return 0;
}
int main(){
	freopen("B-small-attempt0aa.txt","r",stdin);
	freopen("answersecond.txt","w",stdout);
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
