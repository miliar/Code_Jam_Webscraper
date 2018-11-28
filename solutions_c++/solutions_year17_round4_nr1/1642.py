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
int a[5];

int main() {
#ifndef ONLINE_JUDGE
	//freopen("in.txt","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out1001.txt","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		int n,p;
		scanf("%d%d",&n,&p);
		memset(a,0,sizeof a);
		for(int i=0;i<n;i++){
			int x;
			scanf("%d",&x);
			a[x%p]++;
		}
		int ans=a[0];
		if(p==2){
			ans+=(a[1]+1)/2;
		}else if(p==3){
			if(a[1]<=a[2]){
				ans+=a[1];
				ans+=(a[2]-a[1]+2)/3;
			}else{
				ans+=a[2];
				ans+=(a[1]-a[2]+2)/3;
			}
		}else{
			;
		}
		printf("%d\n",ans);		
	}
	return 0;
}









