#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
#include<cassert>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int dp[110][110][110];
int num[5];
int rec(int x,int y,int z){
	if(x+y+z<1) return 0;
	if(dp[x][y][z]>=0) return dp[x][y][z];
	int ret=1;
	if(x>=2 && y>=1) ret=max(ret,1+rec(x-2,y-1,z));
	if(z>=2 && y>=1) ret=max(ret,1+rec(x,y-1,z-2));
	if(x>=1 && z>=1) ret=max(ret,1+rec(x-1,y,z-1));
	if(y>=2) ret=max(ret,1+rec(x,y-2,z));
	if(x>=4) ret=max(ret,1+rec(x-4,y,z));
	if(z>=4) ret=max(ret,1+rec(x,y,z-4));
	return dp[x][y][z]=ret;
}
int cal(int x){
	if(x==2){
		return num[0]+(1+num[1])/2;
	}
	if(x==3){
		int y=min(num[1],num[2]);
		num[1]-=y;num[2]-=y;
		int z=max(num[1],num[2]);
		return num[0]+y+(2+z)/3;
	}
	return num[0]+rec(num[1],num[2],num[3]);
}
int main()
{
	int t,n,p,a;
	cin>>t;
	memset(dp,-1,sizeof(dp));
	rep(i,t){
		cin>>n>>p;
		memset(num,0,sizeof(num));
		rep(j,n){
			cin>>a;num[a%p]++;
		}
		printf("Case #%d: %d\n",i+1,cal(p));
	}
}
