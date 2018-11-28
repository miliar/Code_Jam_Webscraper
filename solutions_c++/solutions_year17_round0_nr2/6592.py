#include<fstream>
using namespace std;
#include<string.h>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
int t,m,a[30],b[30];
char n[30];
void back(int p)
{
	if(p==0)
	{
		b[p]--;
		return;
	}
	if(b[p]>1)
	{
		b[p]--;
		if(b[p]<b[p-1])
		{
			back(p-1);
			b[p]=9;
		}
	}
	else
	{
		back(p-1);
		b[p]=9;
	}
}
int main()
{
	int i,j,k;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;++i)
	{
		fscanf(fin,"%s",n);
		m=strlen(n);
		for(j=0;j<m;++j)a[j]=n[j]-'0';
		b[0]=a[0];
		for(j=1;j<m;++j)
		{
			if(a[j]<b[j-1])
			{
				back(j-1);
				for(k=j;k<m;++k)b[k]=9;
				break;
			}
			b[j]=a[j];
		}
		fprintf(fout,"Case #%d: ",i);
		for(j=0;j<m;++j)if(b[j])break;
		for(;j<m;++j)fprintf(fout,"%d",b[j]);
		fprintf(fout,"\n");
	}
	fcloseall();
	return 0;
}