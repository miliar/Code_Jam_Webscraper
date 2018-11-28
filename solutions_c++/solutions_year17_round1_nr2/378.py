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
const int N=55;

int a[N];
int b[N][N];
int f[N][N];
int c[N];
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in","r",stdin);
	freopen("out1002.txt","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		int n,m;scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d",&b[i][j]);
			}
			sort(b[i],b[i]+m);
		}
		int ans=0;
		memset(f,0,sizeof f);
		for(int k=1;;){
			int tui=0;
			memset(c,-1,sizeof c);
			int cnt=0;
			for(int i=0;i<n;i++){
				double mi=a[i]*k*0.9,mx=a[i]*k*1.1;
				for(int j=0;j<m;j++){
					if(f[i][j])continue;
					if(b[i][j]>=mi&&b[i][j]<=mx){
						c[i]=j;
						cnt++;
						break;
					}
				}
				if(mi>b[i][m-1])tui=1;
			}
			if(cnt==n){
				ans++;
				for(int i=0;i<n;i++){
					f[i][c[i]]=1;
				}
			}else{
				k++;
			}
			if(tui)break;
		}
		printf("%d\n",ans);
	}
	return 0;
}









