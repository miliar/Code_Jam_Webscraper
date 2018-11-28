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
const int N=1005;

char s[N];
int main() {
#ifndef ONLINE_JUDGE
	//freopen("A-large.in","r",stdin);
	//freopen("1001out","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		int m;
		scanf("%s%d",s,&m);
		int n=strlen(s);
		for(int i=0;i<n;i++){
			s[i]=s[i]=='+'?1:0;
		}
		int ans=0;
		int ok=1;
		for(int i=0;i<n;i++){
			if(s[i]==0){
				ans++;
				for(int j=i;j<i+m;j++){
					if(j>=n){
						ok=0;
						break;
					}
					s[j]=!s[j];
				}
			}
		}
		if(ok==0){
			puts("IMPOSSIBLE");
		}else{
			printf("%d\n",ans);
		}
	}
	return 0;
}









