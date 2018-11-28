/* ***********************************************
Author        :yuanzhaolin
Created Time  :2017/4/23 2:13:15
File Name     :c.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <utility>
using namespace std;
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,a) for(int i=0;i<a;i++)
#define REP(i,a) for(int i=1;i<=a;i++)
#define per(i,a,b) for(int i=a-1;i>=b;i--)
#define foreach(i,a) for(int i=head[a];i>=0;i=ee[i].next)
#define Foreach(i,a) for(__typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define m0(x) memset(x,0,sizeof(x))
#define mff(x) memset(x,0xff,sizeof(x))
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x)*(x))
#define C1(x) cout<<x<<endl
#define C2(x,y) cout<<x<<" "<<y<<endl
#define C3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< pair<int,int> > VPII;
const ll mod=(ll)1e9+7;
const ll maxn=(ll)200+7;
const ll maxe=(ll)1e6+7;
const ll INF=(ll)1e11+7;
const double PI=acos(-1);
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
int n,Q;
int E[maxn],S[maxn];
double D[maxn][maxn];
int U,V;
double dp[maxn];
double solve()
{
	for(int i=1;i<=n;i++)
	{
		for(int j=i+2;j<=n;j++)
		{
			D[i][j]=D[i][j-1]+D[j-1][j];
		}
	}
	for(int i=0;i<maxn;i++) dp[i]=INF;
	dp[1]=0;
	for(int i=1;i<=n;i++)	
	{
		for(int j=i+1;j<=n;j++)	
		{
			if(D[i][j]<=E[i])
			{
				dp[j]=min(dp[j],dp[i]+1.0*D[i][j]/S[i]);
			}
		}
	}
	return dp[n];
}
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;    
	cin>>T;
	for(int ca=1;ca<=T;ca++)
	{
		printf("Case #%d: ",ca);
		cin>>n>>Q;
		for(int i=1;i<=n;i++)
			cin>>E[i]>>S[i];
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
				cin>>D[i][j];
		}
		while(Q--)
		{
			cin>>U>>V;
			printf("%.6f ",solve());
		}
		cout<<endl;
	}
    return 0;
}
