#include <bits/stdc++.h>

using namespace std;

FILE *fp, *fw;

void work()
{
	int n, len;
	char s[1011];
	fscanf(fp,"%s %d",s+1,&n);
	len = strlen(s+1);
	
	//cout<<n<<" "<<len<<endl;
	int cnt = 0;
	for (int i=1;i<=len-n+1;i++)
	{
		if (s[i] == '-')
		{
			cnt++;
			for (int j=i;j<=i+n-1;j++)
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
		}
	}
	for (int i=1;i<=len;i++) if (s[i] == '-')
	{
		fprintf(fw,"IMPOSSIBLE");
		return;
	}
	fprintf(fw,"%d",cnt);
}
int main()
{
	fp = fopen("test.in","r");
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