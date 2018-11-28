#include<iostream>
#include<algorithm>
#include<cctype>
#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>
#include<set>
#include<cmath>
#include<queue>
#include<ctime>
typedef long long LL;
using namespace std;
int a[30];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	LL x;
	for(int icase = 1;icase <= T;icase++){
		scanf("%lld",&x);
		memset(a,0,sizeof(a));
		int len = 0;
		while(x>0){
			a[len] = x%10;
			a[len++];
			x/=10;
		}
		for(int i = 0;i<len-1;i++)
			if(a[i] < a[i+1]){
				a[i+1]--;
				for(int j = 0;j <= i;j++)
					a[j] = 9;
			}
		printf("Case #%d: ",icase);
		int flag = 0;
		for(int i = 20;i >= 0;i--){
			if(a[i]>0)
				flag = 1;
			if(flag)
				printf("%d",a[i]);
		}
		printf("\n");
	}

	return 0;
}

