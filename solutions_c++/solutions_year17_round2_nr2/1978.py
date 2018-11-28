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
bool comp(pair<char,int> a , pair<char,int> b ){
	return a.second>b.second;
}
int solve(){
	int n;
	cin>>n;
	vector<pair<char,int> > v(3);
	int tt=0;
	for(int i=0;i<6;i++){
		int x;
		cin>>x;
		if(i!=1 && i!=3 && i!=5){
		v[tt].second=x;
		tt++;
	 }
	}
	//v[0].first='R';v[1].first='O';v[2].first='Y';v[3].first='G';v[4].first='B';v[5].first='V';
	v[0].first='R';v[1].first='Y';v[2].first='B';
	sort(v.begin(),v.end(),comp);
	int a=v[0].second;
	int b=v[1].second;
	int c=v[2].second;
	//cout<<v[0].first<<" "<<v[1].first<<" "<<v[2].first<<endl;
	if(0){
		cout<<"IMPOSSIBLE"<<endl;
		return 0;
	}
	else{
		vector<char> w;
		for(int i=0;i<c;i++){
			w.pb(v[0].first);
			w.pb(v[1].first);
			w.pb(v[2].first);
		}
		for(int i=0;i<(b-c);i++){
			w.pb(v[0].first);
			w.pb(v[1].first);
		}
		int j=2;
		if(c>=(a-b)){
		/*	int z=0,k=0;
			while(z<(a-b)){
				cout<<w[k];
				k++;
				cout<<w[k];
				k++;
				cout<<v[0].first;
				z++;
			}
			for(;k<w.size();k++){
				cout<<w[k];
			}
			cout<<endl;*/
		for(int i=0;i<(a-b);i++){
			if(j==w.size()){
				cout<<"IMPOSSIBLE"<<endl;
				return 0;
			}
			w.insert(w.begin()+j,v[0].first);
			j=j+4;
		}
		for(int i=1;i<n-1;i++){
			if(w[i]==w[i-1] || w[i]==w[i+1]){
				cout<<"IMPOSSIBLE"<<endl;
			}
		}
		if(w[0]!=w[n-1]){
			for(int i=0;i<n;i++){
				cout<<w[i];
			}
			cout<<endl;
			return 0;
		}
		else{
			cout<<"IMPOSSIBLE"<<endl;
			return 0;
		}
	    }
	    else{
	    	cout<<"IMPOSSIBLE"<<endl;
	    	return 0;
		}
	}
	
}
int main(){
	
	freopen("B-small-attempt2.txt","r",stdin);
	freopen("codedcba.txt","w",stdout);
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
