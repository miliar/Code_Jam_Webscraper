//#include<bits/stdc++.h>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<iostream>
#include<algorithm>
#define vi vector<LL>
#define pii pair<int,int>
#define pll pair<LL,LL>
#define fr first
#define sc second
#define MAX 50010
#define LL   long long int
#define ll   long long int
//#define LLL long long int
#define inf 1e18
#define INF 10000000
#define mod 1000000007
#define N 65
#define mMax 30010
#define nMax 2010
#define SZ(a) a.size()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define all(A) A.begin(),A.end()
using namespace std;
LL bigmod(LL a,LL b,LL Mod)
{
    if(b==0) return 1ll;
    if(b%2) return (a*bigmod(a,b-1,Mod))%Mod;
    LL c=bigmod(a,b/2,Mod);
    return (c*c)%Mod;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	int T,I=1;
	cin>>T;
	//cout<<LONG_LONG_MAX;
	while(T--)
	{
		printf("Case #%d: ",I++);
		LL n,k;
		scanf("%lld %lld",&n,&k);
		map<LL,LL> Map;
		vector<pll > A;
		LL x,y;
		if(k==1)
		{
			y=(n-1)/2;
			x=n/2;
		}
		k--;
		A.push_back(mp(n,1));
		while(k>0)
		{
			Map.clear();
			for(int i=0;i<A.size();i++)
			{
				LL a=A[i].fr;
				Map[(a-1)/2]+=A[i].sc;
				Map[a/2]+=A[i].sc;
			}
			A.clear();
			for(map<LL,LL> ::iterator it=Map.begin();it!=Map.end();it++)
			{
				A.push_back(*it);
			}
			sort(all(A));
			for(int i=A.size()-1;i>=0;i--)
			{
				if(A[i].sc >= k)
				{
					k=0;
					y=(A[i].fr-1)/2;
					x=A[i].fr/2;
					break;
				}
				else k-=A[i].sc;
			}
		}
		printf("%lld %lld\n",x,y);
	}
	return 0;
}
