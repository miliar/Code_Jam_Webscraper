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

int solve(){
	string s;
	int k;
	cin>>s>>k;
	int count=0,flag=1;
	int n=s.length();
	for(int i=0;i<=n-k;i++){
		if(s[i]=='-'){
			count++;
			for(int j=i;j<i+k;j++){
				if(s[j]=='+'){
					s[j]='-';
				}
				else{
					s[j]='+';
				}
			}
		}
	}
	for(int i=n-k;i<n;i++){
		if(s[i]=='-'){
			flag=0;
			break;
		}
	}
	if(flag==1){
		cout<<count<<endl;
	}
	else{
		cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}

int main(){
	
	freopen("A-large.txt","r",stdin);
	freopen("code1large.txt","w",stdout);
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
