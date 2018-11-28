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
const int N=30;

char s[N][N];
int a[N];
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("out1001.txt","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d:\n",cas);
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++){
			scanf("%s",s[i]);
		}
		int fi=-1;
		for(int i=0;i<n;i++){
			a[i]=0;
			for(int j=0;j<m;j++){
				if(s[i][j]!='?'){
					a[i]=s[i][j];
					break;
				}			
			}
			if(fi==-1&&a[i]!=0){
				fi=i;
			}
		}
			int t=a[fi];
			for(int j=0;j<m;j++){
				if(s[fi][j]!='?')t=s[fi][j];
				for(int i=0;i<fi;i++){
					s[i][j]=t;
				}
			}
		
		
		for(int i=fi;i<n;){
			int k;
			for(k=i+1;k<n;k++){
				if(a[k])break;
			}
			int t=a[i];
			for(int j=0;j<m;j++){
				if(s[i][j]!='?')t=s[i][j];
				for(int u=i;u<k;u++){
					s[u][j]=t;
				}
			}
			i=k;
		}
		
		for(int i=0;i<n;i++){
			puts(s[i]);
		}
	}
	return 0;
}









