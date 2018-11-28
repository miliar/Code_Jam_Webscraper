
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#define eps 1e-8
#define MAXN 100050
using namespace std;
char s[MAXN];
int a[MAXN];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tt,k,ri=0;
	scanf("%d",&tt);
	while(tt--){
		scanf(" %s%d",s,&k);
		int n=strlen(s);
		for(int i=0;i<n;++i)
			a[i]=(s[i]=='+');
		int flag=0;
		for(int i=0;i<n;++i){
			if(a[i]==0){
				if(i+k>n){
					flag=-1;
					break;
				}
				flag++;
				for(int j=i;j<i+k;++j)
					a[j]=1-a[j];
			}
		}
		printf("Case #%d: ",++ri);
		if(flag==-1)printf("IMPOSSIBLE\n");
		else
			printf("%d\n",flag);
	}
	return 0;
}
