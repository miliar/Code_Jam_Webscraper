#include <bits/stdc++.h>
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros
#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fr(i,n)     re(i,0,n)
#define repv(i,f,t) for(int i = f; i >= t; --i)
#define rev(i,f,t)  repv(i,f - 1,t)
#define frv(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define s(x) scanf("%d",&x)
#define i64 long long
#define gc() getchar()
inline i64 readLLD()
{
	i64 ret=0;
	bool negg=false;
	char c;
	c=gc();
	while((c<'0' || c>'9') && c!='-')
	{
		//scanf("%c",&c);
		c=gc();
	}
	if(c=='-'){negg=true;c=gc();}
	while(c>='0' && c<='9')
	{
		ret=ret*10+(c-'0');
		c=gc();
	}
	if(negg){ret=-ret;}
	return ret;
}//=readLLD();
inline int readInt()
{
	int ret=0;
	bool negg=false;
	char c;
	c=gc();
	while((c<'0' || c>'9') && c!='-')
	{
		c=gc();
	}
	if(c=='-')
	{
		negg=true;
		c=gc();
	}
	while(c>='0' && c<='9')
	{
		ret=ret*10+(c-'0');
		c=gc();
	}
	if(negg)
	{
		ret=-ret;
	}
	return ret;
}//=readInt();
long double PI=acos(-1);
#define MAX 1010
long double dp[MAX][MAX];
int main() {
	#define int long long
	int T; 
	cin>>T;
	rep(t,1,T){
		int K,N; 
		cin>>N>>K;
		vector<pair<double, double> > v;
		re(i,0,N){
			double r,h; 
			cin>>r>>h;
			v.pu(mp(r,h));
		}
		sort(all(v));
		reverse(all(v));
		re(i,0,MAX)re(k,0,MAX)
			dp[i][k]=0L;
		long double res=0L;
		re(i,0,v.size()){
			dp[i][1]=v[i].st*v[i].st*1.0L+2.0L*v[i].se*v[i].st;
			res=max(res,dp[i][1]);
		}
		re(i,1,v.size()){
			rep(k,2,K){
				dp[i][k]=dp[i-1][k];
				dp[i][k]=max(dp[i-1][k-1]*1.0L+2.0L*v[i].se*v[i].st,dp[i][k]);
				res=max(dp[i][k],res);
			}
		}
		res*=PI;
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(9)<<res<<endl;
	}
	return 0;
}