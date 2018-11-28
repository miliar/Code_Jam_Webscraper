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
char s[N];
int main() {
#ifndef ONLINE_JUDGE
	//freopen("in.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("1002.out","w",stdout);
#endif
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;cas++){
		printf("Case #%d: ",cas);
		LL ans=0;
		scanf("%s",s);
		int n=strlen(s);
		while(1){
			int ok=1;
			for(int i=0;i<n-1;i++){
				if(s[i+1]<s[i]){
					ok=0;
					if(s[i]=='0')s[i]='9';
					else s[i]--;
					for(int j=i+1;j<n;j++){
						s[j]='9';	
					}
					
					break;
				}
			}
			
			if(ok)break;
		}
		if(s[0]!='0')putchar(s[0]);
		for(int i=1;i<n;i++)putchar(s[i]);
		putchar('\n');
	}
	return 0;
}









