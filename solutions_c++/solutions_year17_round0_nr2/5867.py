#include <bits/stdc++.h>

using namespace std;
#define LL long long
FILE *fp, *fw;

void work()
{
	LL n;
	fscanf(fp,"%lld",&n);
	int a[22], num = 0;
	int ans[22];
	while (n!=0)
	{
		a[++num] = n%10;
		n/=10;
	}
	
	ans[num] = a[num];
	for (int i=num-1;i>=1;i--)
	{
		if (a[i] < ans[i+1])
		{
			int t = i;ans[i] = a[i];
			while (t<num && ans[t] <ans[t+1])
			{
				ans[t+1]--,t++;
			}
			for (int j=t-1;j>=1;j--) ans[j] = 9;
			break;
		}
		else
		{
			ans[i] = a[i];
		}
	}
	LL tot=0;
	for (int i=num;i>=1;i--) tot = tot*10 + ans[i];
	
	fprintf(fw,"%lld",tot);
	
}
int main()
{
	fp = fopen("input.in","r");
	fw = fopen("output.out","w");
	int T;
	fscanf(fp,"%d",&T);
	for (int i=1;i<=T;i++)
	{
		fprintf(fw,"Case #%d: ",i);
		work();
		if (i!=T) fprintf(fw,"\n");
	}
	fclose(fp);
	fclose(fw);
}