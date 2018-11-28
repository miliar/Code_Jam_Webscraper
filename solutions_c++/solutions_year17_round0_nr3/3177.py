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

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	LL k,n;
	for(int icase = 1;icase <= T;icase++){
		scanf("%lld%lld",&n,&k);
		printf("Case #%d: ",icase);
		LL ct = 0,y = 1;
		for(int i = 1;i <= 100;i++){
			ct += y;
			if(ct>=k){
				LL x = n-ct+y;
				LL z = x/y+((x%y)>=(k-ct+y));
				printf("%lld %lld\n",z/2,(z-1)/2);
				break;
			}
			y*=2;
			
		} 
	}

	return 0;
}

