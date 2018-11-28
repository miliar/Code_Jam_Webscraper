
/*gcj-2017-qr-a1*/
#include<stdio.h>
#include<string.h>
#define MAXN 1005

int n, k, dir[MAXN], f[MAXN];
char s[MAXN];

int counting()
{
	memset(f, 0, sizeof(f));
	int ans=0, sum=0;
	for(int i=0; i+k<=n; i++)
	{
		if((dir[i]+sum)%2!=0)
		{
			ans++;
			f[i]=1;
		}
		sum+=f[i];
		if(i-k+1>=0) sum-=f[i-k+1];
	}
	for(int i=n-k+1; i<n; i++)
	{
		if((dir[i]+sum)%2!=0)
		{
			return -1;
		}
		if(i-k+1>=0) sum-=f[i-k+1];
	}
	return ans;
}

void sol()
{
	int status=counting();
	if(status==-1) printf("IMPOSSIBLE\n");
	else printf("%d\n", status);
}

int main()
{
	freopen("660.in", "r", stdin);
	freopen("660out.txt", "w", stdout);
	int tcases, kase=1;
	for(scanf("%d", &tcases); tcases--;)
	{
		scanf("%s%d", s, &k);
		n=strlen(s);
		for(int i=0; i<n; i++)
		{
			if(s[i]=='+') dir[i]=0;
			else dir[i]=1;
		}
		printf("Case #%d: ", kase++);
		sol();
	}
	return 0;
}
