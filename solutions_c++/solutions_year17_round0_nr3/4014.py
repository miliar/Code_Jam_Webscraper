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
#include <set>
#include <vector>
#include <cstdlib>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define mpii(a,b) make_pair(a,b)
const ll INF=1ll<<60;
const int maxn=100;
const int mod=1000000007;

int T,kase=0;
ll n,k;
set<ll>d[maxn];
ll cnt[maxn][2];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("tan_out.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%I64d%I64d",&n,&k);
		k--;
		int depth=0;
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<maxn;i++)d[i].clear();
		d[0].insert(n);
		cnt[0][0]=1;
		for(int i=0;i<maxn;i++){
			set<ll>::iterator it=d[i].begin();
			if(d[i].size()==1){
				ll a=*it;
				if(a==0){
					depth=i+1;
					d[i+1].insert(0);
					break;
				}
				a--;
				d[i+1].insert(a/2);
				if(a & 1){
					d[i+1].insert((a+1)/2);
					cnt[i+1][0]=cnt[i+1][1]=cnt[i][0];
				}
				else cnt[i+1][0]=2*cnt[i][0];
			}
			else {
				ll a=*it;it++;
				ll b=*it;
				if(a==0){
					depth=i+1;
					d[i+1].insert(0);
					break;
				}
				a--;b--;
				d[i+1].insert(a/2);
				d[i+1].insert(b/2);
				if(a & 1){
					cnt[i+1][0]+=cnt[i][0];
					cnt[i+1][1]+=cnt[i][0];
					d[i+1].insert((a+1)/2);
				}
				else cnt[i+1][0]+=2*cnt[i][0];
				if(b & 1){
					cnt[i+1][0]+=cnt[i][1];
					cnt[i+1][1]+=cnt[i][1];
					d[i+1].insert((b+1)/2);
				}
				else cnt[i+1][1]+=2*cnt[i][1];
			}
		}
		/*
		for(int i=0;i<=depth;i++){
			printf("depth=%d		",i);
			for(set<ll>::iterator it=d[i].begin();it!=d[i].end();it++)
				cout<<*it<<" ";
			cout<<endl;
		}*/
		ll sum=0;
		int fin=0;
		for(int i=0;i<=depth;i++){
			if(sum+(1ll<<i)>k){
				fin=i;
				break;
			}
			sum+=(1ll<<i);
		}
		printf("Case #%d: ",++kase);
		if(d[fin].size()==1){
			set<ll>::iterator it=d[fin].begin();
			ll ans=*it;
			cout<<ans/2<<" ";
			if(ans & 1)cout<<ans/2<<endl;
			else cout<<(ans-1)/2<<endl;
		}
		else {
			set<ll>::iterator it=d[fin].end();
			it--;
			ll ans=*it;
			if(k-sum>=cnt[fin][1]){it--;ans=*it;}
			cout<<ans/2<<" ";
			if(ans & 1)cout<<ans/2<<endl;
			else cout<<(ans-1)/2<<endl;
		}
	}
	return 0;
}



