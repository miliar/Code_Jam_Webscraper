/*---------------------------------------------
				Author:TanYz
---------------------------------------------*/
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <string>
#include <cmath>
#include <map>
#include <bitset>
#include <set>
#include <vector>
#include <cstdlib>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define mpii(a,b) make_pair(a,b)
const int INF=1<<30;
const int maxn=1000+233;
const int mod=1000000007;
const double PI=acos(-1);

struct Pie
{
	double r,h,s;
	int id;
	void read(){
		scanf("%lf%lf",&r,&h);
		s=2*PI*r*h;
	}
	bool operator < (const Pie &rhs)const {
		return r<rhs.r;
	}
}p[maxn];

bool cmp(Pie &a,Pie &b)
{
	return a.s<b.s;
}

int T,kase=0;
int n,k;
int t[maxn][maxn];
double dp[maxn][maxn];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)p[i].read();
		sort(p,p+n);
		for(int i=0;i<n;i++){
			p[i].id=i;
			for(int j=0;j<n;j++){
				if(p[i].r==p[j].r)
					t[i][j]=0;
				else if(p[i].r<p[j].r)
					t[i][j]=-1;
				else t[i][j]=1;
			}
		}
		sort(p,p+n,cmp);
		double ans=0;
		for(int i=0;i<n;i++){
			double sum=PI*p[i].r*p[i].r+p[i].s;
			int cnt=1;
			for(int j=n-1;j>=0 && cnt<k;j--)if(i!=j)
				if(t[p[i].id][p[j].id]>=0){
					cnt++;
					sum+=p[j].s;
				}
			ans=max(ans,sum);
		}
		printf("Case #%d: %.8f\n",++kase,ans);
	}
	return 0;
}



