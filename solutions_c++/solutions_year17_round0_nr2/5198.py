#include <stdio.h>
#include <string.h>

using namespace std;

int main(void)
{
	FILE *in=fopen("1.inp","r");
	FILE *out=fopen("1.out","w");
	int t,tt,res,len,i,j,sw;
	char s[20];
	fscanf(in,"%d",&t);	
	for(tt=1;tt<=t;tt++)
	{
		fscanf(in,"%s",s);
		len=strlen(s);
		sw=0;
		for(i=1;i<len;i++)
		{
			if(sw==1)
				s[i]='9';
			else if(s[i]<s[i-1])
			{
				sw=1;
				s[i]='9';
				s[i-1]--;
				for(j=i-1;j>0;j--)
				{
					if(s[j]<'0' || s[j]<s[j-1])
					{
						s[j]='9';
						s[j-1]--;
					}
					else
						break;
				}
			}
		}
		fprintf(out,"Case #%d: ",tt);
		if(s[0]=='0')
			for(i=1;i<len;i++)
				fprintf(out,"%c",s[i]);
		else
			fprintf(out,"%s",s);
		fprintf(out,"\n");
	}
	return 0;
}
