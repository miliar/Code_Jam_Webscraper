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
#define R_W R("A-large (1).in"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define EPS 1e-12
using namespace std;
vector< pair< double,double > > vals; 
bool solve(double speed,double target){
	for(int nxt=0;nxt<vals.size();nxt++)
	{
		double delta=vals[nxt].first;
		double tget=(delta)/(speed-vals[nxt].second);
		if(tget<0) continue;
		double dist=tget*speed;
		if(dist<target) return false;
	}
	return true;
}
int main(){
	R_W;
	
	int n;
	cin>>n;
	int cases=1;
	while(n--)
	{
		vals.clear();
		double target,hs;
		cin>>target>>hs;
		r(hs){
			int a,b;
			cin>>a>>b;
			vals.push_back(ii(a,b));
		}
		double l=0,r=999999999999999999;
		double mid;
		r(200)
		{
			mid=(l+r)/2;
			if(solve(mid,target))
			{
				l=mid;
			}else
			{
				r=mid;
			}
		}
		if(solve(l,target)) mid=max(mid,l);
		if(solve(r,target)) mid=max(mid,r);
		printf("Case #%d: %.10lf\n",cases++,mid);
	}
	
	return 0;
}