#include<fstream>
using namespace std;
#include<string.h>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
int t,n,k,b[1010],out;
char a[1010];
int main()
{
	int i,j,s;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;++i)
	{
		fscanf(fin,"%s%d",a,&k);
		n=strlen(a);
		out=0;
		for(j=0;j<n;++j)b[j]=(a[j]=='+');
		for(j=0;j<=n-k;++j)
		{
			if(!b[j])
			{
				out++;
				for(s=j;s<j+k;++s)b[s]=1-b[s];
			}
		}
		for(j=n-k;j<n;++j)if(!b[j])break;
		if(j<n)fprintf(fout,"Case #%d: IMPOSSIBLE\n",i);
		else fprintf(fout,"Case #%d: %d\n",i,out);
	}
	fcloseall();
	return 0;
}