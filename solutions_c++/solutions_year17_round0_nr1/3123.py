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
char s[1010];
int a[1010];
int main()
{
	int T,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int icase = 1;icase <= T;icase++){
		memset(s,0,sizeof(s));
		
		scanf("%s%d",s,&k);
		int len =strlen(s);
		for(int i = 0;i < len;i++)
			if(s[i]=='+')
				a[i] = 1;
			else
				a[i] = 0;
		int cnt = 0;
		for(int i = 0;i <= len-k;i++)
			if(a[i]==0){
				cnt++;
				for(int j = i;j < i+k;j++)
					a[j] = (a[j]+1)%2;
			}
		int flag = 1;
		for(int i = 0;i < len;i++)
			if(a[i]==0)
				flag = 0;
		printf("Case #%d: ",icase);
		if(flag)
			printf("%d\n",cnt);
		else
			printf("IMPOSSIBLE\n");
		
			
	}


	return 0;
}

