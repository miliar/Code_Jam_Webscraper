#include <stdio.h>
#include <string.h>

using namespace std;

int main(void)
{
	FILE *in=fopen("1.inp","r");
	FILE *out=fopen("1.out","w");
	int t,tt,k,len,i,j,sw,cnt;
	char s[1001];
	fscanf(in,"%d",&t);	
	for(tt=1;tt<=t;tt++)
	{
		fscanf(in,"%s%d",s,&k);
		len=strlen(s);
		cnt=0;
		for(i=len-1;i>=k-1;i--)
		{
			if(s[i]=='-')
			{	
				for(j=i;j>i-k;j--)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				cnt++;		
			}
		}
		fprintf(out,"Case #%d: ",tt);
		sw=1;
		for(i=0;i<len;i++)
			if(s[i]=='-')
				sw=0;
		if(sw==1)
			fprintf(out,"%d\n",cnt);
		else
			fprintf(out,"IMPOSSIBLE\n");
	}
	return 0;
}
