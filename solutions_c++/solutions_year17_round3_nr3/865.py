#include<fstream>
using namespace std;
#include<algorithm>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
int t,n,k;
double a[60],u,out;
int main()
{
	int i,j,p;
	double d;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;++i)
	{
		fscanf(fin,"%d%d",&n,&k);
		fscanf(fin,"%lf",&u);
		for(j=1;j<=n;++j)fscanf(fin,"%lf",&a[j]);
		out=1;
		sort(&a[1],&a[n+1]);
		a[n+1]=1;
		if(n==k)
		{
			while(u>1e-9)
			{
				for(p=2;p<=n;++p)if(a[p]-a[1]>1e-9)break;
				d=(a[p]-a[1])*(p-1);
				if(d<=u+1e-9)
				{
					u=u-d;
					for(j=1;j<p;++j)a[j]=a[p];
				}
				else
				{
					for(j=1;j<p;++j)a[j]=a[j]+u/(p-1);
					break;
				}
			}
			for(j=1;j<=n;++j)out=out*a[j];
		}
		fprintf(fout,"Case #%d: %.14lf\n",i,out);
		fflush(fout);
	}
	return 0;
}
