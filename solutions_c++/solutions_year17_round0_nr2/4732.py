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
/*int digit(long long num){
	int dig=0;
	while(num>0){
		num=num/10;
		dig++;
	}
	return dig;
}*/
int check(long long num){
	int last=num%10;
	int x;
	while(num>0){
		 x=num%10;
		if(x>last){
			return 0;
		}
		else{
			last=x;
			 num=num/10;
		}
	}
	return 1;
}
int fun(long long num){
	if(num<=9){
		cout<<num;
		return 0;
	}
	vi v;
	int x=num%10;
	v.pb(x);
	num/=10;
	while(num>0){
		x=num%10;
		v.pb(x);
		num/=10;
	}
	vi w;
	int n=v.size();
	for(int i=0;i<n;i++){
		w.pb(v[n-i-1]);
	}
	int temp=w[0],in=0;
	for(int i=1;i<w.size();i++){
		
		if(w[i]<w[i-1]){
			temp=w[i-1];
			in=i;
			break;
		}
	}
	
	if(in==0){
			for(int i=0;i<n;i++)cout<<w[i];
			return 0;
		}
	if(temp==1){
		for(int i=1;i<n;i++)cout<<9;
		
	}
	else{
		
	for(int i=0;i<n;i++){
		if(w[i]<temp){
			cout<<w[i];
		}
		else{
			cout<<w[i]-1;
			for(int j=i+1;j<n;j++){
				cout<<9;
			}
			break;
		}
	}
    }
	return 0;
}
int solve(){
	long long num;
	cin>>num;
	
	fun(num);
	cout<<endl;
	
	return 0;
}

int main(){
	
	freopen("B-large.txt","r",stdin);
	freopen("code2large.txt","w",stdout);
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
