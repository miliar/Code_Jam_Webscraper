#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <functional>
#include <math.h>
#define LL long long int
#define ii pair< double,double >
#define iii pair< ii , int > 
#define vi vector<int>
#define vii vector<ii>
#define II pair< LL , LL >
#define III pair< LL  , LL > 
#define vI vector<LL>
#define rI(B) scanf("%d",&B)
#define wI(B) printf("%d",B)
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("C-small-attempt0.in"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define INF 1e12
using namespace std;
double dp[110][110];
double dists[110];
vii horses;
int n;
double solve(int idx,int horseId){
	double dist=dists[idx]-dists[horseId];
	if(dist>horses[horseId].first) return dp[idx][horseId]=INF;
	if(idx==n-1) return 0;
	if(dp[idx][horseId]!=-1) return dp[idx][horseId];
	
	if(dist>horses[horseId].first) return dp[idx][horseId]=INF;
	double sol=((dists[idx+1]-dists[idx])/horses[horseId].second)+solve(idx+1,horseId);
	sol=min(sol,((dists[idx+1]-dists[idx])/horses[idx].second)+solve(idx+1,idx));
	return dp[idx][horseId]=sol;
}
int main(){
	R_W;
	int t;
	cin>>t;
	int cases=1;
	while(t--)
	{
		horses.clear();
		int q;
		cin>>n>>q;
		r(n){
			int a,b;
			cin>>a>>b;
			horses.push_back(ii(a,b));
		}
		int a,b;
		
		dists[0]=0;
		r(n){
			for(int j=0;j<n;j++)
			{
				dp[i][j]=-1;
				int in;
				cin>>in;
				if(in!=-1)
				{
					dists[i+1]=dists[i]+in;
				}
			}
		}
		cin>>a>>b;
		printf("Case #%d: %.10lf\n",cases++,solve(0,0));
	}
	
	return 0;
}