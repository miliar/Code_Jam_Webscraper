#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <utility>
#include <complex>
#include <functional>
#include <bitset>
#include <time.h>
#include <assert.h>
#define ff first
#define ss second
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
template <class T> inline void umin(T &a,T b){a=min(a,b);}
template <class T> inline void umax(T &a,T b){a=max(a,b);}
const int INF=0x3f3f3f3f;
LL mod=1e9+7;
const int N=100005;

int main() {
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);
	//freopen("A-large.in","r",stdin);
	freopen("out1001.txt","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		int n,m,r;scanf("%d%d%d",&n,&r,&m);
		multiset<int> a,b;
		int cnt1=0,cnt2=0;
		for(int i=1;i<=m;i++){
			int x,y;
			scanf("%d%d",&x,&y);
			if(y==1){
				if(x==1)cnt1++;
				else a.insert(x);
			}else{
				if(x==1)cnt2++;
				else b.insert(x);
			}
		}
		int ans=0,sb=0;
		while(cnt1>0&&b.size()>0){
			int gs=0;
			auto et=b.begin();
			for(auto it=b.begin();it!=b.end();it++){
				if(a.count(*it)>gs){
					gs=a.count(*it);
					et=it;
					sb++;
				}
			}
			b.erase(et);
			cnt1--;
			ans++;
		}
		while(cnt2>0&&a.size()>0){
			int gs=0;
			auto et=a.begin();
			for(auto it=a.begin();it!=a.end();it++){
				if(b.count(*it)>gs){
					gs=b.count(*it);
					et=it;
					sb++;
				}
			}
			a.erase(et);
			cnt2--;
			ans++;
		}
		ans+=max(a.size()+cnt1,b.size()+cnt2);
		printf("%d %d\n",ans,sb);		
	}
	return 0;
}









